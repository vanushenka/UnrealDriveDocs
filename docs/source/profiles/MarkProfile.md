# Mark Profile

A **Mark Profile** (`URoadMarkProfile`) defines a single **road-marking strip** — its type, dimensions, and colour — for
**driving** lanes (`RoadLaneDriving`). The [Road Mark Attribute](/attributes/RoadMarkAttribute.md) then paints the strip
along a lane.

![A Mark Profile](/img/preset-mark.png)

Create one from the Content Browser (**right-click → Meta Road → Mark Profile**); **double-click** it to open the Mark
Profile editor.

## The Mark Profile editor

- **Preview viewport** — a live preview of the marking strip as you edit it.
- **Details panel** — the marking definition.

![alt text](/img/mark-editor.png)

The marking definition (`FRoadLaneMarkProfile`) controls the strip's appearance:

- **Type** — solid, dashed, or double.
- **Dimensions** — strip width, and for dashed marks the dash length and gap.
- **Colour / material** of the strip.

Changes update the preview immediately.

## How it's used

- Referenced by the `Profile` of a [Road Mark Attribute](/attributes/RoadMarkAttribute.md) key.
- Can be **[dragged from the Content Browser onto a road lane](/profiles/Profiles.md#drag-and-drop)** to set that lane's
  road-mark attribute directly.

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Road Mark Attribute](/attributes/RoadMarkAttribute.md) — paints a Mark Profile along a lane.
