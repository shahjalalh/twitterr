from django.shortcuts import render, get_object_or_404, redirect


from .models import Tweet


# Create your views here.

def tweet_detail_view(request, pk=None):
    # obj = Tweet.objects.get(pk=pk)
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }

    return render(request, "tweets/detail_view.html", context)
