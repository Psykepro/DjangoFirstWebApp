from django.contrib.auth import get_user_model

User = get_user_model()

random_ = User.objects.last()

#my_followers

random_.profile.followers.all()

# who I follow
random_.is_followers.all()
