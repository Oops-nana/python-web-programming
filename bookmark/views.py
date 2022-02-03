from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Bookmark
# Create your views here.


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark
