from django.urls import path  
from . import views

urlpatterns = [
    path('', views.page_view, name='home'), 
    path('index/', views.index, name='index'),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('nutrient-data/', views.nutrient_data, name="nutrient-data"),  
    path("chart-data/", views.chart_data, name="chart-data"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout' ), 
    path("add-food/", views.add_food, name="add-food"),
    path("update-goals/", views.update_goals, name="update-goals"),
]
