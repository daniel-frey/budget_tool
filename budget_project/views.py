from django.shortcuts import render


def home_view(request):
    """This is the home view."""
    context = {
        'message': 'Oooh yeah! Can do!'
    }
    return render(request, 'generic/home.html', context)
