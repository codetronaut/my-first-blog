from django.utils import timezone
from .models import Post
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})






'''def handler(request):


    if request.method == 'GET':
        NewAppFormSet = modelformset_factory(Application)

    return render_to_response(request, "template/apps.html",{"new_app_form":NewAppFormSet})'''
