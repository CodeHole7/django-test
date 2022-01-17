from django.urls import path, include
# from .api.v1.router import router
from .api.v1.views import QuoteView
urlpatterns = [
    path('quotes/', QuoteView.as_view()),
]