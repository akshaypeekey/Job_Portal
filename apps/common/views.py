from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView(TemplateView):
    template_name = 'common/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')


class CompanyAddView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'common/company_add.html'
    success_url = reverse_lazy('dashboard')


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    template_name = 'common/company_add.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Company, company_id=id)


class CompanyView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'common/company_view.html'


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'common/company_details.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        print(id)
        return get_object_or_404(Company, company_id=id)