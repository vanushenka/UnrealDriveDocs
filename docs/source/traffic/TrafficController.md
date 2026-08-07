# Traffic Controller

**Meta Traffic Controller** is an actor component that turns a set of [Signal](/attributes/SignalAttribute.md)
keys into a working traffic-light installation: it groups the signals of one junction and drives them through
**phases** — named steps like *"north–south green"*, each with a duration and a state for every linked signal.
It is the MetaRoad analog of an OpenDRIVE `<controller>` combined with an OpenSCENARIO
`TrafficSignalController`.

![A junction with a selected Traffic Controller: signal heads colored by the previewed phase, with association lines along the controlled lanes](/img/traffic-controller.png)  

```{note}
The controller stores **no geometry and no meshes** — it is pure authored data plus a minimal runtime clock.
Visual light fixtures, AI traffic (MassTraffic) and OpenDRIVE/OpenSCENARIO export are separate steps built on
top of this data.
```

## Adding a controller

Select the road actor and add the component in the Details panel: **Add → Meta Traffic Controller**. An actor
can own **several controllers** — the natural setup is one controller per junction.

![The Add Component dropdown on a road actor with Meta Traffic Controller highlighted](/img/traffic-controller-add.png)  

## Properties

Select the component in the actor's components tree to edit it. The **Traffic Controller** category holds:

| Property | Default | Description |
|----------|---------|-------------|
| `Display Name` | *(empty)* | Human-readable name shown in menus and labels. Falls back to the component's name when empty. |
| `Delay` | 0 s | Delayed start of the phase cycle at runtime: the clock starts at −`Delay`, so the **first** phase lasts `Duration` + `Delay` seconds and every later cycle runs at its plain durations. Offset several controllers against each other for a "green wave". |
| `Sync Reference` | none | The coordinated controller this one's `Delay` is expressed against (mirrors the OpenSCENARIO `reference`/`delay` pair). Authoring data only — see the export note below. |
| `Auto Advance` | on | Run the phase cycle automatically in game: each phase lasts its `Duration`, then the next one starts; after the last phase the cycle wraps around. |
| `Controller Id` | *(auto)* | Read-only stable identity, under **Advanced**. Used as the OpenDRIVE controller id on export; a controller pasted next to its original gets a fresh one so the two never share an identity. |

```{note}
The phase list and the linked signals are **not** editable array rows in the Details panel — they are authored
through the phase editor and the viewport, and appear nowhere else. See *Editing phases* below.
```

## In the viewport

The controller draws its signals **while the component itself is selected** — selecting only the owning actor
is not enough. If several controllers are selected on one actor, only the first of them draws (one pass per
actor). Every signal of the actor is then drawn with a pole, a round head and a guide arrow along the
controlled lane.

Colors follow the **accented** controller — the one whose component is selected, or, when the actor owns
exactly one controller, that controller (a lone controller is always accented, selected or not):

- Signals of the accented controller take the **color of their state in the previewed phase**, on a thick
  guide line.
- Signals belonging to *another* controller draw flat blue-grey on a thin line.
- Unlinked signals draw in a neutral color on a thin line.

Clicking a head selects it and shows the transform gizmo, but **dragging it does nothing** — signals are moved
along the lane in [Attribute Mode](/editing/AttributeMode.md), never here.

```{important}
While **Edit → Attribute** is the active sub-mode the controller's viewport shell disappears completely — no
drawing, no clickable heads, no context menu. That sub-mode owns the signal keys and the same click targets,
so the two never compete. Leave Attribute mode to see the controller again, or simply do the linking there:
the right-click menu is identical.
```

## Linking signals

- **Link** — right-click a signal head → **Link to \<controller\>**. Works from the controller's viewport
  visualization and from [Attribute Mode](/editing/AttributeMode.md) alike.
- **Unlink** — right-click a linked signal → **Unlink from \<controller\>**, or use the delete button on its
  row in the *Signal States* list.
