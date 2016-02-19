from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class MyAuth:
    def authenticate(self, email="", password=""):
        try:
            import pdb;pdb.set_trace()
            user = User.objects.get(email=email)
            print user
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None