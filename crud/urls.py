
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', views.website),
    path('about/', views.about,name='about'),
    path('broom/', views.bedroom,name='broom'),
    path('kitchen/', views.kitchen,name='kitchen'),
    path('dining/', views.dining,name='dining'),
    path('byard/', views.backyard,name='byard'),
]
