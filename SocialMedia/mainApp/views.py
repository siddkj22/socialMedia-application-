from django.shortcuts import render

# Create your views here.

from .models import HashTag
from .forms import Tweetform

def index(request):
    return render(request,'mainApp/index.html')


def HashTagShow(request):
    twits = HashTag.objects.order_by('date_added')
    context = {'main':twits}
    return render(request,'mainApp/main.html',context)



def new_tweet(request):
    if request.method != 'POST':
        form = Tweetform()

    else:
        form = Tweetform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainApp:HashTagShow')

    context = {'form':form}
    return render(request,'mainApp/new_tweet.html',context)






