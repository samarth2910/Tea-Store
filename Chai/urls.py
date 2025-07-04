from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.all_chai, name="all_chai"),
    path('<int:chai_id>/', views.chai_detail, name="chai_detail"),
    path('home/', views.chai_home, name="chai_home"),
    path('cart/', views.view_cart, name='view_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='Chai/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('chai_home')), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]