from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'

@login_required
@user_passes_test(is_admin)

def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html')