from re import template
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from .models import Post
# Create your views here.

# ----ListView


class PostLV(ListView):
    model = Post
    # 지정하지 않으면 디폴트 템플릿 파일명은 blog/post_list.html이 된다.
    template_name = 'blog/post_all.html'  # 디폴트 템플릿 파일명은 blog/post_list.html임.
    context_object_name = 'posts'  # 템플릿 파일로 넘겨주는 객체 리시트에 대한 컨텍스트 변수명
    # data = Post.objects.all()
    # p = Paginator(data, 3)
    paginate_by = 2  # 한 객체에서 보여주는 객체 리스트의 숫자


# ----DetailView


class PostDV(DetailView):
    model = Post

# ----ArchiveView


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    # 속성이 true면 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨준다. 즉 템플릿 파일에서 object_list컨텍스트 변수를 사용할 수 있음.
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    month_format = '%m'
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
