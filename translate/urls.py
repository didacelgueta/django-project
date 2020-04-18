from django.urls import path
#from .views import TranslateView
from . import views


urlpatterns = [
    path('', views.home, name='translate-home'),
    path('translate/', views.translate_page, name='translate'),
    #path('gettext/', views.get_text_to_translate, name='get_text'),
    path('translatetext/', views.translate_text, name='translate_text'),
    path('result/', views.result, name='result'),
    #path('translatetext/<translate_lang1>/<translate_lang2>/<translate_text>/', views.get_text_to_translate, name='translate_text')
]
