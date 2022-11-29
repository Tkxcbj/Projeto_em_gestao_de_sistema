from django.shortcuts import render


def home(request):
    access_level = request.session.get('access_level', 0)
    return render(request, 'main/pages/home.html', context={
        'access_level': access_level,
    })


def test(request):
    return render(request, 'main/verification.html', context={
        'access_level': 2
    })


def about(request):
    access_level = request.session.get('access_level', 0)
    return render(request, 'main/pages/about.html', context={
        'access_level': access_level,
    })
