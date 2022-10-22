# pylint: disable=wildcard-import,invalid-name,wrong-import-position
"""ArviZ is a library for exploratory analysis of Bayesian models."""
__version__ = "0.13.0dev1"

import logging
import os

from matplotlib.colors import LinearSegmentedColormap
from matplotlib.pyplot import style
import matplotlib as mpl


class Logger(logging.Logger):
    """Override Logger to avoid repeated messages."""

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name=name, level=level)
        self.cache = []

    def _log(
        self, level, msg, *args, **kwargs
    ):  # pylint: disable=signature-differs, arguments-differ
        msg_hash = hash(msg)
        if msg_hash in self.cache:
            return
        self.cache.append(msg_hash)
        super()._log(level, msg, *args, **kwargs)


_log = Logger("arviz")


from .data import *
from .plots import *
from .plots.backends import *
from .stats import *
from .rcparams import rc_context, rcParams
from .utils import Numba, Dask, interactive_backend
from .wrappers import *

# add ArviZ's styles to matplotlib's styles
_arviz_style_path = os.path.join(os.path.dirname(__file__), "plots", "styles")
style.core.USER_LIBRARY_PATHS.append(_arviz_style_path)
style.core.reload_library()


if not logging.root.handlers:
    _handler = logging.StreamHandler()
    _formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    _handler.setFormatter(_formatter)
    _log.setLevel(logging.INFO)
    _log.addHandler(_handler)


