from django.shortcuts import render


def browser_page(request):
    return render(request, 'beats/browser.html')


def piano_page(request):
    return render(request, 'beats/piano_player.html')
