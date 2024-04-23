from django.urls import path
from . import views
urlpatterns = [
    path('',views.FlowerList.as_view()),
    path('FlowerData/<int:id>/',views.FlowerData.as_view())
]
