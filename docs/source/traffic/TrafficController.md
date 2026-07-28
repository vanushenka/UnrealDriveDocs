# Traffic Controller

**Meta Traffic Controller** is an actor component that turns a set of [Signal](/attributes/SignalAttribute.md)
keys into a working traffic-light installation: it groups the signals of one junction and drives them through
**phases** — named steps like *"north–south green"*, each with a duration and a state for every linked signal.
It is the MetaRoad analog of an OpenDRIVE `<controller>` combined with an OpenSCENARIO
`TrafficSignalController`.

<!-- TODO 📷 screenshot: a junction with a selected Traffic Controller — signals colored by the previewed phase, association arrows along the controlled lanes → /img/traffic-controller.png -->

```{note}
The controller stores **no geometry and no meshes** — it is pure authored data plus a minimal runtime clock.
Visual light fixtures, AI traffic (MassTraffic) and OpenDRIVE/OpenSCENARIO export are separate steps built on
top of this data.
```

## Adding a controller

Select the road actor and add the component in the Details panel: **Add → Meta Traffic Controller**. An actor
can own **several controllers** — the natural setup is one controller per junction.

<!-- TODO 📷 screenshot: Add Component dropdown with "Meta Traffic Controller" highlighted → /img/traffic-controller-add.png -->

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Display Name` | *(empty)* | Human-readable name shown in menus and labels. |
| `Delay` | 0 s | Initial offset of the phase cycle at runtime — shift several controllers against each other for a "green wave". |
| `Sync Reference` | none | Another controller this one's `Delay` is relative to (mirrors the OpenSCENARIO `reference`/`delay` pair). |
| `Auto Advance` | on | Run the phase cycle automatically in game: each phase lasts its `Duration`, then the next one starts; after the last phase the cycle wraps around. |
| `Phases` | *(empty)* | The phase list — edit it in the panel below, not as a raw array. |

## Linking signals

The controller shows its signals **while the component is selected** (selecting just the actor is not enough):
every signal of the actor is drawn with a pole, a round head and a guide arrow along the controlled lane.

- **Link** — right-click a signal head → **Link to \<controller\>**. Works from the controller's viewport
  visualization and from [Attribute Mode](/editing/AttributeMode.md) alike.
- **Unlink** — right-click a linked signal → **Unlink from \<controller\>**.
- Signals linked to *another* controller draw dimmed; unlinked signals draw in a neutral color.

Links are stored by the signal's stable `SignalId`, so they survive copy/paste, actor duplication and
Blueprint templates — a pasted road keeps its controller wiring, re-pointed at its own copies of the signals.

<!-- TODO 🎞 gif: selecting the controller component, right-clicking a signal head and linking it → /img/traffic-controller-link.gif -->

## Editing phases

The controller's Details panel hosts a phase editor:

- **Phase list** — add, duplicate, rename, set the `Duration` (seconds) and delete phases. The selected phase
  is the **previewed** one: every linked signal in the viewport takes its state color from it.
- **Signal states** — below the list, one row per linked signal with a state dropdown:
  `Off`, `Red`, `Red-Yellow`, `Green`, `Yellow`.
- States can also be set right in the viewport: right-click a linked signal → **Set State in Phase '…'**.

<!-- TODO 📷 screenshot: the Details phase editor — phase list on top, per-signal state combos below → /img/traffic-controller-phases.png -->
<!-- TODO 🎞 gif: switching the selected phase in the list — signal heads in the viewport change colors → /img/traffic-controller-preview.gif -->

## Runtime

In game (PIE or packaged) the controller runs a minimal phase clock:

- With **Auto Advance** on, phases advance by their `Duration`, starting `Delay` seconds into the cycle.
- From Blueprint or C++: `SetPhase(Index)`, `AdvancePhase()`, `GetSignalState(SignalId)`.
- The **On Phase Changed** event fires on every phase switch — bind it to drive your own light meshes,
  sounds or gameplay.

```{tip}
The data model is designed for export: signals map to OpenDRIVE `<signal>` elements, controllers to
`<controller>` + OpenSCENARIO `TrafficSignalController` phases, and phases translate to per-lane open/close
periods for AI traffic (e.g. MassTraffic). These exporters ship separately.
```

## See also

- [Signal Attribute](/attributes/SignalAttribute.md) — placing signals on lanes.
- [Attribute Mode](/editing/AttributeMode.md) — the editing sub-mode signals are authored in.
- [Junctions](/concepts/Junctions.md) — how junctions are modeled with connected splines.
