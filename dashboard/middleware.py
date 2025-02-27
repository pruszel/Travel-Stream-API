from django.shortcuts import redirect
from django.conf import settings


class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == f"{settings.APP_NAME}.fly.dev":
            return redirect(f"https://api.travelstreamapp.com{request.path}", permanent=True)

        response = self.get_response(request)
        return response
