from django.shortcuts import render

# Create your views here.
def reviews(request):
    context = {
        'page_name': 'Reviews', # Name of the current page
    }
    return render(request, 'reviews/review_home.html', context)
