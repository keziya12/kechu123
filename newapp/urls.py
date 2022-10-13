from .import views
from django.urls import path

urlpatterns = [
    path('',views.fun, name='fun'),
    path('movie/<int:movie_id>/',views.fun2, name='fun2')

]