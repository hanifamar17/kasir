import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.timezone import now

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            current_time = now()

            if last_activity:
                elapsed_time = (current_time - datetime.datetime.fromisoformat(last_activity)).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
            request.session['last_activity'] = current_time.isoformat()

        response = self.get_response(request)
        return response
