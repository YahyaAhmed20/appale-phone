from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        """
        السماح بالتسجيل التلقائي بدون عرض صفحة /3rdparty/signup/
        """
        return True

    def pre_social_login(self, request, sociallogin):
        """
        لو في مستخدم بنفس الإيميل، اربطه تلقائيًا بحساب Google بدلاً من عرض صفحة signup.
        """
        if sociallogin.is_existing:
            return

        user_email = sociallogin.account.extra_data.get('email')
        if not user_email:
            return

        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            existing_user = User.objects.get(email__iexact=user_email)
        except User.DoesNotExist:
            return

        sociallogin.connect(request, existing_user)

    def save_user(self, request, sociallogin, form=None):
        """
        حفظ المستخدم الجديد تلقائيًا من بيانات Google
        """
        user = sociallogin.user
        user.email = user.email or sociallogin.account.extra_data.get('email', '')
        user.username = user.username or sociallogin.account.extra_data.get('name') or user.email.split('@')[0]
        user.set_unusable_password()
        user.save()
        sociallogin.save(request)
        return user
