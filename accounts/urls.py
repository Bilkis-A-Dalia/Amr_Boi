from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.UserRegistrationView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('edit_profile/',views.UserUpdateView.as_view(),name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('borrow/<int:id>',views.borrow,name='borrow'),
    path('return_book/<int:id>',views.return_book,name='return_book'),
    path('deposit',views.DepositMoneyView.as_view(),name='deposit'),
]