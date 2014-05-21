from django.template.loader   import render_to_string
from django.shortcuts import render_to_response
from django.conf              import settings

from dash.base                import BaseDashboardPluginWidget


class BaseOpenLayersWidget(BaseDashboardPluginWidget):
    """
    Base OpenLayers widget.
    """
    media_js = (
        'js/OpenLayers.js',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'MEDIA_URL': settings.MEDIA_URL,
            'data_url': str(self.plugin.data.data_url),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('map/plugins/render.html', context)