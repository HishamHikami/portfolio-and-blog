from core.models import Service

def menu(request):
    services = Service.objects.all()

    return {
        'services': services,
    }