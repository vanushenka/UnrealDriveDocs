# C++ API

This page covers common patterns for working with MetaRoad data from C++ at runtime: reading the road layout, querying lane positions, evaluating attributes, and extending the plugin with custom attribute and zone types.

> **Module:** `MetaRoad` (runtime). Add it to your module's `PublicDependencyModuleNames` in the `.Build.cs` file.

---

## Finding Road Components

`URoadSplineComponent` is a standard `UActorComponent`. Use normal UE traversal to find instances in the world:

```cpp
// Iterate all actors in the world that contain a URoadSplineComponent
for (TActorIterator<AActor> It(GetWorld()); It; ++It)
{
    URoadSplineComponent* Road = It->FindComponentByClass<URoadSplineComponent>();
    if (Road)
    {
        // work with Road
    }
}
```

Or, if you placed roads inside known actors, keep direct references in your game code.

---

## Reading the Road Layout

`URoadSplineComponent` owns an `FRoadLayout` which holds the array of `FRoadLaneSection` objects:

```cpp
const FRoadLayout& Layout = RoadSpline->GetRoadLayout();

for (int i = 0; i < Layout.Sections.Num(); ++i)
{
    // Always use GetLeftRighLanes — Left[] or Right[] may be empty
    // in asymmetric layouts (Side == Left or Side == Right).
    auto [LeftLanes, RightLanes] = Layout.GetLeftRighLanes(i);

    for (const FRoadLane& Lane : RightLanes)
    {
        // Lane.LaneIndex > 0 = right side
    }
    for (const FRoadLane& Lane : LeftLanes)
    {
        // Lane.LaneIndex < 0 = left side
    }
}
```

To get a specific lane directly:

```cpp
// Returns nullptr if the combination is invalid
const FRoadLane* Lane = RoadSpline->GetRoadLane(SectionIndex, LaneIndex);
```

Lane index conventions:
- `0` (`MetaRoad::ZeroLaneIndex`) — invalid / reference centerline, no width
- `> 0` — right of the reference spline
- `< 0` — left of the reference spline

---

## Evaluating Lane Positions

### World position at a given arc length

```cpp
// Alpha: 0.0 = inner edge (nearest center), 1.0 = outer edge
// Note: function name has a typo ("Poistion") — it is Blueprint-exposed and cannot be renamed.
FVector Pos = RoadSpline->EvalLanePoistion(
    SectionIndex, LaneIndex,
    /*S=*/ 500.0,
    /*Alpha=*/ 0.5,          // lane center
    ESplineCoordinateSpace::World);
```

### Full road position (position + orientation)

```cpp
FRoadPosition RoadPos = RoadSpline->GetRoadPosition(
    SectionIndex, LaneIndex,
    /*Alpha=*/ 1.0,          // outer edge
    /*SOffset=*/ 500.0,
    ESplineCoordinateSpace::World);

FVector WorldLoc  = RoadPos.Location;
FQuat   WorldQuat = RoadPos.Quat;     // forward = lane direction
double  S         = RoadPos.SOffset;
double  R         = RoadPos.ROffset;  // positive = right of center
```

### Arc-length range of a lane

```cpp
URoadSplineComponent::FRang Range = RoadSpline->GetLaneRang(SectionIndex, LaneIndex);
double StartS = Range.StartS;
double EndS   = Range.EndS;
```

### Hit-testing against lane geometry

```cpp
FRoadHitResult Hit;
if (RoadSpline->LineTrace(Start, End, Hit))
{
    FVector  HitPt       = Hit.HitPoint;
    int32    SectionIdx  = Hit.SectionIndex;
    int32    LaneIdx     = Hit.LaneIndex;
}
```

---

## Lane Attribute Queries

Attributes are stored per lane as a map from descriptor class to `FRoadLaneAttribute`:

```cpp
#include "Assets/RoadLaneAttributeDescriptor.h"
#include "Assets/RoadLaneAttributeSpeed.h" // example

const FRoadLane* Lane = RoadSpline->GetRoadLane(SectionIndex, LaneIndex);
if (!Lane) return;

const FRoadLaneAttribute* SpeedAttr =
    Lane->Attributes.Find(URoadLaneAttributeSpeed::StaticClass());

if (SpeedAttr && SpeedAttr->CanEvaluate())
{
    FRoadLaneAttributeValueSpeed SpeedVal =
        SpeedAttr->Evaluate<FRoadLaneAttributeValueSpeed>(SOffset);
    float MaxSpeedMS = SpeedVal.MaxSpeed; // metres per second
}
```

