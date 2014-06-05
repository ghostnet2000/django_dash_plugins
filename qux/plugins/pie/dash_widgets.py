from django.template.loader import render_to_string
from django.conf import settings
from dash.base import BaseDashboardPluginWidget


class PieChartWidget(BaseDashboardPluginWidget):
    """
    Base chart widget.
    """
    media_js = (
        'js/polychart2.standalone.js',
    )

    def render(self, request=None):
        context = {
            'plugin': self.plugin,
            'MEDIA_URL': settings.MEDIA_URL,
            'category': str(self.plugin.data.category),
            'number': str(self.plugin.data.number),
            'width': self.get_width(),
            'height': self.get_height(),
        }
        return render_to_string('pie/plugins/render_graph.html', context)