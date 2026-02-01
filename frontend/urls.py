# from django.urls import path
# from . import views  # <--- This imports the whole file, making 'views.' work

# urlpatterns = [
#     # Homepage - Redirects to dashboard logic
#     #  path('', views.dashboard_stats, name='home'),

#     # Dashboard Pages
#     path('dashboard-stats/', views.dashboard_stats, name='dashboard_stats'),
#     path('financial-summary/', views.financial_summary, name='financial_summary'),
#     path('spending-analysis/', views.spending_analysis, name='spending_analysis'),
    
# ]

from django.urls import path
from . import views  # <--- Import the views from the current folder

urlpatterns = [
    # Homepage (Redirects to dashboard logic)
    path('', views.financial_summary, name='home'), 
    
    # Dashboard Pages
    path('dashboard-stats/', views.dashboard_stats, name='dashboard_stats'),
    path('financial-summary/', views.financial_summary, name='financial_summary'),
    path('spending-analysis/', views.spending_analysis, name='spending_analysis'),
    
]