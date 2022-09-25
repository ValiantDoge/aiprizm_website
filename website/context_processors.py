from .models import *

def context_base(request):
    service = Service.objects.all()
    client = Client.objects.all()
    return { 'client': client, 'service': service }