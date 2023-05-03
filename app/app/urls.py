
from apis import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.home_view,name="home"),
    path('admin/', admin.site.urls),
    path('', include('apis.urls')),
    
]


# python manage.py makemigrations