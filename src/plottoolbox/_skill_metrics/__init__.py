__version__ = "1.2.1"

from .add_legend import add_legend
from .bias import bias
from .brier_score import brier_score
from .centered_rms_dev import centered_rms_dev
from .check_duplicate_stats import check_duplicate_stats
from .check_on_off import check_on_off
from .check_taylor_stats import check_taylor_stats
from .error_check_stats import error_check_stats
from .get_from_dict_or_default import get_from_dict_or_default
from .get_target_diagram_axes import get_target_diagram_axes
from .get_target_diagram_options import get_target_diagram_options
from .get_taylor_diagram_axes import get_taylor_diagram_axes
from .get_taylor_diagram_options import get_taylor_diagram_options
from .kling_gupta_eff09 import kling_gupta_eff09
from .kling_gupta_eff12 import kling_gupta_eff12
from .nash_sutcliffe_eff import nash_sutcliffe_eff
from .overlay_target_diagram_circles import overlay_target_diagram_circles
from .overlay_taylor_diagram_circles import overlay_taylor_diagram_circles
from .overlay_taylor_diagram_lines import overlay_taylor_diagram_lines
from .plot_pattern_diagram_colorbar import plot_pattern_diagram_colorbar
from .plot_pattern_diagram_markers import plot_pattern_diagram_markers
from .plot_target_axes import plot_target_axes
from .plot_taylor_axes import plot_taylor_axes
from .plot_taylor_obs import plot_taylor_obs
from .report_duplicate_stats import report_duplicate_stats
from .rmsd import rmsd
from .save_figures import save_figures
from .skill_score_brier import skill_score_brier
from .skill_score_murphy import skill_score_murphy
from .target_diagram import target_diagram
from .target_statistics import target_statistics
from .taylor_diagram import taylor_diagram
from .taylor_statistics import taylor_statistics
from .write_stats import write_stats
from .write_target_stats import write_target_stats
from .write_taylor_stats import write_taylor_stats