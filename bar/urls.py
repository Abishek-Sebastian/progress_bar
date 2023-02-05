from django.urls import path
from .import views

urlpatterns = [
    path('import/', views.import_data, name='import_data'),
    path('get_progress/', views.get_progress, name='get_progress'),
]
