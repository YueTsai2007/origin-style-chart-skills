"""
Origin-style chart core module.

Provides configuration and plotting functions to create matplotlib charts
in the style of OriginLab software, designed for scientific data visualization.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator


# ===========================================================================
# Configuration
# ===========================================================================

@dataclass
class OriginStyleConfig:
    """Configuration class for Origin-style chart appearance.

    All visual parameters are centralized here for easy customization.
    """
    # Axis
    axis_linewidth: float = 1.5

    # Ticks
    major_tick_length: float = 8.0
    minor_tick_length: float = 4.0
    major_tick_width: float = 1.0
    minor_tick_width: float = 0.8

    # Data markers and lines
    marker_style: str = "s"
    marker_size: float = 7.0
    line_width: float = 0.75
    line_color: str = "black"

    # Labels
    label_fontsize: float = 12.0

    # Grid
    grid_visible: bool = False


# ===========================================================================
# Axis styling
# ===========================================================================

def apply_origin_style_to_axes(
    ax: plt.Axes, config: Optional[OriginStyleConfig] = None
) -> None:
    """Apply Origin-style appearance to a matplotlib Axes object.

    This is the core styling function. It configures spines, ticks,
    and other visual elements to match OriginLab's default style.

    Args:
        ax: A matplotlib Axes instance to style.
        config: An OriginStyleConfig instance. Uses defaults if None.
    """
    if config is None:
        config = OriginStyleConfig()

    # --- Spines: show only left and bottom ---
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for spine_name in ("bottom", "left"):
        ax.spines[spine_name].set_linewidth(config.axis_linewidth)

    # --- Tick direction: outward ---
    ax.tick_params(direction="out")

    # --- Major ticks ---
    ax.tick_params(
        which="major",
        length=config.major_tick_length,
        width=config.major_tick_width,
        labelsize=config.label_fontsize - 2,
    )

    # --- Minor ticks ---
    ax.tick_params(
        which="minor",
        length=config.minor_tick_length,
        width=config.minor_tick_width,
    )

    # Enable minor ticks by default
    if not hasattr(ax.xaxis, "minor_locator") or ax.xaxis.get_minor_locator().__class__.__name__ == "NullLocator":
        ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    if not hasattr(ax.yaxis, "minor_locator") or ax.yaxis.get_minor_locator().__class__.__name__ == "NullLocator":
        ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    # --- Grid ---
    ax.grid(config.grid_visible)


def setup_origin_style() -> OriginStyleConfig:
    """Create and return a default OriginStyleConfig.

    Convenience factory for the common case where the default parameters
    are sufficient.

    Returns:
        A new OriginStyleConfig with default values.
    """
    return OriginStyleConfig()


# ===========================================================================
# Single-curve plot
# ===========================================================================

def plot_origin_style(
    x: List[float],
    y: List[float],
    xlabel: str = "",
    ylabel: str = "",
    title: Optional[str] = None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    x_major_interval: Optional[float] = None,
    y_major_interval: Optional[float] = None,
    x_minor_interval: Optional[float] = None,
    y_minor_interval: Optional[float] = None,
    config: Optional[OriginStyleConfig] = None,
    label: str = "",
    color: Optional[str] = None,
    marker: Optional[str] = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """Plot a single curve with full Origin-style formatting.

    A convenience function that creates a figure, applies Origin styling,
    plots the data, and configures labels, limits, and tick intervals.

    Args:
        x: X-axis data points.
        y: Y-axis data points.
        xlabel: Label for the X axis.
        ylabel: Label for the Y axis.
        title: Optional chart title.
        xlim: (min, max) for X axis. Auto-scaled if None.
        ylim: (min, max) for Y axis. Auto-scaled if None.
        x_major_interval: Spacing between major X ticks. Auto if None.
        y_major_interval: Spacing between major Y ticks. Auto if None.
        x_minor_interval: Spacing between minor X ticks. Auto if None.
        y_minor_interval: Spacing between minor Y ticks. Auto if None.
        config: Style configuration. Uses defaults if None.
        label: Legend label for the curve.
        color: Line and marker color. Overrides config.line_color if set.
        marker: Marker style string. Overrides config.marker_style if set.

    Returns:
        A tuple of (Figure, Axes) for further customization.
    """
    if config is None:
        config = OriginStyleConfig()

    fig, ax = plt.subplots()

    # Apply Origin style
    apply_origin_style_to_axes(ax, config)

    # Build format string or use color/marker directly
    effective_color = color if color is not None else config.line_color
    effective_marker = marker if marker is not None else config.marker_style

    ax.plot(
        x, y,
        color=effective_color,
        marker=effective_marker,
        markersize=config.marker_size,
        linewidth=config.line_width,
        markerfacecolor=effective_color,
        markeredgecolor=effective_color,
        label=label if label else None,
    )

    # Labels
    ax.set_xlabel(xlabel, fontsize=config.label_fontsize)
    ax.set_ylabel(ylabel, fontsize=config.label_fontsize)
    if title:
        ax.set_title(title, fontsize=config.label_fontsize + 2)

    # Limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Major tick intervals
    if x_major_interval is not None:
        ax.xaxis.set_major_locator(MultipleLocator(x_major_interval))
    if y_major_interval is not None:
        ax.yaxis.set_major_locator(MultipleLocator(y_major_interval))

    # Minor tick intervals
    if x_minor_interval is not None:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_interval))
    if y_minor_interval is not None:
        ax.yaxis.set_minor_locator(MultipleLocator(y_minor_interval))

    # Legend (Origin-style: bordered frame, upper right)
    if label:
        ax.legend(
            loc="upper right",
            fontsize=config.label_fontsize - 1,
            frameon=True,
            fancybox=False,
            edgecolor="black",
        )

    fig.tight_layout()
    return fig, ax


# ===========================================================================
# Multi-curve plot
# ===========================================================================

def plot_multiple_origin_style(
    data: Dict[str, Tuple[List[float], List[float]]],
    xlabel: str = "",
    ylabel: str = "",
    title: Optional[str] = None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    x_major_interval: Optional[float] = None,
    y_major_interval: Optional[float] = None,
    x_minor_interval: Optional[float] = None,
    y_minor_interval: Optional[float] = None,
    config: Optional[OriginStyleConfig] = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """Plot multiple curves on the same axes with Origin-style formatting.

    Each entry in *data* becomes a separate curve. A default color cycle
    is applied so that curves are visually distinct.

    Args:
        data: Mapping of ``{label: (x_values, y_values)}``.
        xlabel: Label for the X axis.
        ylabel: Label for the Y axis.
        title: Optional chart title.
        xlim: (min, max) for X axis.
        ylim: (min, max) for Y axis.
        x_major_interval: Spacing between major X ticks.
        y_major_interval: Spacing between major Y ticks.
        x_minor_interval: Spacing between minor X ticks.
        y_minor_interval: Spacing between minor Y ticks.
        config: Style configuration.

    Returns:
        A tuple of (Figure, Axes).
    """
    if config is None:
        config = OriginStyleConfig()

    fig, ax = plt.subplots()

    # Apply Origin style
    apply_origin_style_to_axes(ax, config)

    # Color cycle for multiple curves
    color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for idx, (label, (x_vals, y_vals)) in enumerate(data.items()):
        color = color_cycle[idx % len(color_cycle)]
        marker = config.marker_style if idx == 0 else "o"

        ax.plot(
            x_vals, y_vals,
            color=color,
            marker=marker,
            markersize=config.marker_size,
            linewidth=config.line_width,
            markerfacecolor=color,
            markeredgecolor=color,
            label=label,
        )

    # Labels
    ax.set_xlabel(xlabel, fontsize=config.label_fontsize)
    ax.set_ylabel(ylabel, fontsize=config.label_fontsize)
    if title:
        ax.set_title(title, fontsize=config.label_fontsize + 2)

    # Limits
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # Tick intervals
    if x_major_interval is not None:
        ax.xaxis.set_major_locator(MultipleLocator(x_major_interval))
    if y_major_interval is not None:
        ax.yaxis.set_major_locator(MultipleLocator(y_major_interval))
    if x_minor_interval is not None:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_interval))
    if y_minor_interval is not None:
        ax.yaxis.set_minor_locator(MultipleLocator(y_minor_interval))

    ax.legend(
        loc="upper right",
        fontsize=config.label_fontsize - 1,
        frameon=True,
        fancybox=False,
        edgecolor="black",
    )
    fig.tight_layout()
    return fig, ax


# ===========================================================================
# Save helper
# ===========================================================================

def save_figure(
    fig: plt.Figure,
    filename: str,
    formats: Union[str, List[str]] = "png",
    dpi: int = 300,
    bbox_inches: str = "tight",
) -> List[str]:
    """Save a figure in one or more formats.

    Args:
        fig: The matplotlib Figure to save.
        filename: Output path without extension (e.g. ``"output"``).
        formats: A single format string or a list of format strings
            (``"png"``, ``"pdf"``, ``"svg"``, ``"eps"``).
        dpi: Resolution in dots per inch.
        bbox_inches: Bounding box setting passed to ``fig.savefig``.

    Returns:
        List of saved file paths.
    """
    if isinstance(formats, str):
        formats = [formats]

    saved = []
    for fmt in formats:
        path = f"{filename}.{fmt}"
        fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches)
        saved.append(path)

    return saved
