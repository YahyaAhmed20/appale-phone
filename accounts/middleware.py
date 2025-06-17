from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile

class CompletePhoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # استثناء صفحات معينة
            excluded_paths = [reverse('accounts:profile_edit'), reverse('logout'), reverse('login')]
            if request.path not in excluded_paths:
                profile, created = Profile.objects.get_or_create(user=request.user)
                if not profile.phone_number or profile.phone_number.strip() == "":
  # استخدم phone_number بدلاً من phone
                    return redirect('accounts:profile_edit')
        return self.get_response(request)