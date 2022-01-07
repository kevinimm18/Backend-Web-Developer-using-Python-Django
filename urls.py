from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from traveling_app.views import  Content_ListListView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    url(r'^traveling_app/', include(('traveling_app.urls', 'traveling_app'), namespace='traveling_app')),
    path('admin/', admin.site.urls),

    # path('content/', Content_ListListView.as_view(), app_name='list', namespace='list')
]































# urlpatterns = [
#     path('', include('traveling_app.urls')),
#     path('admin/', admin.site.urls),
