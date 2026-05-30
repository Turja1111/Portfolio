from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/paper/', views.research_paper_pdf, name='research_paper_pdf'),
    path('cv/download/', views.download_cv, name='download_cv'),
]
