from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic


# Create your views here.

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'polls.add_choice'
    login_url = "bases:login"
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name = 'bases/sin_privilegios.html'
