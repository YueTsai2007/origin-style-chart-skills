---
name: origin-style-chart
description: Generate OriginLab-style scientific charts using matplotlib — axis styling, tick configuration, single/multi-curve plotting, and publication-ready exports. 基于 matplotlib 的专业 Origin 风格科学图表绘制工具。
trigger: origin style chart, Origin风格图表, scientific plotting, matplotlib Origin style, 科学图表绘制, origin_style_chart, 实验数据可视化, 物理实验图表, 磁场分布, 磁滞回线, 伏安特性曲线
requirements:
  - matplotlib>=3.5
  - numpy>=1.20
---

# Origin Style Chart Skill

基于 Python matplotlib 的专业图表样式模块，完全符合 Origin 软件的图表风格。专门为物理实验数据可视化设计，适用于磁场分布、磁滞回线等科学图表的绘制。

## 工作流程

> **核心原则：严格遵循模板，仅修改输入数据，不更改模板结构和样式参数。**
> 除非有明确的定制要求，否则只替换数据和标签，保持其他所有设置不变。

### 推荐一：极简模板（90% 场景）

```bash
# 1. 复制模板
cp examples/simple_plot.py my_plot.py

# 2. 仅修改数据区和设置区
#    编辑 my_plot.py 中的 x_data、y_data、x_label、y_label

# 3. 运行
python my_plot.py
```

### 推荐二：通用模板（复杂需求）

```bash
cp examples/quick_plot_template.py my_chart.py
# 编辑 PlotConfig 类中的配置和数据
python my_chart.py
```

### 推荐三：导入模块（完全定制）

```python
from origin_style_chart import plot_origin_style

X = [1, 2, 3, 4, 5]
Y = [10, 20, 15, 25, 30]

fig, ax = plot_origin_style(X, Y, xlabel='X', ylabel='Y')
fig.savefig('chart.png', dpi=300)
```

---

## 主要特性

### 1. 坐标轴样式
- **只显示 X 和 Y 轴**：隐藏上边框和右边框
- **加粗轴线**：默认线宽 1.5
- **专业刻度**：包含主刻度和次刻度（短刻度），刻度向外显示

### 2. 刻度系统
- **主刻度**：长度 8，显示数值
- **次刻度**：长度 4（主刻度的一半），不显示数值
- **自动间隔**：可根据数据范围自定义设置

### 3. 数据点样式
- **标记样式**：黑色方块（`'s'`）
- **连线样式**：黑色实线，线宽 1.5
- **标记大小**：7

### 4. 图表元素
- **网格**：默认不显示
- **图例**：位于右上角
- **标签**：清晰的坐标轴标签
- **范围**：可自定义坐标轴范围

---

## Installation

```bash
# From the project root (requires Python 3.9+)
pip install -e .
```

---

## Usage

### Single curve

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

### Multiple curves

```python
from origin_style_chart import plot_multiple_origin_style

data = {
    "Sample A": ([1, 2, 3], [10, 20, 30]),
    "Sample B": ([1, 2, 3], [15, 25, 35]),
}

fig, ax = plot_multiple_origin_style(
    data,
    xlabel="Position (mm)",
    ylabel="Magnetic Field (T)",
)
```

### 自定义刻度间隔

```python
fig, ax = plot_origin_style(
    X, Y,
    x_major_interval=20,     # X轴主刻度间隔
    y_major_interval=0.001,  # Y轴主刻度间隔
    x_minor_interval=10,     # X轴次刻度间隔
    y_minor_interval=0.0005, # Y轴次刻度间隔
)
```

### Custom configuration

```python
from origin_style_chart import OriginStyleConfig, apply_origin_style_to_axes
import matplotlib.pyplot as plt

config = OriginStyleConfig()
config.marker_size = 9
config.line_width = 2.0
config.axis_linewidth = 2.0

fig, ax = plt.subplots()
apply_origin_style_to_axes(ax, config)
ax.plot([1, 2, 3], [10, 20, 15], "k-s", label="Data")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.legend()
plt.show()
```

