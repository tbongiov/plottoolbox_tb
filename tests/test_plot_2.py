import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pytest
from toolbox_utils import tsutils

from plottoolbox import plottoolbox

# Pull this in once.
idf = tsutils.common_kwds(input_tsd="tests/02234500_65_65.csv", clean=True)

df = idf.resample("D").agg("mean")

ndfa = idf.resample("A").agg("mean")

dfa = pd.DataFrame()
dfa["Elevation::mean"] = ndfa.iloc[:, 0] * 120
dfa["Flow::mean"] = ndfa.iloc[:, 1]


@pytest.mark.mpl_image_compare(tolerance=6)
def test_double_mass():
    plt.close("all")
    return plottoolbox.double_mass(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_double_mass_mult():
    plt.close("all")
    return plottoolbox.double_mass(
        columns=[2, 3, 3, 2],
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_double_mass_marker():
    plt.close("all")
    return plottoolbox.double_mass(
        columns=[2, 3, 3, 2],
        linestyles=" ",
        markerstyles="auto",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_boxplot():
    plt.close("all")
    xdf = pd.read_csv("tests/02234500_65_65.csv", index_col=0, parse_dates=True)
    xdf = xdf.join(
        pd.read_csv("tests/data_02325000_flow.csv", index_col=0, parse_dates=True),
        how="outer",
    )
    return plottoolbox.boxplot(
        input_ts=xdf,
        clean=True,
        columns=[2, 3],
        ofilename=None,
        plot_styles="classic",
    )


# @pytest.mark.mpl_image_compare(tolerance=6)
# def test_scatter_matrix():
#     plt.close("all")
#     return plottoolbox.scatter_matrix(
#         clean=True,
#         input_ts="tests/02234500_65_65.csv",
#         ofilename=None,
#         plot_styles="classic",
#     )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_lag_plot():
    plt.close("all")
    return plottoolbox.lag_plot(
        columns=1, input_ts=df, ofilename=None, plot_styles="classic"
    )


# Can't have a bootstrap test since random selections are made.
# @image_comparison(baseline_images=['bootstrap'],
#                   tol=0.019, extensions=['png'])
# def test_bootstrap():
#     return plottoolbox.plot(type='bootstrap',
#                    clean=True,
#                    columns=2,
#                    input_ts='tests/02234500_65_65.csv')


@pytest.mark.mpl_image_compare(tolerance=6)
def test_probability_density():
    plt.close("all")
    return plottoolbox.probability_density(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_bar():
    plt.close("all")
    return plottoolbox.bar(input_ts=dfa, plot_styles="classic", ofilename=None)


@pytest.mark.mpl_image_compare(tolerance=6)
def test_barh():
    plt.close("all")
    return plottoolbox.barh(input_ts=dfa, plot_styles="classic", ofilename=None)


@pytest.mark.mpl_image_compare(tolerance=6)
def test_bar_stacked():
    plt.close("all")
    return plottoolbox.bar_stacked(input_ts=dfa, plot_styles="classic", ofilename=None)


@pytest.mark.mpl_image_compare(tolerance=6)
def test_barh_stacked():
    plt.close("all")
    return plottoolbox.barh_stacked(input_ts=dfa, plot_styles="classic", ofilename=None)
