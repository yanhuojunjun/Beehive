from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.initial),
    path('user/login/', views.user_login),
    path('user/signup/', views.user_signup),
    path('manager/image/', views.manager_image),
    path('manager/image_add/', views.manager_image_add),
    path('manager/image_delete/', views.manager_image_delete),
    path('manager/image_update/', views.manager_image_update),
    path('manager/user/', views.manager_user),
    path('manager/user_add/', views.manager_user_add),
    path('manager/user_delete/', views.manager_user_delete),
    path('manager/user_update/', views.manager_user_update),
    path('user/home/', views.user_home),
    path('user/myspace', views.myspace),
    path('user/share', views.share),
    path('user/image/', views.user_image),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
