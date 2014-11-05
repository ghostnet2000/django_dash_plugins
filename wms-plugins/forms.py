from django import forms
from django.utils.translation import ugettext_lazy as _ 
from dash.base import DashboardPluginFormBase

class MapForm(forms.Form, DashboardPluginFormBase):
	""" Chart Form """

	plugin_data_fields = [
		("title", ""),
	]

	title = forms.CharField(label=("Title"), required=True)

