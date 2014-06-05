from django.utils.translation import ugettext_lazy as _
from dash.base import plugin_registry, plugin_widget_registry, BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash.contrib.plugins.image.dash_plugins import BaseImagePlugin
from qux.plugins.pie.dash_widgets import PieChartWidget
from qux.plugins.pie.forms import ChartForm

class BaseChartPlugin(BaseDashboardPlugin):
    """
    Base chart plugin.
    """
    name = _("pie_chart")
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

plugin_factory(BaseChartPlugin, 'pie_chart', sizes)


plugin_widget_factory(PieChartWidget, 'android', 'main', 'pie_chart', sizes)
plugin_widget_factory(PieChartWidget, 'windows8', 'main', 'pie_chart', sizes)
plugin_widget_factory(PieChartWidget, 'bootstrap2_fluid', 'main', 'pie_chart', sizes)

