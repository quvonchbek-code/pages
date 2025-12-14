from django.shortcuts import render
from django.views.generic import TemplateView
# Create your vviews here.
class HomepageView(TemplateView):
    template_name='home.html'
class AboutView(TemplateView):
    template_name='about.html'
class MainView(TemplateView):
    template_name='main.html'
class FinalView(TemplateView):
    template_name='final.html'

    