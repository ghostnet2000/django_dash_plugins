from django.utils.translation import ugettext_lazy as _
from dash.base import plugin_registry, plugin_widget_registry, BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash.contrib.plugins.image.dash_plugins import BaseImagePlugin
from qux.plugins.line.dash_widgets import LineChartWidget
from qux.plugins.line.forms import ChartForm

class BaseChartPlugin(BaseDashboardPlugin):
    """
    Base chart plugin.
    """
    name = _("line_chart")
    group = _("charts")
    form = ChartForm
    html_classes = ['chartonic']


sizes = (
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 3),
    (4, 4),
    (4, 5),
    (5, 4),
    (5, 5)
)

plugin_factory(BaseChartPlugin, 'bar_chart', sizes)


plugin_widget_factory(LineChartWidget, 'android', 'main', 'line_chart', sizes)
plugin_widget_factory(LineChartWidget, 'windows8', 'main', 'line_chart', sizes)
plugin_widget_factory(LineChartWidget, 'bootstrap2_fluid', 'main', 'line_chart', sizes)

