from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Goals n\' Glory',
        'name': 'Sahila Khairatul Athia',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)