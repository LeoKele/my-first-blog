from django.shortcuts import render

# Create your views here. 

#Como puedes ver, hemos creado una función (def) llamada post_list que acepta request y return una función render que reproduce (construye) 
# nuestra plantilla blog/post_list.html.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
