from django.template.loader   import render_to_string
from django.conf              import settings

from dash.base                import BaseDashboardPluginWidget


class BaseChartWidget(BaseDashboardPluginWidget):
    """
    Base chart widget.
    """
    media_js = (
        'static/js/d3.js',
    )

    media_css = (
        'static/css/style.css',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'MEDIA_URL': settings.MEDIA_URL,
            #'data_date': str(self.plugin.data.data_date),
            #'data_open': str(self.plugin.data.data_open),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('bar/plugins/render_graph.html', context)