from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
]
