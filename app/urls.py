from django.urls import path
from app.views import home, add_todo, delete_todo, edit_todo

urlpatterns = [
    path('', home, name='home'),
    path('add_todo/', add_todo, name='add_todo'),
    path('delete_todo/<int:id>', delete_todo, name='delete_todo'),
    path('edit_todo/<int:id>', edit_todo, name='edit_todo'),
]
