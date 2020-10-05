from django.forms import ModelForm
from .models import *
from django import forms


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_place', 'company_industry', 'company_job_positions']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_place': forms.TextInput(attrs={'class': 'form-control'}),
            'company_industry': forms.Select(attrs={'class': 'form-control'}),
            'company_job_positions': forms.TextInput(attrs={'class': 'form-control'})
        }

        def clean(self):
            pass


class CompanyUpdateForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_place', 'company_industry', 'company_job_positions']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_place': forms.TextInput(attrs={'class': 'form-control'}),
            'company_industry': forms.Select(attrs={'class': 'form-control'}),
            'company_job_positions': forms.TextInput(attrs={'class': 'form-control'})
        }

        def clean(self):
            pass


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['job_company', 'job_place', 'job_type', 'job_title', 'job_category', 'job_skills', 'job_description',
                  'job_vacancy', 'job_experience', 'job_salary', 'job_offer_end', 'job_status']
        widgets = {
            'job_company': forms.TextInput(attrs={'class': 'form-control'}),
            'job_place': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'job_category': forms.Select(attrs={'class': 'form-control'}),
            'job_skills': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description': forms.TextInput(attrs={'class': 'form-control'}),
            'job_vacancy': forms.TextInput(attrs={'class': 'form-control'}),
            'job_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'job_salary': forms.TextInput(attrs={'class': 'form-control'}),
            'job_offer_end': forms.TextInput(attrs={'class': 'form-control'}),
            'job_status': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean(self):
            pass


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['company_id', 'job_id', 'user', 'application_status']
        widgets = {
            'company_id': forms.TextInput(attrs={'class': 'form-control'}),
            'job_id': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'application_status': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            pass


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ['interview_place', 'interview_date', 'interview_status']

        def clean(self):
            pass
