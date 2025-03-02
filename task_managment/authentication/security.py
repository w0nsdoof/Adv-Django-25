from django.conf import settings
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ForgetPasswordThrottle(AnonRateThrottle):
    rate = '2/min'

class LoginThrottle(UserRateThrottle):
    rate = '5/min'
    
