from django.shortcuts import redirect

def redirect_main(request):
    return redirect('main_url', permanent=True)