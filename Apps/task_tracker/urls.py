from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name='feature-landing'),
    path('home/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('home/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('home/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('home/new/', TaskCreateView.as_view(), name='task-create'),
    path('home/', TaskListView.as_view(), name='task-tracker-home'),
    path('about/', views.about, name='task-tracker-about'),
    path('contact/', views.contact, name='feature-contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
