from rest_framework import routers
from .views import QuoteView

router = routers.DefaultRouter()
router.register(r'quotes', QuoteView)
