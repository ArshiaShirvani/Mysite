from accounts.models import Profile

def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user) 
            if not profile.first_name or not profile.last_name:  
                return {"user_profile": f"کاربر جدید  {request.user.id}"}
            return {"user_profile": profile}
        except Profile.DoesNotExist:
            return {"user_profile": f"کاربر جدید  {request.user.id}"}  
    return {}