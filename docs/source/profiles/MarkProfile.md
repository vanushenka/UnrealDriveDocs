# Mark Profile

A **Mark Profile** (`URoadMarkProfile`) defines a single **road-marking strip** — its type, dimensions, and color — for
**driving** lanes (`RoadLaneDriving`). The [Road Mark Attribute](/attributes/RoadMarkAttribute.md) then paints the strip
along a lane.

![A Mark Profile](/img/preset-mark.png)

Create one from the Content Browser (**right-click → Meta Road → Mark Profile**); **double-click** it to open the Mark
Profile editor.

## The Mark Profile editor

- **Preview viewport** — a live preview of the marking strip as you edit it.
- **Details panel** — the marking definition.

![The Mark Profile editor previewing a marking strip](/img/mark-editor.png)

Changes update the preview immediately.

## Properties

The marking definition (`FRoadLaneMarkProfile`) controls the strip's appearance:

| Property | Description |
|----------|-------------|
| `Type` | Marking style: `None`, `Solid`, `Broken`, `Double Solid`, `Double Broken`, `Solid Broken`, `Broken Solid`, `Custom`. |
| `Dimensions` | Strip width, and for broken marks the dash length and gap. |
| `Color / Material` | Color and material applied to the strip. |

```{note}
`Type` is **metadata**, not geometry. The strip's appearance comes from the dimensions and material below it;
`Type` labels what kind of marking it is, so your own systems — traffic generation, HD-map export, lane-change
rules — can read it. Changing it does not change what is baked.
```

```{note}
**Renamed in 3.2.0.** The `Broked` spellings became `Broken`: `Broked → Broken`, `Double Broked → Double Broken`,
`Solid Broked → Solid Broken`, `Broked Solid → Broken Solid`. Existing assets are redirected automatically and
keep their value; only the label in the dropdown changed. The asset **file names** in the shipped library still
use the old spelling, and are left alone deliberately so existing references keep resolving.
```

## How it's used

- Referenced by the `Profile` of a [Road Mark Attribute](/attributes/RoadMarkAttribute.md) key.
- Can be **[dragged from the Content Browser onto a road lane](/profiles/Profiles.md#drag-and-drop)** to set that lane's
  road-mark attribute directly.

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Road Mark Attribute](/attributes/RoadMarkAttribute.md) — paints a Mark Profile along a lane.
