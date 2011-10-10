# coding: utf-8
import requests
from django.conf import settings
from django.http import HttpResponse
from main import BRZipCode


def zipcode_view(request):
    """
    This view is just a proxy to brzipcode webservice (avoiding parsing and
    serializing the same content)
    """
    return HttpResponse(BRZipCode.get(
        zip_code=request.GET.get('zip_code'),
        token=settings.BRZIPCODE_TOKEN,
        plain_text=True,
    ))
