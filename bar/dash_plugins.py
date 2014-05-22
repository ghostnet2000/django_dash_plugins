from django.utils.translation import ugettext_lazy as _
from dash.base import plugin_registry, plugin_widget_registry, BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory
from dash.contrib.plugins.image.dash_plugins import BaseImagePlugin
from bar.dash_widgets import BaseChartWidget
from bar.forms import ChartForm

class BaseChartPlugin(BaseDashboardPlugin):
    """
    Base chart plugin.
    """
    name = _("chart")
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

plugin_factory(BaseChartPlugin, 'chart', sizes)


plugin_widget_factory(BaseChartWidget, 'android', 'main', 'chart', sizes)
plugin_widget_factory(BaseChartWidget, 'windows8', 'main', 'chart', sizes)
plugin_widget_factory(BaseChartWidget, 'bootstrap2_fluid', 'main', 'chart', sizes)






