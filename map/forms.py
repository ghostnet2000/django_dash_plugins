from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase
from map.defaults import DEFAULT_URL_VALUE

class MapForm(forms.Form, DashboardPluginFormBase):
    """
     Map form for `OpenLayersPlugin` plugin.
    """

    plugin_data_fields = [
        ("title", ""),
        ("data_url", DEFAULT_URL_VALUE),
    ]

    title = forms.CharField(label=_("Title"), required=True)
    data_date = forms.CharField(label=_("Url"), required=True, initial=DEFAULT_URL_VALUE,
                                widget=forms.widgets.Textarea)
