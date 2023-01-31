"""movies_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view(), name="main_page"),
    path("filter/", views.FilterMoviesView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name="json_filter"),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("reviews/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]
