from django.shortcuts import redirect

def redirect_dashboard(request):
    return redirect('post_list_url', permanent=True)