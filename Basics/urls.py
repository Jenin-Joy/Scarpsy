from django.urls import path
from Basics import views

urlpatterns = [
    path('Sum/',views.Sum,name="Sum"),
    path('Sum3/',views.Sum3,name="Sum3"),
    path('calculator/',views.calculator,name="calculator"),
    path('Largest/',views.Largest,name="Largest"),
    path('RankList/',views.RankList,name="RankList"),
    
    
]