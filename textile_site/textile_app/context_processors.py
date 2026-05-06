from .models import Business


def business_data(request):

    business = Business.objects.first()

    return {
        'business': business
    }