from core.models import Service

def menu(request):
    services = Service.objects.filter(status="published")

    return {
        'services': services,
    }