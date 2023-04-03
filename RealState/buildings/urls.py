from django.urls import path, include

from .views import HomeListAPIView, HomeDetailsAPIView, ImageView

urlpatterns = [
    path('', HomeListAPIView.as_view(), name="list"),
    path('<slug>', HomeDetailsAPIView.as_view(), name="home-details"),
    path('images/<pk>', ImageView.as_view(), name="images"),
]
