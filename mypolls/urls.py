from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Andere URL-configuraties hierboven
    
    path('polls/', include('mypolls.urls')),  # Voeg deze regel toe
]