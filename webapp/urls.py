from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("main/", views.main, name="main"),
    path("view-report/", views.viewreport, name="view-report"),
    path("bookmark/", views.bookmarks, name="bookmark"),
    path("analytics/", views.analytics, name="analytics"),
    path("casehistory/", views.casehistory, name="casehistory"),
    path("application/", views.application, name="application"),
    path("submit/", views.submit, name="submit"),
    path("citizen/", views.citizen, name="citizen"),
    path("select/", views.select, name="select"),
    # path('faq', views.faq, name='faq'),
    # path('notification', views.notification, name='notification'),
    # path('news', views.news, name='news'),
    path("citizen_report/", views.report_citizen, name="citizen_report"),
]
