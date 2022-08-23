from django.shortcuts import render

# Create your views here.
def reviews(request):
    context = {}
    return render(request, 'reviews/review_home.html', context)