`Evaluate<T>()` returns the stepped or interpolated value at the requested arc-length position, depending on whether the value type overrides `CanInterpolate()`.

---

## Custom Attribute Types

Custom attributes let you attach arbitrary per-lane data (e.g. traffic density, vegetation type, surface roughness) that varies along the lane.

### Step 1 — Define the value struct

```cpp
// MyRoadAttribute.h
#include "RoadLaneAttribute.h"
#include "MyRoadAttribute.generated.h"

USTRUCT(BlueprintType)
struct FMyRoadAttributeValue : public FRoadLaneAttributeValue
{
    GENERATED_USTRUCT_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = MyAttribute)
    float Density = 1.0f;

    // Stepped evaluation (default). Override to return true for cubic blending.
    virtual bool CanInterpolate() const override { return false; }

    // Called only when CanInterpolate() == true.
    // Alpha [0,1]: 0 = at this key, 1 = at the next key.
    virtual bool Interpolate(const UScriptStruct* ValueType,
        const FRoadLaneAttributeValue* Other, float Alpha,
        FRoadLaneAttributeValue* Out) const override
    {
        // Example linear blend:
        const FMyRoadAttributeValue* OtherVal = static_cast<const FMyRoadAttributeValue*>(Other);
        FMyRoadAttributeValue* OutVal = static_cast<FMyRoadAttributeValue*>(Out);
        OutVal->Density = FMath::Lerp(Density, OtherVal->Density, Alpha);
        return true;
    }

    // Lateral position [0,1] for rendering the key handle in the editor.
    // 0.0 = inner edge, 0.5 = lane center (default), 1.0 = outer edge.
    virtual double GetKeyAlpha() const override { return 0.5; }
};
```

### Step 2 — Register the descriptor

```cpp
// URoadLaneAttributeDescriptor subclass — acts as the "type key" for the attribute map.
#include "Assets/RoadLaneAttributeDescriptor.h"
#include "MyRoadAttributeDescriptor.generated.h"

UCLASS()
class UMyRoadAttributeDescriptor : public URoadLaneAttributeDescriptor
{
    GENERATED_BODY()
public:
    virtual TConstStructView<FRoadLaneAttributeValue> GetAttributeValueTemplate() const override
    {
        static FMyRoadAttributeValue Default;
        return TConstStructView<FRoadLaneAttributeValue>::Make(Default);
    }
};
```

Once this class exists, it is automatically available in the editor's **Attribute Modes** menu (no further registration needed).

### Step 3 — Evaluate at runtime

```cpp
const FRoadLane* Lane = RoadSpline->GetRoadLane(SectionIndex, LaneIndex);
if (const FRoadLaneAttribute* Attr = Lane->Attributes.Find(UMyRoadAttributeDescriptor::StaticClass()))
{
    FMyRoadAttributeValue Val = Attr->Evaluate<FMyRoadAttributeValue>(SOffset);
    float Density = Val.Density;
}
```

---

## Custom Zone Types

Zone types define the surface category of a lane (Driving, Sidewalk, Marking, etc.). To register a custom type:

1. Open **Edit → Project Settings → Plugins → MetaRoad**
2. In **Road Zone Types**, add a new entry with a unique `FName` key
3. Fill in `FRoadZoneTypeDetails`: material, decal material, material priority, editor color

The type is then available in the **Zone Type** dropdown on any `FRoadLane` or `FRoadZone`.

From C++, read the registered types via:

```cpp
#include "MetaRoadSettings.h"

const UMetaRoadSettings* Settings = GetDefault<UMetaRoadSettings>();
const TMap<FName, FRoadZoneTypeDetails>& ZoneTypes = Settings->RoadZoneTypes;
```

---

## `UpdateLayout()` Lifecycle

After any programmatic change to `RoadLayout.Sections[]` (adding/removing sections or lanes, changing `SOffset`), call:

```cpp
RoadSpline->UpdateRoadLayout();         // rebuilds back-pointers (SectionIndex, LaneIndex, OwnedRoadLayout)
RoadSpline->UpdateLaneSectionBounds();  // recomputes SOffsetEnd based on current spline length
RoadSpline->TrimLaneSections();         // removes sections outside [0, SplineLength]
RoadSpline->MarkRoadStateDirty();       // queues procedural regeneration
```

Skipping `UpdateRoadLayout()` leaves `LaneIndex`, `SectionIndex`, and `OwnedRoadLayout` stale — subsequent queries will return wrong results.
