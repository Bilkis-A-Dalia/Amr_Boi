from django.urls import path
from .import views

urlpatterns = [
    path('detail_view/<int:id>', views.DetailsBookView.as_view(), name='detail_books'),
]