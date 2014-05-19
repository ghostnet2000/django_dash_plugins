from django.utils.translation                   import ugettext_lazy as _

from dash.base                                  import plugin_registry, plugin_widget_registry, BaseDashboardPlugin
from dash.factory                               import plugin_factory, plugin_widget_factory
from dash.contrib.plugins.image.dash_plugins    import BaseImagePlugin

from map.dash_widgets   import BaseOpenLayersWidget
from map.forms          import OpenLayersForm



class BaseOpenLayersPlugin(BaseDashboardPlugin):
    """
    Base OpenLayers plugin.
    """
    name = _("openlayers")
    group = _("internet")
    form = MapForm
    html_classes = ['mapping']

#  Generating and registering the plugins using factory 

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

plugin_factory(BaseOpenLayersPlugin, 'OpenLayers', sizes)

plugin_widget_factory(BaseOpenLayersWidget, 'android', 'main', 'OpenLayers', sizes)


