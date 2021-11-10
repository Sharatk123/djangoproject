from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('test/',views.test,name="test"),
    path('contact/', views.contact,name="contact"),
    path('add/', views.add,name="add"),
    path('upload_book/', views.upload_book,name="upload_book"),
    path('book_list/', views.book_list,name="book_list"),
    path('delete_book/<int:pk>', views.delete_book,name="delete_book"),
    path('send_email/', views.send_email,name="send_email"),

    path('ssession/',views.ssession,name="ssession"),
    path('gsession/',views.gsession,name="gsession"),

    path('scookies/',views.scookies,name="scookies"),
    path('gcookies/',views.gcookies,name="gcookies"),

    path('csvs/',views.csvs,name="csvs"),


]

