from multiprocessing import context
from re import template
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.conf import settings
from .models import Post
from django.views.generic import FormView  # FormView 클래스형 제네릭 뷰를 임포트
from blog.foms import PostSearchForm
from django.db.models import Q  # 검색 기능에 필요한 Q클래스를 임포트
from django.shortcuts import render
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id} - {self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


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


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post  # == queryset = Post.objects.all()
    context_object_name = 'tag_objects'
    # 기본적으로 queryset 속성 의 값을 반환 하지만 더 많은 로직을 추가하는 데 사용할 수 있습니다.

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):  # get_context_data 오버라이딩
        # 상위클래스의 컨텍스트 변수, 즉 변경 전의 컨텍스트 변수를 구한다.
        context = super().get_context_data(**kwargs)
        # URLConfig에 있는 파라미터 tag를 가져옴...
        context['tagname'] = self.kwargs['tag']

        return context


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(
            description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        # No Redirection
        return render(self.request, self.template_name, context)
