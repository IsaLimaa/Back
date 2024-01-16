from django.shortcuts import render
from django.views.generic import TemplateView
# Create you view here
class Index(TemplateView):
    template_name = 'index.html'