from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Vina Myrnauli Abigail Siallagan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)