# urls.py

from django.urls import path
from django.views.generic.base import RedirectView
from .views import calculator_view, login_view, logout_view

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),  # Default to login page
    path('calculator/', calculator_view, name='calculator'),  # Calculator view (requires login)
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout page
]
