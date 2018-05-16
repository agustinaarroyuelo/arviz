import matplotlib.pyplot as plt
import numpy as np
from .plot_utils import _scale_text


<<<<<<< HEAD
def khatplot(ks, figsize=None, textsize=None, ax=None, hlines_kwargs=None, **kwargs):
    R"""
    Plot Paretto tail indices.

    Parameters
    ----------
    ks : array
      Paretto tail indices.
=======
def khatplot(khats, figsize=None, textsize=None, ax=None, hlines_kwargs=None, **kwargs):
    R"""
    Plot Pareto tail indices.

    Parameters
    ----------
    khats : array
      Pareto tail indices.
>>>>>>> b63a01f72b06f4166c128ee2d543b89eed2c9b00
    figsize : figure size tuple
      If None, size is (8, 4)
    textsize: int
      Text size for labels. If None it will be autoscaled based on figsize.
    ax: axes
      Matplotlib axes
    hlines_kwargs: dictionary
<<<<<<< HEAD
      Aditional keywords passed to ax.hlines
=======
      Additional keywords passed to ax.hlines
    kwargs :
      Additional keywords passed to ax.scatter
>>>>>>> b63a01f72b06f4166c128ee2d543b89eed2c9b00

    Returns
    -------
    ax : axes
      Matplotlib axes.
    """

    if figsize is None:
        figsize = (8, 5)

    if hlines_kwargs is None:
        hlines_kwargs = {}

<<<<<<< HEAD
    textsize, linewidth, ms = _scale_text(figsize, textsize=textsize)
=======
    textsize, linewidth, markersize = _scale_text(figsize, textsize=textsize)
>>>>>>> b63a01f72b06f4166c128ee2d543b89eed2c9b00

    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=figsize)

<<<<<<< HEAD
    ax.hlines([0, .5, .7, 1], xmin=-1, xmax=len(ks)+1,
              alpha=.25, **hlines_kwargs)

    alphas = .5 + .5*(ks > .5)
    rgba_c = np.zeros((len(ks), 4))
    rgba_c[:, 2] = .8
    rgba_c[:, 3] = alphas
    ax.scatter(np.arange(len(ks)), ks, c=rgba_c, marker='+', linewidth=ms)
=======
    ax.hlines([0, .5, .7, 1], xmin=-1, xmax=len(khats)+1,
              alpha=.25, linewidth=linewidth, **hlines_kwargs)

    alphas = .5 + .5*(khats > .5)
    rgba_c = np.zeros((len(khats), 4))
    rgba_c[:, 2] = .8
    rgba_c[:, 3] = alphas
    ax.scatter(np.arange(len(khats)), khats, c=rgba_c, marker='+', markersize=markersize, **kwargs)
>>>>>>> b63a01f72b06f4166c128ee2d543b89eed2c9b00
    ax.set_xlabel('Data point', fontsize=textsize)
    ax.set_ylabel(r'Shape parameter κ', fontsize=textsize)
    ax.tick_params(labelsize=textsize)
    return ax
