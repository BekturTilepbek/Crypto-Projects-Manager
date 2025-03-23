from django.urls import path

from webapp.views import ProjectListView, CreateProjectView, UpdateProjectView, ProjectDetailView, DeleteProjectView
from webapp.views import CreateLinkView, UpdateLinkView, DeleteLinkView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('projects/create/', CreateProjectView.as_view(), name='create_project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('projects/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),
    path('projects/<int:pk>/links/create/', CreateLinkView.as_view(), name='create_link'),
    path('links/<int:pk>/update', UpdateLinkView.as_view(), name='update_link'),
    path('links/<int:pk>/delete/', DeleteLinkView.as_view(), name='delete_link')
]
