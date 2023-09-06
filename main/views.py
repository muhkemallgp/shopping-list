from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Kemal Ganteng (Muh.Kemal Lathif GP)',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)