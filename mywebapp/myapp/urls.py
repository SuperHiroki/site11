from django.urls import path
from . import views

urlpatterns=[
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('bunpunotokuchou/', views.bunpunotokuchou, name='bunpunotokuchou'),
    path('hubyoudoudo/', views.hubyoudoudo, name='hubyoudoudo'),
    path('nihensuunokankei/', views.nihensuunokankei, name='nihensuunokankei'),
    path('kakuritunokiso/', views.kakuritunokiso, name='kakuritunokiso'),
    path('kakuritubunputokitaichi/', views.kakuritubunputokitaichi, name='kakuritubunputokitaichi'),
    path('yuumeinakakuritubunpu/', views.yuumeinakakuritubunpu, name='yuumeinakakuritubunpu'),
    path('tahensuunokakuritubunpu/', views.tahensuunokakuritubunpu, name='tahensuunokakuritubunpu'),
    path('randamuhyouhonkaranosuisoku/', views.randamuhyouhonkaranosuisoku, name='randamuhyouhonkaranosuisoku'),
    path('suitei/', views.suitei, name='suitei'),
    path('kasetukentei/', views.kasetukentei, name='kasetukentei'),
    path('kaikibunseki/', views.kaikibunseki, name='kaikibunseki'),
    path('keizaisyakaideitanotoukeibunseki/', views.keizaisyakaideitanotoukeibunseki, name='keizaisyakaideitanotoukeibunseki'),
    path('jikeiretudeitanotoukeibunseki/', views.jikeiretudeitanotoukeibunseki, name='jikeiretudeitanotoukeibunseki'),
    path('jikken/', views.jikken, name='jikken'),
]