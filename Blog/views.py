from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'Blog/post_list.html', {})


'''def handler(request):
    if request.method == 'GET':
        NewAppFormSet = modelformset_factory(Application)

    return render_to_response(request, "template/apps.html",{"new_app_form":NewAppFormSet})'''