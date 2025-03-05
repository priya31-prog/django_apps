from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# register
router.register(r"grocery", views.GroceryViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
