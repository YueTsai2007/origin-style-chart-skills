# Origin Style Chart

Matplotlib charts styled like OriginLab — designed for scientific/engineering data visualization.

## Features

- **Origin-style axes**: only left and bottom spines, inward ticks
- **Dual tick system**: major ticks with labels, minor ticks without
- **Single & multi-curve** plotting with one function call
- **Fully configurable**: marker style, line width, tick length, font size, colors

## Installation

```bash
pip install -e .
```

Requires Python 3.9+ with `matplotlib` and `numpy`.

## Quick start

```python
from origin_style_chart import plot_origin_style

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

fig, ax = plot_origin_style(
    x, y,
    xlabel="Time (s)",
    ylabel="Amplitude (mV)",
    xlim=(0, 6),
    ylim=(0, 35),
)
fig.savefig("chart.png", dpi=300)
```

