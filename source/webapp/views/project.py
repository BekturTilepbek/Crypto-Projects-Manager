from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from webapp.models import Project, priorities, TIER_1, TIER_2, TIER_3, ANTIFOMO, ACTIVE
from webapp.forms import ProjectForm



class ProjectListView(ListView):
    model = Project
    template_name = "project/projects_list.html"
    ordering = ['created_at']
    context_object_name = 'projects'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        tier_1_queryset = []
        tier_2_queryset = []
        tier_3_queryset = []
        antifomo_queryset = []

        non_active_projects = []

        for project in queryset:
            if project.status == ACTIVE:
                if project.priority == TIER_1:
                    tier_1_queryset.append(project)
                elif project.priority == TIER_2:
                    tier_2_queryset.append(project)
                elif project.priority == TIER_3:
                    tier_3_queryset.append(project)
                else:
                    antifomo_queryset.append(project)
            else:
                non_active_projects.append(project)

        sorted_queryset = [*tier_1_queryset, *tier_2_queryset, *tier_3_queryset, *antifomo_queryset, *non_active_projects]

        sort_order = self.request.GET.get('sort', 'desc')
        if sort_order == 'asc':
            queryset = sorted_queryset[::-1]
        else:
            queryset = sorted_queryset
        return queryset



class CreateProjectView(CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project


class UpdateProjectView(UpdateView):
    template_name = "project/update_project.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class DeleteProjectView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('webapp:projects')
