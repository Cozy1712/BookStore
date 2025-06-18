
from django.urls import path
from .api import *

urlpatterns = [
    path('list', BookListApi),
    path('create', BookCreateApi, name='create-book'),
    path('update/<int:id>', BookUpdateApi),
    path('delete/<int:id>', BookDeleteApi)
]