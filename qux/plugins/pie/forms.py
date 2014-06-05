from django import forms
from django.utils.translation import ugettext_lazy as _
from dash.base import DashboardPluginFormBase

from qux.plugins.pie.defaults import CATEGORY, NUMBER

class ChartForm(forms.Form, DashboardPluginFormBase):
    """
Chart form for `ChartBasePlugin` plugin.
"""

    plugin_data_fields = [
        ("title", ""),
        ("category", CATEGORY),
        ("number", NUMBER)
    ]

    title = forms.CharField(label=_("Title"), required=True)
    data_date = forms.CharField(label=_("Category"), required=True, initial=CATEGORY,
                                widget=forms.widgets.Textarea)
    data_open = forms.CharField(label=_("Numbers"), required=True, initial=NUMBER,
                                widget=forms.widgets.Textarea)