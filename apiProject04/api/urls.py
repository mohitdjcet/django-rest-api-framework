from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# urlpatterns = [
#     path('public/', views.public_view, name='public_view'),
#     path('private/', views.private_view, name='private_view'),
# ]

# urlpatterns = [
#     path('blogs/', views.blog_list, name='blog_list'),
# ]


urlpatterns = [
    path('get-token/', obtain_auth_token, name='api_token_auth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]