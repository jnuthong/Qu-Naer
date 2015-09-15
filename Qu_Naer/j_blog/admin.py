from django.contrib import admin
from j_blog.models import PersonalPost, PostTopic
# Register your models here.

class PersonalPostAdmin(admin.ModelAdmin):
    """
    REF: http://www.djangobook.com/en/2.0/chapter06.html
    """
    list_display = ('title', 'topic', 'index_time', 'author','language')
    search_fields = ('title', 'topic')
    fieldsets = (
        (None, {
            'fields': ('author',
                       'language',
                       'title',
                       'create_time',
                       'update_time',
                       'index_time',
                       'topic',
                       'post_status',
                       'content')
        }),
    )

admin.site.register(PersonalPost, PersonalPostAdmin)
admin.site.register(PostTopic)