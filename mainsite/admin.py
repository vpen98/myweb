from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','pub_date') # 在管理页显示标题，时间等内容
    search_fields = ('title','slug')
    
admin.site.register(Post,PostAdmin)