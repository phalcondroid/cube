from django.urls import path

from . import views

app_name = 'cube'
urlpatterns = [
    path('<int:shape_id>', views.index, name='index'),
    path('<int:shape_id>/save/', views.save, name='save'),
]