# adds perceptually uniform grey scale from colorcet
_linear_grey_10_95_c0 = [
    [0.10767, 0.1077, 0.1077],
    [0.11032, 0.11035, 0.11035],
    [0.11295, 0.11298, 0.11297],
    [0.11554, 0.11558, 0.11557],
    [0.1182, 0.11824, 0.11823],
    [0.12079, 0.12083, 0.12082],
    [0.12344, 0.12348, 0.12347],
    [0.12615, 0.12618, 0.12618],
    [0.12879, 0.12882, 0.12881],
    [0.13149, 0.13152, 0.13151],
    [0.13418, 0.13421, 0.1342],
    [0.13684, 0.13688, 0.13687],
    [0.13951, 0.13955, 0.13954],
    [0.14226, 0.1423, 0.14229],
    [0.14499, 0.14503, 0.14502],
    [0.1477, 0.14774, 0.14773],
    [0.15042, 0.15046, 0.15045],
    [0.15313, 0.15317, 0.15316],
    [0.15591, 0.15595, 0.15594],
    [0.15866, 0.1587, 0.15869],
    [0.16142, 0.16147, 0.16145],
    [0.16418, 0.16423, 0.16422],
    [0.16695, 0.16699, 0.16698],
    [0.16973, 0.16977, 0.16976],
    [0.17248, 0.17253, 0.17252],
    [0.17529, 0.17533, 0.17532],
    [0.17811, 0.17815, 0.17814],
    [0.18087, 0.18092, 0.1809],
    [0.18369, 0.18374, 0.18372],
    [0.18652, 0.18656, 0.18655],
    [0.18934, 0.18939, 0.18938],
    [0.19217, 0.19221, 0.1922],
    [0.19502, 0.19506, 0.19505],
    [0.19785, 0.1979, 0.19788],
    [0.20068, 0.20073, 0.20072],
    [0.20357, 0.20362, 0.20361],
    [0.20645, 0.2065, 0.20649],
    [0.20929, 0.20934, 0.20933],
    [0.21219, 0.21224, 0.21222],
    [0.21504, 0.21509, 0.21508],
    [0.21795, 0.218, 0.21799],
    [0.22086, 0.22091, 0.2209],
    [0.22374, 0.22379, 0.22377],
    [0.22666, 0.22671, 0.22669],
    [0.22954, 0.2296, 0.22958],
    [0.23248, 0.23253, 0.23252],
    [0.23542, 0.23547, 0.23546],
    [0.23832, 0.23838, 0.23836],
    [0.24127, 0.24133, 0.24131],
    [0.24419, 0.24425, 0.24424],
    [0.24716, 0.24722, 0.2472],
    [0.25009, 0.25015, 0.25014],
    [0.25308, 0.25313, 0.25312],
    [0.25603, 0.25608, 0.25607],
    [0.25902, 0.25908, 0.25906],
    [0.26198, 0.26204, 0.26203],
    [0.26496, 0.26502, 0.265],
    [0.26794, 0.268, 0.26798],
    [0.27095, 0.27101, 0.271],
    [0.27395, 0.27401, 0.274],
    [0.27695, 0.27702, 0.277],
    [0.27996, 0.28002, 0.28],
    [0.28298, 0.28304, 0.28303],
    [0.28598, 0.28604, 0.28603],
    [0.28902, 0.28909, 0.28907],
    [0.29205, 0.29212, 0.2921],
    [0.29508, 0.29514, 0.29513],
    [0.29812, 0.29818, 0.29817],
    [0.30116, 0.30123, 0.30121],
    [0.30422, 0.30429, 0.30427],
    [0.30728, 0.30734, 0.30733],
    [0.31036, 0.31043, 0.31041],
    [0.31342, 0.31349, 0.31347],
    [0.31649, 0.31656, 0.31654],
    [0.31957, 0.31964, 0.31962],
    [0.32266, 0.32273, 0.32271],
    [0.32572, 0.3258, 0.32578],
    [0.32883, 0.32891, 0.32889],
    [0.33193, 0.332, 0.33198],
    [0.33504, 0.33512, 0.3351],
    [0.33813, 0.3382, 0.33818],
    [0.34125, 0.34133, 0.34131],
    [0.34436, 0.34444, 0.34442],
    [0.3475, 0.34757, 0.34755],
    [0.35063, 0.3507, 0.35068],
    [0.35374, 0.35382, 0.3538],
    [0.35689, 0.35697, 0.35695],
    [0.36002, 0.3601, 0.36008],
    [0.36317, 0.36325, 0.36323],
    [0.36633, 0.36641, 0.36639],
    [0.36948, 0.36956, 0.36954],
    [0.37263, 0.37272, 0.3727],
    [0.3758, 0.37589, 0.37587],
    [0.37897, 0.37906, 0.37904],
    [0.38214, 0.38223, 0.38221],
    [0.38532, 0.3854, 0.38538],
    [0.38852, 0.3886, 0.38858],
    [0.3917, 0.39179, 0.39177],
    [0.39489, 0.39498, 0.39496],
    [0.3981, 0.39818, 0.39816],
    [0.4013, 0.40138, 0.40136],
    [0.40449, 0.40458, 0.40456],
    [0.40771, 0.4078, 0.40778],
    [0.41093, 0.41102, 0.411],
    [0.41415, 0.41423, 0.41421],
    [0.41738, 0.41747, 0.41744],
    [0.4206, 0.42068, 0.42066],
    [0.42383, 0.42392, 0.4239],
    [0.42708, 0.42717, 0.42715],
    [0.43031, 0.43041, 0.43038],
    [0.43355, 0.43364, 0.43362],
    [0.43681, 0.43691, 0.43688],
    [0.44007, 0.44016, 0.44014],
    [0.44333, 0.44342, 0.4434],
    [0.44659, 0.44668, 0.44666],
    [0.44986, 0.44995, 0.44993],
    [0.45313, 0.45322, 0.4532],
    [0.4564, 0.4565, 0.45647],
    [0.45968, 0.45978, 0.45976],
    [0.46296, 0.46306, 0.46303],
    [0.46625, 0.46635, 0.46633],
    [0.46956, 0.46966, 0.46963],
    [0.47284, 0.47294, 0.47292],
    [0.47615, 0.47625, 0.47623],
    [0.47946, 0.47956, 0.47953],
    [0.48276, 0.48286, 0.48284],
    [0.48607, 0.48618, 0.48615],
    [0.48939, 0.48949, 0.48947],
    [0.49271, 0.49281, 0.49279],
    [0.49603, 0.49614, 0.49611],
    [0.49936, 0.49947, 0.49944],
    [0.5027, 0.5028, 0.50278],
    [0.50603, 0.50614, 0.50612],
    [0.50938, 0.50949, 0.50946],
    [0.51273, 0.51284, 0.51281],
    [0.51607, 0.51618, 0.51615],
    [0.51943, 0.51954, 0.51951],
    [0.52279, 0.5229, 0.52287],
    [0.52615, 0.52626, 0.52624],
    [0.52952, 0.52963, 0.5296],
    [0.53289, 0.533, 0.53297],
    [0.53626, 0.53637, 0.53634],
    [0.53963, 0.53974, 0.53971],
    [0.54302, 0.54313, 0.5431],
    [0.54641, 0.54652, 0.54649],
    [0.54979, 0.5499, 0.54987],
    [0.55317, 0.55329, 0.55326],
    [0.55657, 0.55669, 0.55666],
    [0.55998, 0.56009, 0.56007],
    [0.56338, 0.5635, 0.56347],
    [0.56679, 0.56691, 0.56688],
    [0.57019, 0.57031, 0.57028],
    [0.57361, 0.57373, 0.5737],
    [0.57703, 0.57715, 0.57712],
    [0.58045, 0.58057, 0.58054],
    [0.58387, 0.58399, 0.58396],
    [0.5873, 0.58742, 0.58739],
    [0.59073, 0.59086, 0.59083],
    [0.59417, 0.5943, 0.59427],
    [0.59761, 0.59774, 0.59771],
    [0.60106, 0.60118, 0.60115],
    [0.60451, 0.60463, 0.6046],
    [0.60796, 0.60809, 0.60806],
    [0.61141, 0.61154, 0.61151],
    [0.61486, 0.61499, 0.61496],
    [0.61833, 0.61846, 0.61843],
    [0.62179, 0.62192, 0.62189],
    [0.62527, 0.62539, 0.62536],
    [0.62874, 0.62887, 0.62884],
    [0.63222, 0.63235, 0.63231],
    [0.63569, 0.63583, 0.63579],
    [0.63918, 0.63931, 0.63928],
    [0.64267, 0.6428, 0.64276],
    [0.64615, 0.64629, 0.64625],
    [0.64965, 0.64978, 0.64975],
    [0.65314, 0.65327, 0.65324],
    [0.65665, 0.65678, 0.65675],
    [0.66015, 0.66028, 0.66025],
    [0.66366, 0.6638, 0.66376],
    [0.66717, 0.6673, 0.66727],
    [0.67069, 0.67082, 0.67079],
    [0.6742, 0.67434, 0.6743],
    [0.67772, 0.67786, 0.67783],
    [0.68124, 0.68138, 0.68134],
    [0.68477, 0.68491, 0.68488],
    [0.68831, 0.68845, 0.68841],
    [0.69184, 0.69198, 0.69195],
    [0.69538, 0.69552, 0.69548],
    [0.69891, 0.69906, 0.69902],
    [0.70246, 0.7026, 0.70257],
    [0.70601, 0.70616, 0.70612],
    [0.70956, 0.70971, 0.70967],
    [0.71311, 0.71326, 0.71322],
    [0.71668, 0.71682, 0.71679],
    [0.72023, 0.72038, 0.72034],
    [0.7238, 0.72394, 0.72391],
    [0.72736, 0.72751, 0.72748],
    [0.73093, 0.73108, 0.73105],
    [0.73451, 0.73466, 0.73463],
    [0.73808, 0.73823, 0.7382],
    [0.74167, 0.74182, 0.74178],
    [0.74525, 0.7454, 0.74536],
    [0.74884, 0.74899, 0.74895],
    [0.75243, 0.75258, 0.75254],
    [0.75602, 0.75618, 0.75614],
    [0.75961, 0.75977, 0.75973],
    [0.76322, 0.76337, 0.76333],
    [0.76682, 0.76697, 0.76694],
    [0.77043, 0.77058, 0.77055],
    [0.77403, 0.77419, 0.77415],
    [0.77765, 0.77781, 0.77777],
    [0.78126, 0.78142, 0.78138],
    [0.78489, 0.78504, 0.785],
    [0.78851, 0.78867, 0.78863],
    [0.79213, 0.79229, 0.79225],
    [0.79576, 0.79592, 0.79588],
    [0.79939, 0.79955, 0.79951],
    [0.80302, 0.80318, 0.80314],
    [0.80666, 0.80683, 0.80679],
    [0.8103, 0.81046, 0.81042],
    [0.81394, 0.81411, 0.81406],
    [0.81759, 0.81775, 0.81771],
    [0.82124, 0.82141, 0.82136],
    [0.82489, 0.82506, 0.82501],
    [0.82855, 0.82872, 0.82867],
    [0.83221, 0.83237, 0.83233],
    [0.83587, 0.83604, 0.83599],
    [0.83953, 0.8397, 0.83966],
    [0.8432, 0.84337, 0.84333],
    [0.84687, 0.84704, 0.847],
    [0.85054, 0.85071, 0.85067],
    [0.85422, 0.85439, 0.85435],
    [0.8579, 0.85807, 0.85803],
    [0.86158, 0.86176, 0.86171],
    [0.86527, 0.86544, 0.8654],
    [0.86896, 0.86913, 0.86909],
    [0.87265, 0.87282, 0.87278],
    [0.87634, 0.87652, 0.87647],
    [0.88004, 0.88022, 0.88017],
    [0.88374, 0.88392, 0.88388],
    [0.88744, 0.88762, 0.88758],
    [0.89115, 0.89133, 0.89128],
    [0.89486, 0.89504, 0.895],
    [0.89857, 0.89875, 0.89871],
    [0.90229, 0.90247, 0.90242],
    [0.90601, 0.90619, 0.90614],
    [0.90972, 0.90991, 0.90986],
    [0.91345, 0.91363, 0.91359],
    [0.91718, 0.91736, 0.91732],
    [0.9209, 0.92108, 0.92104],
    [0.92463, 0.92482, 0.92477],
    [0.92837, 0.92855, 0.92851],
    [0.9321, 0.93229, 0.93224],
    [0.93585, 0.93604, 0.93599],
    [0.93959, 0.93978, 0.93973],
    [0.94334, 0.94353, 0.94348],
]


def _mpl_cm(name, colorlist):
    cmap = LinearSegmentedColormap.from_list(name, colorlist, N=256)
    mpl.colormaps.register(cmap, name="cet_" + name)


try:
    import colorcet
except ModuleNotFoundError:
    _mpl_cm("gray", _linear_grey_10_95_c0)
    _mpl_cm("gray_r", list(reversed(_linear_grey_10_95_c0)))


# clean namespace
del os, logging, LinearSegmentedColormap, Logger, mpl
