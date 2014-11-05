from django.utils.translation import ugettext_lazy as _

from dash.base import BaseDashboardPlugin
from dash.factory import plugin_factory, plugin_widget_factory

from wms.dash_widgets import ( WmsMapWidget )
from wms.forms import MapForm

# *****************************************************************************
# *************************** Base map plugin *******************************
# *****************************************************************************

class BaseMapPlugin(BaseDashboardPlugin):
    """
    Base chart plugin.
    """
    group = _("Openlayers3 plugins")
    form = MapForm
    html_classes = ['chartonic']


class BaseMapPlugin(BaseMapPlugin):
    """
    Base Map plugin.
    """
    name = _("Map Chart")
    html_classes = ['maps', 'openlayers3-map-plugin']

# *****************************************************************************
# ********** Generating and registering the plugins using factory *************
# *****************************************************************************
sizes = (
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (11, 10)
)

plugin_factory(BaseMapPlugin, 'openlayers3_map', sizes)

# *****************************************************************************
# ********************************* Registering widgets ***********************
# *****************************************************************************

# Registering map plugin widgets

# Openlayers Map
plugin_widget_factory(WmsMapWidget, 'bootstrap2_fluid', 'main', \
                      'openlayers3_map', sizes) 