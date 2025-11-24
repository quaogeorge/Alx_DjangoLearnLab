from django.utils.deprecation import MiddlewareMixin

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    """
    Minimal CSP middleware. Adjust the policy string below to match your assets.
    """
    def process_response(self, request, response):
        csp = "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;"
        response['Content-Security-Policy'] = csp
        return response