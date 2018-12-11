from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from Quiz import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register/', views.register_view, name="register"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('new_quiz/', views.new_quiz_view, name="new_quiz"),
    path('quiz/<int:quiz_id>/<int:question_no>', views.question_view, name="question"),
    path('quiz/<int:quiz_id>/add_question/<int:question_no>', views.add_question_view, name="add_question"),
    path('results/<int:quiz_id>', views.result_view, name="results"),
    path('delete/<int:quiz_id>', views.delete_quiz_view, name="delete_quiz"),
    path('logout', views.signout_view, name="signout"),
]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^cv/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT,
        }),
           ]
