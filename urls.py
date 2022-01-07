from django.conf.urls import url
from django.urls import path
from traveling_app import views
from .models import contact, Content_List
from .views import Content_ListListView, Content_ListDetailView

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('services/', views.services, name='services'),
    path('content/<page>', Content_ListListView.as_view(), name='list'),
    path('content/<slug>', Content_ListDetailView.as_view(), name='detail')
]
