from django.urls import path, include
from . import views
from rest_framework import routers

from .models import BookImage
from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet, basename="books" )

router.register("images", BookImageViewSet, basename="book-images")

urlpatterns = [
    # path('books', views.get_books),


    path('', include(router.urls)),

    path('authors/', views.AddAuthorView.as_view(), name='add_author'),

    path('authors/<int:pk>/', views.GetUpdateDeleteAuthorView.as_view()),

    # path('images/<int:pk>/', views.image_detail, name='book-image-detail'),
    # path('delete/authors/<int:pk>', views.delete_author, name='delete_author'),
    #
    # path('get/authors/', views.get_authors, name='get_authors'),

    # path('greet<name>', views.greet),]
]
