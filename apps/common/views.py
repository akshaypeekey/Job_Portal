from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('index')


class CompanyAddView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'common/recruiter/company_add.html'
    success_url = reverse_lazy('view_company')


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'common/recruiter/company_add.html'
    success_url = reverse_lazy('view_company')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Company, company_id=id)


class CompanyView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'common/recruiter/company_view.html'


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'common/recruiter/company_details.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Company, company_id=id)


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'common/recruiter/job_add.html'
    success_url = reverse_lazy('view_job')


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'common/recruiter/job_add.html'
    success_url = reverse_lazy('view_job')

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Job, job_id=id)


class JobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'common/recruiter/job_view.html'


class JobDetails(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'common/recruiter/job_details.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Job, job_id=id)


class CandidateJobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'common/candidate/job_view.html'


class CandidateJobDetails(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'common/candidate/job_details.html'
    context_object_name = "details"

    def get_object(self):
        id = self.kwargs.get("id")
        print(id)
        return get_object_or_404(Job, job_id=id)


class PreApplyView(LoginRequiredMixin, TemplateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'common/candidate/job_apply.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Job, job_id=id)

    def get(self,request, *args, **kwargs):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_job')
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)

class AppliedJobs(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'common/candidate/applied_jobs.html'
