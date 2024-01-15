from django.views.generic import TemplateView, DetailView
from resume.models import *

class HomePage(TemplateView):
    template_name="index.html"

class PortfolioPage(TemplateView):
    model = portfolioModels
    context_object_name = "portfolio"
    template_name = "portfolio.html"



    