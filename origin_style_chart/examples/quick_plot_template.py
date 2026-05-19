"""
================================================================================
Origin风格通用快速绘图模板 - Quick Plot Template
================================================================================

本模板适用于：
- 任意实验数据可视化
- 单条曲线、多条曲线
- 多种刻度配置
- 多种输出格式

================================================================================
快速使用指南
================================================================================

1. 修改数据区域（DATA SECTION）
2. 修改配置区域（CONFIG SECTION）
3. 运行脚本：python quick_plot_template.py

================================================================================
"""

# ===================== 0. 导入必要的库 (IMPORT SECTION) =====================
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional, List, Tuple, Union
from origin_style_chart import (
    plot_origin_style,
    plot_multiple_origin_style,
    OriginStyleConfig,
    setup_origin_style,
    save_figure
)

# ============================================================================
# ===================== 1. 数据区域 (DATA SECTION) ===========================
# ============================================================================

# ----------------------------------------------------------------------------
# 示例A：单条曲线数据
# ----------------------------------------------------------------------------
SINGLE_CURVE_DATA = {
    "x": [-110, -105, -100, -95, -90, -85, -80, -75, -70, -65, -60, -55, -50, -45, -40,
          -35, -30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
          55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110],
    "y": [0.00108, 0.00143, 0.00195, 0.00258, 0.00328, 0.00398, 0.00454, 0.00494, 0.00522, 0.00542,
          0.00556, 0.00568, 0.00575, 0.00582, 0.00586, 0.00592, 0.00593, 0.00595, 0.00595, 0.00596,
          0.00596, 0.00597, 0.00598, 0.00598, 0.00598, 0.00598, 0.00598, 0.00596, 0.00595, 0.00593,
          0.00587, 0.00582, 0.00575, 0.00568, 0.00556, 0.00539, 0.00516, 0.00483, 0.00439, 0.00382,
          0.00311, 0.00242, 0.00179, 0.00133, 0.00099],
    "label": "Magnetic Field Distribution"
}

# ----------------------------------------------------------------------------
# 示例B：多条曲线数据
# ----------------------------------------------------------------------------
MULTIPLE_CURVES_DATA = {
    "Sample 1": (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
    ),
    "Sample 2": (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0],
    ),
    "Sample 3": (
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    ),
}

# ----------------------------------------------------------------------------
# 示例C：磁滞回线数据
# ----------------------------------------------------------------------------
HYSTERESIS_DATA = {
    "Upper Branch": (
        [-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100],
        [-0.50, -0.48, -0.40, -0.25, -0.10, 0.05, 0.20, 0.35, 0.45, 0.49, 0.50],
    ),
    "Lower Branch": (
        [100, 80, 60, 40, 20, 0, -20, -40, -60, -80, -100],
        [0.50, 0.48, 0.40, 0.25, 0.10, -0.05, -0.20, -0.35, -0.45, -0.49, -0.50],
    ),
}

