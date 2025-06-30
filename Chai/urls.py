
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_chai,name="all_chai"),
    path('<int:chai_id>/',views.chai_detail,name="chai_detail"),
    path('home/',views.chai_home,name="chai_home"),
    path('cart/', views.view_cart, name='view_cart'),

]
