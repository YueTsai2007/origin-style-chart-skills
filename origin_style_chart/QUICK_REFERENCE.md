# Origin风格图表 - 快速参考指南

## 📁 文件清单

| 文件名 | 说明 | 使用场景 |
|--------|------|----------|
| [origin_style_chart.py](file:///workspace/origin_style_chart.py) | 核心模块库 | 需要灵活定制时导入使用 |
| [quick_plot_template.py](file:///workspace/quick_plot_template.py) | 通用完整模板 | 需要高级功能时使用 |
| [simple_plot.py](file:///workspace/simple_plot.py) | 极简模板 | 快速绘制基本图表 |
| [README_ORIGIN_STYLE.md](file:///workspace/README_ORIGIN_STYLE.md) | 详细文档 | 学习API使用 |
| [quick_plot.py](file:///workspace/quick_plot.py) | 原始快速脚本 | 保留参考 |

---

## 🚀 推荐使用流程

### 📌 推荐一：极简模板（大多数情况）

**使用 `simple_plot.py`

```bash
# 1. 复制一个副本
cp simple_plot.py my_plot.py

# 2. 修改数据和设置
vim my_plot.py  # 或用编辑器打开

# 3. 运行
python my_plot.py
```

**优点：**
- ✅ 最简单
- ✅ 只有2个区域修改
- ✅ 直接看到效果

---

### 📌 推荐二：通用模板（复杂需求）

**使用 `quick_plot_template.py`

```bash
cp quick_plot_template.py my_chart.py
vim my_chart.py
python my_chart.py
```

**优点：**
- ✅ 支持单条/多条曲线
- ✅ 内置多个示例数据
- ✅ 完整配置类统一管理
- ✅ 支持多种输出

---

### 📌 推荐三：导入模块库（完全定制）

**在您的项目中导入**

```python
from origin_style_chart import plot_origin_style

X = [1, 2, 3, 4, 5]
Y = [10, 20, 15, 25, 30]

fig, ax = plot_origin_style(X, Y, xlabel='X', ylabel='Y')
plt.savefig('chart.png', dpi=300)
```

---

## 📝 快速修改对照

### `simple_plot.py` 修改位置

```python
# 1. 数据区
x_data = [1, 2, 3]  # ← 改这里
y_data = [10, 20, 30]  # ← 改这里

# 2. 设置区
x_label = "X轴标签"  # ← 改这里
y_label = "Y轴标签"  # ← 改这里
```

### `quick_plot_template.py` 修改位置

```python
# 1. 数据区域 (DATA SECTION)
SINGLE_CURVE_DATA = {
    "x": [...],  # ← 改这里
    "y": [...],  # ← 改这里
}

# 2. 配置区域 (CONFIG SECTION)
class PlotConfig:
    DATASET = "single"  # 或 "multiple", "hysteresis"
    X_LABEL = "..."  # ← 改这里
    Y_LABEL = "..."  # ← 改这里
```

---

## 📊 内置示例数据

### 示例1：单条曲线
```python
DATASET = "single"
```

### 示例2：多条曲线
```python
DATASET = "multiple"
```

### 示例3：磁滞回线
```python
DATASET = "hysteresis"
```

### 示例4：生成数据
```python
DATASET = "generated"
```

---

## 🔧 常见修改配置对照表

| 参数 | simple_plot | quick_plot_template | 说明 |
|------|------------|---------------------|------|
| 数据 | x_data, y_data | SINGLE_CURVE_DATA | 您的数据 |
| X标签 | x_label | X_LABEL | X轴标签 |
| Y标签 | y_label | Y_LABEL | Y轴标签 |
| X范围 | x_lim | X_LIMIT | 坐标轴范围 |
| Y范围 | y_lim | Y_LIMIT | 坐标轴范围 |
| 主刻度间隔 | x_major_tick | X_MAJOR_INTERVAL | 主刻度 |
| 主刻度间隔 | y_major_tick | Y_MAJOR_INTERVAL | 主刻度 |
| 次刻度间隔 | x_minor_tick | X_MINOR_INTERVAL | 次刻度 |
| 次刻度间隔 | y_minor_tick | Y_MINOR_INTERVAL | 次刻度 |
| 输出文件名 | output_file | OUTPUT_FILENAME | 文件名 |
| 输出格式 | formats | OUTPUT_FORMATS | 输出格式列表 |
| 分辨率 | dpi | DPI | 300或更高 |

---

## ⚡ 快速开始（30秒上手

1. **创建新脚本
```bash
# 复制极简版
cp simple_plot.py my_chart.py
python my_chart.py
```

2. **修改**
```python
# 用编辑器打开 my_chart.py
# 修改 x_data, y_data, x_label, y_label
```

3. **运行**
```bash
python my_chart.py
```

---

## 📚 更多文档

- 完整的使用方法请参考：
1. [README_ORIGIN_STYLE.md - 完整文档
2. origin_style_chart.py - 模块源代码
3. quick_plot_template.py - 通用模板

---

## 💡 小提示

- 建议始终从 `simple_plot.py` 开始，足够90%场景都能满足！

```bash
# 复制这个文件
cp simple_plot.py 你的图表名称.py

# 修改数据和标签
# 运行
python 你的图表名称.py
```