from django.urls import path
from books import views


app_name = 'books'

urlpatterns = [
    path('catalogue/<int:user_id>/', views.render_book_catalogue, name='catalogue'),
    path('create/<int:user_id>/', views.create_book, name='create'),
    path('edit/<int:book_id>/', views.edit_book, name='edit'),
    path('delete/<int:book_id>/', views.delete_book, name='delete'),
]