- A newly linked signal starts as **Red** in every existing phase — set the phases where it should go green.
- Every Link, Unlink and Set State is its own undo step.

Links are stored by the signal's stable `SignalId`, so they survive duplication:

- **Duplicating the whole actor** — Ctrl+D, copy/paste of the `AMetaRoad`, or a Blueprint made from it —
  keeps the wiring: the copy's controllers re-point at the copy's own signals.
- **Pasting a single road spline next to its original** deliberately does not. The pasted spline's signal ids
  would collide with the originals, so they are regenerated: the **original keeps its wiring** and the copy's
  signals come back **unlinked**. Link them to a controller yourself.

![Right-clicking a signal head in the viewport and linking it to the selected controller](/img/traffic-controller-link.gif)  

## Editing phases

The controller's Details panel hosts a phase editor below the properties:

- **Phases** — **Add** appends a phase (its states are copied from the last phase, or all `Red` for the very
  first one); **Duplicate** copies the selected phase. Each row carries its index, an editable name, a
  `Duration` spin box in seconds and a delete button.
- The selected row is the **previewed** phase: every linked signal of the accented controller takes its state
  color from it in the viewport. This is editor view state only — it is not saved with the level and does not
  change where the runtime cycle starts.
- **Signal States — \<phase\>** — one row per linked signal, labelled `<spline> · Lane N · S=Xm`, with a state
  dropdown (`Off`, `Red`, `Red Yellow`, `Green`, `Yellow`) and a button that unlinks the signal. A link whose
  signal key no longer exists shows **Missing signal (stale link)** in red — unlink it, or restore the key.
  ![The Signal States list for a phase, one row per linked signal with its state dropdown and unlink button](/img/traffic-controller-phases.png)  
- States can also be set right in the viewport: right-click a linked signal → **Set State in Phase '…'**, which
  always targets the phase currently previewed in the list.
  ![The viewport right-click menu on a linked signal, setting its state in the previewed phase](/img/traffic-controller-set-color.png)  
  

```{note}
There is no phase-reordering control — author the cycle in the order you want it. Selecting several
controllers at once replaces the editor with *"Phase editing is not available for multi-selection."*
```
  
![Switching the selected phase in the list while the signal heads in the viewport change color to match](/img/traffic-controller-preview.gif)  

## Runtime

The phase clock runs **only in a game world** — Play In Editor or a packaged build. Nothing animates in the
editor viewport: the colors there are always the previewed phase, never a running cycle.

- The cycle always starts at the **first phase**, whichever phase is previewed in the editor.
- With **Auto Advance** on, each phase lasts its `Duration` and then hands over to the next; after the last
  phase the cycle wraps around.
- `Delay` delays that start — the first phase effectively lasts `Duration` + `Delay` seconds (see the property
  table). Turn **Auto Advance** off to drive the cycle entirely yourself.
- A `Duration` of 0 does not stall or spin the cycle: it is treated as effectively instantaneous and the clock
  moves on to the next phase.

From Blueprint or C++: `Set Phase (Index)`, `Advance Phase`, `Get Current Phase Index`,
`Get Signal State (SignalId)`.

The **On Phase Changed** event fires on every phase switch — and once at the start of play for the first phase
— bind it to drive your own light meshes, sounds or gameplay.

```{tip}
The data model is built for export: signals map to OpenDRIVE `<signal>` elements, the controller to a
`<controller>` plus an OpenSCENARIO `TrafficSignalController`, and phases translate to per-lane open/close
periods for AI traffic (e.g. MassTraffic). **No exporter ships with MetaRoad today** — the stable ids, the
OpenDRIVE code overrides on each signal and `Sync Reference` exist so that an exporter (yours, or a later
MetaRoad one) has everything it needs.
```

## See also

- [Signal Attribute](/attributes/SignalAttribute.md) — placing signals on lanes.
- [Attribute Mode](/editing/AttributeMode.md) — the editing sub-mode signals are authored in.
- [Junctions](/concepts/Junctions.md) — how junctions are modeled with connected splines.
