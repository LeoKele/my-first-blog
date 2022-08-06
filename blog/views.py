from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here. 

#Como puedes ver, hemos creado una función (def) llamada post_list que acepta request y return una función render que reproduce (construye) 
# nuestra plantilla blog/post_list.html.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
