from django.http import HttpResponse

class FaviconMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/favicon.ico':
            return HttpResponse(status=204)  # No Content
        response = self.get_response(request)
        return response