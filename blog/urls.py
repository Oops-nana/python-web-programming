from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    # Exemple: /blog/
    path('', views.PostLV.as_view(), name='index'),

    # Exemple: /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # Exemple: /blog/post/django-example
    re_path(r'^post/(?P<slug>[-\w]+)/$',
            views.PostDV.as_view(), name='post_detail'),

    # Exemple /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Exemple /blog/archive/2019
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Exemple /blog/archive/2019/nov
    path('archive/<int:year>/<int:month>/',
         views.PostMAV.as_view(), name='post_month_archive'),

    # Exemple /blog/archive/2019/nov/10/
    path('archive/<int:year>/<int:month>/<int:day>/',
         views.PostDAV.as_view(), name='post_day_archive'),
    # 정규식 표현으로 제한하고 싶다면,
    #     re_path(r'^archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$',
    #             views.PostDAV.as_view(), name='post_day_archive'),

    # Exemple /blog/archive/2019/nov/10/
    path('archive/today', views.PostTAV.as_view(), name='post_today_archive'),

    # Exemple /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # Example /blog/tag/tagname
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(),
         name='tagged_object_list'),

]
