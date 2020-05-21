from django.urls import path
from . import views

urlpatterns = [
    # path('data1/',views.TestModelView1.as_view()),
    # path('query1/',views.TestModelView2.as_view()),
    path('query2/',views.TestModelView3.as_view()),
    path('books/', views.BooksView.as_view()),
]