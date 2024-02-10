from django.shortcuts import render

def index(request):
    x = 5;
    y = calculateSome(80,90)
    context = {
        'x':y,
        "title": "Django example",
    }
    return render(request, "index.html", context)


def calculateSome(x,y):
    return x+y;