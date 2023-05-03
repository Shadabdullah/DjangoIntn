
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  UserRegistration, WorkListView


from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'works', WorkListView)



urlpatterns = [
    path('api/register/', UserRegistration.as_view(), name='register'),
    path('api/', include(router.urls)),
    
]
handler404 = "apis.views.error_404_view"



# python manage.py makemigrations
# python manage.py migrate  