---

## OriginStyleConfig 参数说明

| 参数 | 默认值 | 说明 |
|---|---|---|
| `axis_linewidth` | 1.5 | 坐标轴线宽 |
| `major_tick_length` | 8 | 主刻度长度 |
| `minor_tick_length` | 4 | 次刻度长度（主刻度的一半） |
| `major_tick_width` | 1.0 | 主刻度宽度 |
| `minor_tick_width` | 0.8 | 次刻度宽度 |
| `marker_style` | 's' | 标记样式（方块） |
| `marker_size` | 7 | 标记大小 |
| `line_width` | 0.75 | 线条宽度 |
| `line_color` | 'black' | 线条颜色 |
| `label_fontsize` | 12 | 标签字体大小 |
| `grid_visible` | False | 是否显示网格 |

---

## 应用场景

### 1. 磁场分布测量

```python
X_mm = [-110, -105, -100, -95, -90, -85, -80, -75, -70, -65, -60, -55, -50,
        -45, -40, -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30,
        35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]
B_T = [0.00108, 0.00143, 0.00195, 0.00258, 0.00328, 0.00398, 0.00454, 0.00494,
       0.00522, 0.00542, 0.00556, 0.00568, 0.00575, 0.00582, 0.00586, 0.00592,
       0.00593, 0.00595, 0.00595, 0.00596, 0.00596, 0.00597, 0.00598, 0.00598,
       0.00598, 0.00598, 0.00598, 0.00596, 0.00595, 0.00593, 0.00587, 0.00582,
       0.00575, 0.00568, 0.00556, 0.00539, 0.00516, 0.00483, 0.00439, 0.00382,
       0.00311, 0.00242, 0.00179, 0.00133, 0.00099]

fig, ax = plot_origin_style(
    X_mm, B_T,
    xlabel='X (mm)',
    ylabel='B (T)',
    xlim=(-120, 120),
    ylim=(0, 0.0065),
    x_major_interval=20,
    y_major_interval=0.001,
    x_minor_interval=10,
    y_minor_interval=0.0005
)
```

### 2. 磁滞回线

```python
H = [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100]
B = [-0.50, -0.48, -0.40, -0.25, -0.10, 0.05, 0.20, 0.35, 0.45, 0.49, 0.50]

fig, ax = plot_origin_style(
    H, B,
    xlabel='H (A/m)',
    ylabel='B (T)',
    xlim=(-120, 120),
    ylim=(-0.6, 0.6),
    x_major_interval=20,
    y_major_interval=0.1,
    x_minor_interval=10,
    y_minor_interval=0.05
)
```

### 3. 伏安特性曲线

```python
V = [0, 1, 2, 3, 4, 5]
I = [0, 0.02, 0.04, 0.06, 0.08, 0.10]

fig, ax = plot_origin_style(
    V, I,
    xlabel='Voltage (V)',
    ylabel='Current (A)',
    xlim=(-0.5, 5.5),
    ylim=(0, 0.12),
    x_major_interval=1,
    y_major_interval=0.02,
    x_minor_interval=0.5,
    y_minor_interval=0.01
)
```

---

## 快速修改对照表

| 参数 | simple_plot.py | quick_plot_template.py | 说明 |
|---|---|---|---|
| 数据 | `x_data`, `y_data` | `SINGLE_CURVE_DATA` | 仅修改这里 |
| X 标签 | `x_label` | `X_LABEL` | X 轴标签 |
| Y 标签 | `y_label` | `Y_LABEL` | Y 轴标签 |
| X 范围 | `x_lim` | `X_LIMIT` | 坐标轴范围 |
| Y 范围 | `y_lim` | `Y_LIMIT` | 坐标轴范围 |
| 主刻度间隔 | `x_major_tick` | `X_MAJOR_INTERVAL` | 主刻度间距 |
| 主刻度间隔 | `y_major_tick` | `Y_MAJOR_INTERVAL` | 主刻度间距 |
| 次刻度间隔 | `x_minor_tick` | `X_MINOR_INTERVAL` | 次刻度间距 |
| 次刻度间隔 | `y_minor_tick` | `Y_MINOR_INTERVAL` | 次刻度间距 |
| 输出文件名 | `output_file` | `OUTPUT_FILENAME` | 文件名（不含扩展名） |
| 输出格式 | `formats` | `OUTPUT_FORMATS` | 输出格式列表 |
| 分辨率 | `dpi` | `DPI` | 300 或更高 |

