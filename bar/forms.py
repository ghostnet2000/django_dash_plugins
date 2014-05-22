from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase

#from bar.defaults               import DEFAULT_DATE_VALUE, DEFAULT_OPEN_VALUE

class ChartForm(forms.Form, DashboardPluginFormBase):
    """
    Chart form for `ChartBasePlugin` plugin.
    """

    plugin_data_fields = [
        ("title", "")
    ]

    title = forms.CharField(label=_("Title"), required=True)


