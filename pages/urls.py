from django.urls import path
from .import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('<int:pk>/', views.PhilanthropistDetailView.as_view(), name='philanthropist_detail'),
    path('philanthropist/<int:pk>/', views.PhilanthropistDetailView.as_view(),name='philanthropist'),
    path('homecontact/', views.HomeContactView.as_view(), name='homecontact')
]