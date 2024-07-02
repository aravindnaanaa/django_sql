from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="flights"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>',views.flight,name="flight"),
    path('<int:flight_id>/book',views.book,name="book"),
    # Add other URL patterns here
]
