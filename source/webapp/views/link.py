from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from webapp.models import Link, Project
from webapp.forms import LinkForm


class CreateLinkView(CreateView):
    template_name = "link/create_link.html"
    form_class = LinkForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().dispatch(request, args, kwargs)

    def form_valid(self, form):
        link = form.save(commit=False)
        link.project = self.project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.project.pk})


class UpdateLinkView(UpdateView):
    template_name = "link/update_link.html"
    form_class = LinkForm
    model = Link

    def get_success_url(self):
        return reverse('webapp:projects')


class DeleteLinkView(DeleteView):
    model = Link

    def get_success_url(self):
        return reverse('webapp:projects')
