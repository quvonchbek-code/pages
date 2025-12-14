from django.urls import path
from .views import HomepageView,AboutView,MainView,FinalView
urlpatterns=[
    path('main/',MainView.as_view(),name='main'),
    path('final/',FinalView.as_view(),name='final'),
    path('about/',AboutView.as_view(),name='about'),
    path('',HomepageView.as_view(),name='home'),
   
]