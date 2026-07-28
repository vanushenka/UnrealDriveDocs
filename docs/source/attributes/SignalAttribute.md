# Signal Attribute

A stepped per-lane attribute that places a **traffic signal** (traffic light or pedestrian light) on a lane —
the MetaRoad analog of an OpenDRIVE `<signal>`. A signal key marks *where* the signal stands and *which lane it
controls*; the actual light sequencing (red/green phases) lives on a
[Traffic Controller](/traffic/TrafficController.md) component that the signal is linked to.

```{note}
The lane itself gives the signal its meaning: placing a key on a lane defines the controlled lane **and** the
traffic direction — no extra "orientation" or "validity" fields are needed. The centre line cannot carry
signals; add them to real lanes only.
```

<!-- TODO 📷 screenshot: a junction with several signal keys — poles with colored heads and association arrows along the lanes → /img/signal-attribute.png -->

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Kind` | Traffic Light | `Traffic Light` (vehicle, 3-section) or `Pedestrian Light` (2-section). |
| `ZOffset` | 500 cm | Height of the signal head above the road surface. |
| `Country` | *(empty)* | OpenDRIVE country code override. Empty = `OpenDRIVE` (the de-facto catalog for dynamic signals). |
| `Type` | *(empty)* | OpenDRIVE type override. Empty = derived from `Kind`: `1000001` (3-section light) or `1000002` (pedestrian light). |
| `SubType` | *(empty)* | OpenDRIVE subtype override. Empty = `-1`. |
| `SignalId` | *(auto)* | Read-only stable identity of this signal. Controller links and future exports address the signal by this id — it survives copy/paste and duplication. |

The `Country` / `Type` / `SubType` overrides exist for round-tripping with external formats — leave them empty
unless you need a specific OpenDRIVE signal code.

## Placement and the validity segment

Add the attribute in [Attribute Mode](/editing/AttributeMode.md) like any other: pick **Signal** in the attribute
tree, pin it to a lane and place keys. Each key controls the stretch of lane **from its position to the next key
downstream** (or to the lane's end) — shown in the viewport as a guide line with an arrowhead pointing along the
traffic direction. On reverse-direction lanes the segment correctly runs against the spline direction.

Typical placement is on the **approach lane right before the junction** — like a real stop line — one key per
controlled lane.

<!-- TODO 🎞 gif: adding a Signal key to a lane in Attribute mode; the guide arrow appears along the lane → /img/signal-add.gif -->

## Linking to a controller

An unlinked signal draws in a neutral color. Right-click a **selected** signal key to get the **Traffic Signal**
menu section:

- **Link to \<controller\>** — attach the signal to one of the actor's
  [Traffic Controllers](/traffic/TrafficController.md).
- **Unlink from \<controller\>** — detach it.
- **Set State in Phase '…'** — set this signal's state in the controller's currently previewed phase.

Once linked, the head and the guide line take the **color of the signal's state in the previewed phase**
(red / red-yellow / green / yellow / gray for Off).

<!-- TODO 🎞 gif: right-clicking a signal key → Link to controller → the head turns to the phase state color → /img/signal-link.gif -->

## See also

- [Traffic Controller](/traffic/TrafficController.md) — phases, states and the runtime clock.
- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
