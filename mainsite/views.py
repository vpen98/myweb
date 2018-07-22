from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect 
# Create your views here.


def homepage(request):
    template = get_template('index.html') # 加载网页模板
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())  #把当前内存中的所有局部变量使用字典类型打包起来 
    return HttpResponse(html)

def showpost(request,id):
    template = get_template('post.html')
    try:
        post = Post.objects.get(id=id)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')  # 发生例外时直接返回首页