# ----------------------------------------------------------------------------
# 示例D：从NumPy数组或计算生成数据
# ----------------------------------------------------------------------------
def generate_sample_data():
    """生成示例数据的函数"""
    x = np.linspace(0, 2 * np.pi, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    return x, y1, y2


# ============================================================================
# ===================== 2. 配置区域 (CONFIG SECTION) =========================
# ============================================================================

class PlotConfig:
    """绘图配置类 - 在此修改配置参数"""
    
    # ---------------------- 基本设置 (BASIC SETTINGS) ----------------------
    
    # 选择要使用的数据集
    # 选项: "single", "multiple", "hysteresis", "generated"
    DATASET = "single"
    
    # 图表标题
    TITLE = ""  # 空字符串表示不显示标题
    
    # 坐标轴标签
    X_LABEL = "X (mm)"
    Y_LABEL = "B (T)"
    
    # 曲线标签（仅用于单条曲线）
    CURVE_LABEL = "B (T)"
    
    # ---------------------- 坐标轴范围 (AXIS RANGES) ------------------------
    
    # X轴范围 (最小值, 最大值)
    X_LIMIT = (-120, 120)
    
    # Y轴范围 (最小值, 最大值)
    Y_LIMIT = (0, 0.0065)
    
    # ---------------------- 刻度间隔 (TICKS) --------------------------------
    
    # X轴主刻度间隔 (None表示自动)
    X_MAJOR_INTERVAL = 20
    
    # X轴次刻度间隔 (None表示自动，为主刻度的一半)
    X_MINOR_INTERVAL = 10
    
    # Y轴主刻度间隔
    Y_MAJOR_INTERVAL = 0.001
    
    # Y轴次刻度间隔
    Y_MINOR_INTERVAL = 0.0005
    
    # ---------------------- 输出设置 (OUTPUT) --------------------------------
    
    # 输出文件名（不含扩展名）
    OUTPUT_FILENAME = "output"
    
    # 输出格式: "png", "pdf", "svg", "eps"
    OUTPUT_FORMATS = ["png", "pdf"]
    
    # 分辨率（DPI）
    DPI = 300
    
    # 显示图表在屏幕上（True/False）
    SHOW_PLOT = False
    
    # ---------------------- 样式设置 (STYLE) ---------------------------------
    
    # 标记大小
    MARKER_SIZE = 7
    
    # 线条宽度
    LINE_WIDTH = 1.5
    
    # 坐标轴宽度
    AXIS_WIDTH = 1.5
    
    # 主刻度长度
    MAJOR_TICK_LENGTH = 8
    
    # 次刻度长度
    MINOR_TICK_LENGTH = 4
    
    # 字体大小
    FONT_SIZE = 12


# ============================================================================
# ===================== 3. 绘图函数 (PLOTTING FUNCTIONS) =====================
# ============================================================================

def plot_single_curve(config: PlotConfig):
    """绘制单条曲线"""
    print("\n绘制单条曲线...")
    
    # 设置样式
    style_config = setup_origin_style()
    style_config.marker_size = config.MARKER_SIZE
    style_config.line_width = config.LINE_WIDTH
    style_config.axis_linewidth = config.AXIS_WIDTH
    style_config.major_tick_length = config.MAJOR_TICK_LENGTH
    style_config.minor_tick_length = config.MINOR_TICK_LENGTH
    style_config.label_fontsize = config.FONT_SIZE
    
    # 获取数据
    x = SINGLE_CURVE_DATA["x"]
    y = SINGLE_CURVE_DATA["y"]
    label = config.CURVE_LABEL
    
    # 绘制图表
    fig, ax = plot_origin_style(
        x, y,
        xlabel=config.X_LABEL,
        ylabel=config.Y_LABEL,
        title=config.TITLE if config.TITLE else None,
        xlim=config.X_LIMIT,
        ylim=config.Y_LIMIT,
        x_major_interval=config.X_MAJOR_INTERVAL,
        y_major_interval=config.Y_MAJOR_INTERVAL,
        x_minor_interval=config.X_MINOR_INTERVAL,
        y_minor_interval=config.Y_MINOR_INTERVAL,
        config=style_config,
        label=label
    )
    
    return fig, ax


def plot_multiple_curves(config: PlotConfig):
    """绘制多条曲线"""
    print("\n绘制多条曲线...")
    
    # 设置样式
    style_config = setup_origin_style()
    style_config.marker_size = config.MARKER_SIZE
    style_config.line_width = config.LINE_WIDTH
    style_config.axis_linewidth = config.AXIS_WIDTH
    style_config.major_tick_length = config.MAJOR_TICK_LENGTH
    style_config.minor_tick_length = config.MINOR_TICK_LENGTH
    style_config.label_fontsize = config.FONT_SIZE
    
    # 绘制图表
    fig, ax = plot_multiple_origin_style(
        MULTIPLE_CURVES_DATA,
        xlabel=config.X_LABEL,
        ylabel=config.Y_LABEL,
        title=config.TITLE if config.TITLE else None,
        xlim=config.X_LIMIT,
        ylim=config.Y_LIMIT,
        config=style_config
    )
    
    # 设置刻度
    if config.X_MAJOR_INTERVAL:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(config.X_MAJOR_INTERVAL))
    if config.Y_MAJOR_INTERVAL:
        ax.yaxis.set_major_locator(MultipleLocator(config.Y_MAJOR_INTERVAL))
    if config.X_MINOR_INTERVAL:
        ax.xaxis.set_minor_locator(MultipleLocator(config.X_MINOR_INTERVAL))
    if config.Y_MINOR_INTERVAL:
        ax.yaxis.set_minor_locator(MultipleLocator(config.Y_MINOR_INTERVAL))
    
    return fig, ax


def plot_hysteresis(config: PlotConfig):
    """绘制磁滞回线"""
    print("\n绘制磁滞回线...")
    
    # 设置样式
    style_config = setup_origin_style()
    style_config.marker_size = config.MARKER_SIZE
    style_config.line_width = config.LINE_WIDTH
    style_config.axis_linewidth = config.AXIS_WIDTH
    style_config.major_tick_length = config.MAJOR_TICK_LENGTH
    style_config.minor_tick_length = config.MINOR_TICK_LENGTH
    style_config.label_fontsize = config.FONT_SIZE
    
    # 绘制图表
    fig, ax = plot_multiple_origin_style(
        HYSTERESIS_DATA,
        xlabel=config.X_LABEL,
        ylabel=config.Y_LABEL,
        title=config.TITLE if config.TITLE else None,
        xlim=config.X_LIMIT,
        ylim=config.Y_LIMIT,
        config=style_config
    )
    
    # 设置刻度
    if config.X_MAJOR_INTERVAL:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(config.X_MAJOR_INTERVAL))
    if config.Y_MAJOR_INTERVAL:
        ax.yaxis.set_major_locator(MultipleLocator(config.Y_MAJOR_INTERVAL))
    if config.X_MINOR_INTERVAL:
        ax.xaxis.set_minor_locator(MultipleLocator(config.X_MINOR_INTERVAL))
    if config.Y_MINOR_INTERVAL:
        ax.yaxis.set_minor_locator(MultipleLocator(config.Y_MINOR_INTERVAL))
    
    return fig, ax


