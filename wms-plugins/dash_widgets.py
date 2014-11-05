from django.template.loader import render_to_string
from django.conf import settings

from dash.base import BaseDashboardPluginWidget

class BaseMapWidget(BaseDashboardPluginWidget):
	"""Base map widget"""
	_template = None

	def render(self, request=None):
		context = {
			'plugin': self.plugin,
			'width' : self.get_width(),
			'height': self.get_height(), 
		}

		return render_to_string( 
			self._template, 
			context
		)

class WmsMapWidget(BaseMapWidget):
	""" Map widget"""
	media_js = (
		'js/ol.js',
	)

	media_css = (
		#specific media css here
	)

	_template = 'wms/plugins/render_map.html'