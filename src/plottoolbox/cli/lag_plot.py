"""Collection of functions for the manipulation of time series."""

import warnings

import cltoolbox
import matplotlib
from cltoolbox.rst_text_formatter import RSTHelpFormatter
from toolbox_utils import tsutils

from .. import _plotutils
from .._functions.lag_plot import lag_plot

matplotlib.use("Agg")

warnings.filterwarnings("ignore")


@cltoolbox.command("lag_plot", formatter_class=RSTHelpFormatter)
@tsutils.doc(_plotutils.ldocstrings)
def lag_plot_cli(
    input_ts="-",
    columns=None,
    start_date=None,
    end_date=None,
    clean=False,
    skiprows=None,
    index_type="datetime",
    names=None,
    ofilename="plot.png",
    xtitle="",
    ytitle="",
    title="",
    figsize="10,6.0",
    legend=None,
    legend_names=None,
    colors="auto",
    linestyles="auto",
    markerstyles=" ",
    style="auto",
    grid=False,
    por=False,
    invert_xaxis=False,
    invert_yaxis=False,
    round_index=None,
    source_units=None,
    target_units=None,
    lag_plot_lag=1,
    plot_styles="bright",
    hlines_y=None,
    hlines_xmin=None,
    hlines_xmax=None,
    hlines_colors=None,
    hlines_linestyles="-",
    vlines_x=None,
    vlines_ymin=None,
    vlines_ymax=None,
    vlines_colors=None,
    vlines_linestyles="-",
):
    r"""Lag plot.

    "lag_plot" indicates structure in the data.

    ${yone}

    Parameters
    ----------
    ${input_ts}

    ${columns}

    ${start_date}

    ${end_date}

    ${clean}

    ${skiprows}

    ${index_type}

    ${names}

    ${ofilename}

    ${xtitle}

    ${ytitle}

    ${title}

    ${figsize}

    ${legend}

    ${legend_names}

    ${colors}

    ${linestyles}

    ${markerstyles}

    ${style}

    ${grid}

    ${por}

    ${invert_xaxis}

    ${invert_yaxis}

    ${round_index}

    ${source_units}

    ${target_units}

    lag_plot_lag : int
        Defaults to 1.

        The lag used in the plot.

    ${plot_styles}

    ${hlines_y}

    ${hlines_xmin}

    ${hlines_xmax}

    ${hlines_colors}

    ${hlines_linestyles}

    ${vlines_x}

    ${vlines_ymin}

    ${vlines_ymax}

    ${vlines_colors}

    ${vlines_linestyles}
    """
    lag_plot(
        input_ts=input_ts,
        columns=columns,
        start_date=start_date,
        end_date=end_date,
        clean=clean,
        skiprows=skiprows,
        index_type=index_type,
        names=names,
        ofilename=ofilename,
        xtitle=xtitle,
        ytitle=ytitle,
        title=title,
        figsize=figsize,
        legend=legend,
        legend_names=legend_names,
        colors=colors,
        linestyles=linestyles,
        markerstyles=markerstyles,
        style=style,
        grid=grid,
        por=por,
        invert_xaxis=invert_xaxis,
        invert_yaxis=invert_yaxis,
        round_index=round_index,
        source_units=source_units,
        target_units=target_units,
        lag_plot_lag=lag_plot_lag,
        plot_styles=plot_styles,
        hlines_y=hlines_y,
        hlines_xmin=hlines_xmin,
        hlines_xmax=hlines_xmax,
        hlines_colors=hlines_colors,
        hlines_linestyles=hlines_linestyles,
        vlines_x=vlines_x,
        vlines_ymin=vlines_ymin,
        vlines_ymax=vlines_ymax,
        vlines_colors=vlines_colors,
        vlines_linestyles=vlines_linestyles,
    )


lag_plot_cli.__doc__ = lag_plot.__doc__
