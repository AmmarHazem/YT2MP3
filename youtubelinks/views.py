from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import DownloadForm


class Home(FormView):
    form_class = DownloadForm
    success_url = reverse_lazy('home')
    template_name = 'home.html'

    def form_valid(self, form):
        return form.download()
