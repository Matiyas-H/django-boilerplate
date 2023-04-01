from django.shortcuts import render
from .models import User
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

User = get_user_model()



class Profile(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "pages/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_info"] = self.request.user
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "pages/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_form'] = PasswordChangeForm(self.request.user)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        password_form = PasswordChangeForm(self.request.user, self.request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(self.request, user)
        return response
    def get_success_url(self):
        return reverse('detail', kwargs={'username': self.request.user.username})

def home(requests):
    return render(requests, "pages/home.html")
    



