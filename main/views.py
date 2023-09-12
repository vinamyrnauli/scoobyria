from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Vina Myrnauli Abigail Siallagan',
        'class': 'PBP E',
        'harga': 'Rp200.000,00',
    }

    return render(request, "main.html", context)