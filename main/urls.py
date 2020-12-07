from django.contrib import admin
from django.urls import include, path
from poll import views as poll_views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<poll_id>/', poll_views.vote, name='vote'),
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
]