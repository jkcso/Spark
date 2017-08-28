from django import forms

from django.utils.translation import ugettext_lazy as _

from .models import *


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description']


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['description', 'file']



class ProblemSearchForm(forms.Form):
    query = forms.CharField(required=False, label=_('Search'),)

    def filter_queryset(self, request, queryset):
        if self.cleaned_data['query']:
            returning_set = queryset.filter(title__icontains=self.cleaned_data['query']) or \
                            queryset.filter(description__icontains=self.cleaned_data['query'])
            return returning_set
        
        return queryset

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


