from typing import SupportsIndex
from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopluated_fields = {'slug': ('title'), }

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    # Post 레코드 리스트를 가져오는 get_queryset()메소드를 오버라이딩함. 그 이유는 Post테이블과 Tag테이블이 manytomany관계이므로, tag테이블의 관련 레코드를 한 번의 쿼리로 미리 가져오기 위함.
    # 이렇게 n:n관계에서 쿼리 횟수를 줄여 성능을 높이고자 할 때 prefetch_realated()메소드를 사용한다.

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
