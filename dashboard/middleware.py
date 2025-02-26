from django.shortcuts import redirect
from django.conf import settings

class RedirectToNonWww:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        host = request.META.get('HTTP_HOST')

        if host and host.startswith('www.'):
            non_www = host.replace('www.', '')
            return redirect('{}://{}{}'.format('https', non_www, request.get_full_path()), permanent=True)

        return response


class DomainRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == f"{settings.APP_NAME}.fly.dev":
            return redirect(f"https://travelstreamapp.com{request.path}", permanent=True)

        response = self.get_response(request)
        return response
