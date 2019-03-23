from django.utils import timezone
from .models import Post
from django.shortcuts import render

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/post_list.html', {'posts':posts})

















'''def handler(request):


    if request.method == 'GET':
        NewAppFormSet = modelformset_factory(Application)

    return render_to_response(request, "template/apps.html",{"new_app_form":NewAppFormSet})'''
