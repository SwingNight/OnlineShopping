from django.urls import path
from core.views import index

# app_name = "bananas"

urlpatterns = [
    # path("bananas/", index),
    path('', index, name="index")
]