from django.urls import path
from . import views

# urlpatterns = [
#     path('public/', views.public_view, name='public_view'),
#     path('private/', views.private_view, name='private_view'),
# ]

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
]
