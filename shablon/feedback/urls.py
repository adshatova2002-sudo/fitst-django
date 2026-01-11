from django.urls import path
from .views import *

urlpatterns = [
    path('', feedback_page),
    path('add_feedback/', add_feedback_page, name="add_feedback_page"),
    path('end/', end_page, name="end_page"),
]