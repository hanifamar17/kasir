from django.http import HttpResponseRedirect

def homepage(request):
    # Redirect langsung ke halaman admin
    return HttpResponseRedirect('/admin/')