### simple_plot.py 修改位置

```python
# 1. 数据区 — 仅改这里
x_data = [1, 2, 3]    # ← 改这里
y_data = [10, 20, 30]  # ← 改这里

# 2. 设置区
x_label = "X轴标签"    # ← 改这里
y_label = "Y轴标签"    # ← 改这里
```

### quick_plot_template.py 修改位置

```python
# 1. 数据区域 (DATA SECTION)
SINGLE_CURVE_DATA = {
    "x": [...],   # ← 改这里
    "y": [...],   # ← 改这里
}

# 2. 配置区域 (CONFIG SECTION)
class PlotConfig:
    DATASET = "single"  # 或 "multiple", "hysteresis", "generated"
    X_LABEL = "..."     # ← 改这里
    Y_LABEL = "..."     # ← 改这里
```

---

## 内置数据集（quick_plot_template.py）

| 选项 | 说明 |
|---|---|
| `DATASET = "single"` | 单条曲线（螺线管磁场数据） |
| `DATASET = "multiple"` | 三条对比曲线 |
| `DATASET = "hysteresis"` | 磁滞回线（上下分支） |
| `DATASET = "generated"` | 自动生成 sin/cos 数据 |

---

## API Reference

| Function / Class | Description |
|---|---|
| `plot_origin_style(x, y, ...)` | Single curve with full Origin styling |
| `plot_multiple_origin_style(data, ...)` | Multiple curves on shared axes |
| `apply_origin_style_to_axes(ax, config)` | Apply Origin styling to existing axes |
| `setup_origin_style()` | Create default config |
| `save_figure(fig, filename, formats, dpi)` | Export in multiple formats |
| `OriginStyleConfig` | Dataclass for all style knobs |

---

## 常见问题

### Q: 刻度不显示？
确保设置了刻度间隔：
```python
fig, ax = plot_origin_style(
    X, Y,
    x_major_interval=20,
    y_major_interval=0.001
)
```

### Q: 如何修改线条颜色？
```python
# 在 plot_origin_style 中使用 color 参数
fig, ax = plot_origin_style(X, Y, color='red')
```

### Q: 如何添加多个数据集？
```python
# 方法1：使用 plot_multiple_origin_style
data = {
    'Dataset 1': (x1, y1),
    'Dataset 2': (x2, y2)
}
fig, ax = plot_multiple_origin_style(data, xlabel='X', ylabel='Y')

# 方法2：手动添加
fig, ax = plot_origin_style(x1, y1, xlabel='X', ylabel='Y')
ax.plot(x2, y2, 'r-s', label='Dataset 2')
ax.legend()
```

---

## Examples

Pre-built templates in `examples/` — copy and modify:

```bash
# Quick start — minimal template (only change data + labels)
cp examples/simple_plot.py my_plot.py
python my_plot.py

# Full-featured — single/multi/hysteresis/generated datasets
cp examples/quick_plot_template.py my_chart.py
python my_chart.py
```

---

## Trigger phrases

- "绘制 Origin 风格图表", "Origin 风格", "科学图表"
- "scientific plot with Origin style", "matplotlib Origin-like chart"
- "实验数据可视化", "物理实验图表", "磁场分布", "磁滞回线", "伏安特性曲线"
- "publication-ready matplotlib chart"
