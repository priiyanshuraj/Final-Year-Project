# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from django.conf import settings
# from django.conf.urls.static import static

# from django.shortcuts import render



# urlpatterns = [
#     path('api/group-expenses/', include, name='group_expenses'),
#     path('admin/', admin.site.urls),

#     # JWT Authentication Routes
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token

#     # Group Expenses API Routes
#     path('api/group-expenses/', include('group_expenses.urls')),  # Include the group_expenses URLs
    
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
#     path('api/transactions/', include('transactions.urls')),  # Ensure this is correctly included
#     path('api/payments/', include('payments.urls')),
    
#     path('api/notifications/', include('notifications.urls')),
#     path('transactions/', include('transactions.urls')),  
#     path('insights/', include('insights.urls')),
#     path('admin_dashboard/', include('admin_dashboard.urls')),
#     path('', include('frontend.urls')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Authentication (JWT) ---
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # --- API Routes (Backend Logic) ---
    path('api/users/', include('users.urls')),
    path('api/transactions/', include('transactions.urls')), 
    path('api/group-expenses/', include('group_expenses.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/notifications/', include('notifications.urls')),

    # --- Frontend Pages (UI) ---
    # Login & Signup pages
    path('admin_dashboard/', include('admin_dashboard.urls')), 
    
    # Insights & Charts
    path('insights/', include('insights.urls')),
    
    # Homepage & Dashboards (Must be last to catch empty paths)
    path('', include('frontend.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)