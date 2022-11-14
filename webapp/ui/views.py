from django.views.generic.base import TemplateView
from django.contrib.auth import models as auth_models


class HomeView(TemplateView):
    template_name = 'base.html'
