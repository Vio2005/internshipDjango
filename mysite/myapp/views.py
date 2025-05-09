from django.shortcuts import render
from .models import Post
from .models import Myfriend

# Create your views here.
def postdata(request):
    post_data=Post.objects.all()
    context={'post_data':post_data}
    return render(request,'posts.html',context)

def frienddata(request):
    friend_data=Myfriend.objects.all()
    context={'friend_data':friend_data}
    return render(request,'friends.html',context)
