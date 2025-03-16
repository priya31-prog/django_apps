from django.urls import path, include

# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r"accounts/<int:id>", views.AccountInfoView)

# urlpatterns = [
#     path("", include(router.urls)),
# ]


from . import views

urlpatterns = [
    path("ecommerce/", views.AccountInfoView),
    path("ecommerce/<int:id>/", views.SingleAccountView),
    path("address/", views.AddressView.as_view()),
    path("address/<int:pk>/", views.SingleAddress.as_view()),
]
