from django.shortcuts import render


def home_page(request):
    return render(request, 'common/index.html')


def profile_page(request, profile_id):
    return render(request, 'common/profile.html')
