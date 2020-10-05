from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
# Create your views here.


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'userprofile/register.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'userprofile/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile updated successfully')
            return HttpResponseRedirect(reverse_lazy('profile'))
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
