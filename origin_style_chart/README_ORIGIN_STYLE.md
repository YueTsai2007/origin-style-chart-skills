# Origin风格图表Skills

## 简介

这是一个基于Python matplotlib的专业图表样式模块，完全符合Origin软件的图表风格。专门为物理实验数据可视化设计，适用于磁场分布、磁滞回线等科学图表的绘制。

## 主要特性

### 1. 坐标轴样式
- ✅ **只显示X和Y轴**：隐藏上边框和右边框
- ✅ **加粗轴线**：默认线宽1.5
- ✅ **专业刻度**：包含主刻度和次刻度（短刻度）

### 2. 刻度系统
- **主刻度**：长度8，显示数值
- **次刻度**：长度4（主刻度的一半），不显示数值
- **自动间隔**：可根据数据范围自定义设置

### 3. 数据点样式
- **标记样式**：黑色方块（'k-s'）
- **连线样式**：黑色实线，线宽1.5
- **标记大小**：7

### 4. 图表元素
- **网格**：默认不显示
- **图例**：位于右上角
- **标签**：清晰的坐标轴标签
- **范围**：可自定义坐标轴范围

## 文件结构

```
/workspace/
├── origin_style_chart.py    # 核心模块（样式类和函数）
├── quick_plot.py            # 快速绘图脚本
├── solenoid_field.png       # 示例输出图表
└── README_ORIGIN_STYLE.md  # 说明文档（本文件）
```

## 安装依赖

```bash
pip install matplotlib numpy
```

## 快速开始

### 方法1：使用快速绘图脚本

```bash
python quick_plot.py
```

### 方法2：在Python脚本中导入

```python
from origin_style_chart import plot_origin_style

X = [-110, -105, -100, -95, -90, -85, -80]
Y = [0.00108, 0.00143, 0.00195, 0.00258, 0.00328, 0.00398, 0.00454]

fig, ax = plot_origin_style(
    X, Y,
    xlabel='X (mm)',
    ylabel='B (T)',
    xlim=(-120, 120),
    ylim=(0, 0.0065)
)

plt.savefig('output.png', dpi=300)
plt.show()
```

## 详细用法

### 1. 基本绘图函数

```python
from origin_style_chart import plot_origin_style

# 绘制单条曲线
fig, ax = plot_origin_style(
    x=[1, 2, 3, 4, 5],
    y=[10, 20, 15, 25, 30],
    xlabel='Time (s)',
    ylabel='Amplitude (mV)',
    xlim=(0, 6),
    ylim=(0, 35),
    x_major_interval=1,
    y_major_interval=5
)
```

### 2. 多条曲线绘图

```python
from origin_style_chart import plot_multiple_origin_style

data = {
    'Sample A': ([1, 2, 3], [10, 20, 30]),
    'Sample B': ([1, 2, 3], [15, 25, 35]),
    'Sample C': ([1, 2, 3], [20, 30, 40])
}

fig, ax = plot_multiple_origin_style(
    data,
    xlabel='Position (mm)',
    ylabel='Magnetic Field (T)',
    title='Multiple Samples Comparison'
)
```

### 3. 自定义配置

```python
from origin_style_chart import OriginStyleConfig, apply_origin_style_to_axes
import matplotlib.pyplot as plt

# 创建自定义配置
config = OriginStyleConfig()
config.marker_size = 9          # 更大的标记点
config.line_width = 2.0         # 更粗的线条
config.axis_linewidth = 2.0     # 更粗的坐标轴

# 创建图表
fig, ax = plt.subplots()
apply_origin_style_to_axes(ax, config)

# 绘制数据
ax.plot([1, 2, 3], [10, 20, 15], 'k-s', label='Data')

# 添加元素
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.legend()

plt.show()
```

## OriginStyleConfig 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `axis_linewidth` | 1.5 | 坐标轴线宽 |
| `major_tick_length` | 8 | 主刻度长度 |
| `minor_tick_length` | 4 | 次刻度长度 |
| `major_tick_width` | 1.0 | 主刻度宽度 |
| `minor_tick_width` | 0.8 | 次刻度宽度 |
| `marker_style` | 's' | 标记样式（方块） |
| `marker_size` | 7 | 标记大小 |
| `line_width` | 1.5 | 线条宽度 |
| `line_color` | 'black' | 线条颜色 |
| `label_fontsize` | 12 | 标签字体大小 |
| `grid_visible` | False | 是否显示网格 |

## 刻度设置

### 自动刻度
```python
# 使用默认刻度
fig, ax = plot_origin_style(X, Y)
```

### 自定义刻度间隔
```python
# 设置主刻度和次刻度间隔
fig, ax = plot_origin_style(
    X, Y,
    x_major_interval=20,    # X轴主刻度间隔
    y_major_interval=0.001, # Y轴主刻度间隔
    x_minor_interval=10,    # X轴次刻度间隔
    y_minor_interval=0.0005  # Y轴次刻度间隔
)
```

## 应用场景

### 1. 磁场分布测量
```python
# 螺线管轴线磁场分布
X_mm = [-110, -105, -100, ..., 110]
B_T = [0.00108, 0.00143, ..., 0.00099]

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
# 铁磁材料磁滞回线
H = [-100, -80, -60, ..., 100]
B = [-0.5, -0.4, -0.3, ..., 0.5]

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
# 电阻伏安特性
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

## 导出和使用

### 在其他项目中导入
```python
# 在任意Python脚本中导入
import sys
sys.path.append('/workspace')

from origin_style_chart import plot_origin_style

# 直接使用
fig, ax = plot_origin_style(x_data, y_data, xlabel='X', ylabel='Y')
```

### 作为模块安装（可选）
```bash
# 复制到Python路径
cp origin_style_chart.py ~/.local/lib/python3.x/site-packages/

# 或者添加到PYTHONPATH
export PYTHONPATH=/workspace:$PYTHONPATH
```

## 常见问题

### Q: 刻度不显示？
```python
# 确保设置了刻度间隔
fig, ax = plot_origin_style(
    X, Y,
    x_major_interval=20,
    y_major_interval=0.001
)
```

### Q: 如何修改线条颜色？
```python
# 在plot函数中指定color参数
ax.plot(X, Y, 'r-s', ...)  # 红色方块

# 或在plot_origin_style中使用color参数
fig, ax = plot_origin_style(X, Y, color='red')
```

### Q: 如何添加多个数据集？
```python
# 方法1：使用plot_multiple_origin_style
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

## 更新日志

### Version 1.0.0 (2026-05-19)
- 初始版本
- 支持Origin风格坐标轴样式
- 支持主刻度和次刻度
- 支持单条和多条曲线绘制
- 完整的配置系统
- 详细的使用文档

## 联系方式

如有问题或建议，请联系开发团队。

## 许可

本模块仅供学习和科研使用。

---

**记住**：所有新图表只需调用 `plot_origin_style()` 函数，即可自动应用Origin风格！