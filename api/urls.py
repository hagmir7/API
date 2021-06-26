from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', detail, name='detail_post'),
]