def plot_generated_data(config: PlotConfig):
    """绘制生成的数据"""
    print("\n绘制生成的数据...")
    
    # 设置样式
    style_config = setup_origin_style()
    style_config.marker_size = config.MARKER_SIZE
    style_config.line_width = config.LINE_WIDTH
    style_config.axis_linewidth = config.AXIS_WIDTH
    style_config.major_tick_length = config.MAJOR_TICK_LENGTH
    style_config.minor_tick_length = config.MINOR_TICK_LENGTH
    style_config.label_fontsize = config.FONT_SIZE
    
    # 生成数据
    x, y1, y2 = generate_sample_data()
    
    data_dict = {
        "sin(x)": (x, y1),
        "cos(x)": (x, y2),
    }
    
    # 绘制图表
    fig, ax = plot_multiple_origin_style(
        data_dict,
        xlabel=config.X_LABEL,
        ylabel=config.Y_LABEL,
        title=config.TITLE if config.TITLE else None,
        xlim=config.X_LIMIT,
        ylim=config.Y_LIMIT,
        config=style_config
    )
    
    # 设置刻度
    if config.X_MAJOR_INTERVAL:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_major_locator(MultipleLocator(config.X_MAJOR_INTERVAL))
    if config.Y_MAJOR_INTERVAL:
        ax.yaxis.set_major_locator(MultipleLocator(config.Y_MAJOR_INTERVAL))
    if config.X_MINOR_INTERVAL:
        ax.xaxis.set_minor_locator(MultipleLocator(config.X_MINOR_INTERVAL))
    if config.Y_MINOR_INTERVAL:
        ax.yaxis.set_minor_locator(MultipleLocator(config.Y_MINOR_INTERVAL))
    
    return fig, ax


def save_chart(fig, config: PlotConfig):
    """保存图表"""
    plt.tight_layout()
    
    for fmt in config.OUTPUT_FORMATS:
        filename = f"{config.OUTPUT_FILENAME}.{fmt}"
        fig.savefig(filename, dpi=config.DPI, bbox_inches='tight')
        print(f"✓ 已保存: {filename}")


# ============================================================================
# ===================== 4. 主程序 (MAIN PROGRAM) =============================
# ============================================================================

def main():
    """主函数"""
    print("=" * 60)
    print("Origin风格 - 通用快速绘图模板")
    print("=" * 60)
    
    # 加载配置
    config = PlotConfig()
    
    # 根据选择的数据集绘图
    if config.DATASET == "single":
        fig, ax = plot_single_curve(config)
    elif config.DATASET == "multiple":
        fig, ax = plot_multiple_curves(config)
    elif config.DATASET == "hysteresis":
        fig, ax = plot_hysteresis(config)
    elif config.DATASET == "generated":
        fig, ax = plot_generated_data(config)
    else:
        raise ValueError(f"未知的数据集类型: {config.DATASET}")
    
    # 保存图表
    save_chart(fig, config)
    
    # 显示图表
    if config.SHOW_PLOT:
        plt.show()
    else:
        plt.close()
    
    print("\n" + "=" * 60)
    print("绘图完成！")
    print("=" * 60)
    
    # 打印提示信息
    print(f"\n📌 提示:")
    print(f"   1. 修改 PlotConfig 类中的配置参数")
    print(f"   2. 更换数据区域中的数据")
    print(f"   3. 运行脚本重新生成图表\n")


if __name__ == "__main__":
    main()


# ============================================================================
# ===================== 5. 快速参考 (QUICK REFERENCE) ========================
# ============================================================================

"""
----------------------------------------------------------------------------
快速修改说明
----------------------------------------------------------------------------

▶ 更换数据：
  - 修改 SINGLE_CURVE_DATA 或 MULTIPLE_CURVES_DATA
  - 或设置 DATASET = "multiple" 等

▶ 调整坐标轴：
  - X_LIMIT, Y_LIMIT: 调整范围
  - X_MAJOR_INTERVAL, Y_MAJOR_INTERVAL: 主刻度间隔
  - X_MINOR_INTERVAL, Y_MINOR_INTERVAL: 次刻度间隔

▶ 修改标签：
  - X_LABEL, Y_LABEL: 坐标轴标签
  - TITLE: 图表标题（可选）

▶ 调整样式：
  - MARKER_SIZE: 标记大小
  - LINE_WIDTH: 线条宽度
  - AXIS_WIDTH: 坐标轴宽度
  - FONT_SIZE: 字体大小

▶ 输出设置：
  - OUTPUT_FILENAME: 输出文件名
  - OUTPUT_FORMATS: 输出格式
  - DPI: 分辨率
  - SHOW_PLOT: 是否显示在屏幕上

----------------------------------------------------------------------------
常见数据集模板
----------------------------------------------------------------------------

# 数据格式1：单条曲线
SINGLE_CURVE_DATA = {
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 15, 25, 30],
    "label": "Curve Label"
}

# 数据格式2：多条曲线
MULTIPLE_CURVES_DATA = {
    "Name 1": (x_list1, y_list1),
    "Name 2": (x_list2, y_list2),
}

----------------------------------------------------------------------------
"""