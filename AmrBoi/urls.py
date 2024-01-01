from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('category/<slug:category_slug>', views.Home,name='category_wise_book'),
    path('', views.Home,name='homepage'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
