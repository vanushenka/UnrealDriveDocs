# Speed Attribute

A stepped attribute that stores a **speed limit** (`MaxSpeed`) along a lane. It is authored metadata you read at
runtime — carry per-section speed for your own traffic, analytics, or AI systems.

```{note}
`Speed` is essentially the **simplest possible attribute** — a single stepped value along the lane, with no generated
geometry. It's a good reference for what a minimal attribute type looks like when you
[build your own](/concepts/Attributes.md#extending-attributes).
```

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `MaxSpeed` | 15 | The speed limit stored at this key. It is not consumed by the plugin — the unit is yours to interpret. |

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
