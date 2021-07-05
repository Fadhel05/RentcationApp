from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Rentcation.RentcationApp.views.CategoryViews import CategoryView
from Rentcation.RentcationApp.views.CheckoutViews import CheckoutView
from Rentcation.RentcationApp.views.DestinationViews import DestinationView
from Rentcation.RentcationApp.views.ImageView import droptable, ImageView
from Rentcation.RentcationApp.views.CustomerViews import CustomerView
from Rentcation.RentcationApp.views.BookingViews import BookingView
from Rentcation.RentcationApp.views.PaymentViews import PaymentView
from Rentcation.RentcationApp.views.ProductViews import ProductView
from Rentcation.RentcationApp.views.ReviewViews import ReviewView

router = DefaultRouter()
router.register(r'user',CustomerView)
router.register(r'product',ProductView)
router.register(r'category',CategoryView)
router.register(r'image',ImageView)
router.register(r'booking',BookingView)
router.register(r'checkout',CheckoutView)
router.register(r'payment',PaymentView)
router.register(r'destination',DestinationView)
router.register(r"review",ReviewView)

urlpatterns = [
    path('user/update_location/<int:pk>/',CustomerView.as_view({"put":"update_location"})),
    path('', include(router.urls)),
    path('drop_table/',droptable)
]