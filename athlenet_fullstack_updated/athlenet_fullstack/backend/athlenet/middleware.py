import logging
import os

from django.http import HttpResponseServerError


logger = logging.getLogger(__name__)


class RequireProductionSecretKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (os.getenv('RENDER') or os.getenv('VERCEL')) and not os.getenv('DJANGO_SECRET_KEY'):
            logger.error('DJANGO_SECRET_KEY must be set when DEBUG is disabled.')
            return HttpResponseServerError(
                'Server configuration error: DJANGO_SECRET_KEY is not configured.'
            )
        return self.get_response(request)
