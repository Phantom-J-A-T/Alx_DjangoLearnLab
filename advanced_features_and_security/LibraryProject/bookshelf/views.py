from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def home(request):
    return render(request, 'relationship_app/home.html')

@permission_required('relationship_app.can_create_userprofile', raise_exception=True)
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'relationship_app/profile_form.html', {'form': form})

@permission_required('relationship_app.can_edit_userprofile', raise_exception=True)
def edit_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'relationship_app/profile_form.html', {'form': form})

@permission_required('relationship_app.can_delete_userprofile', raise_exception=True)
def delete_profile(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'relationship_app/profile_confirm_delete.html', {'profile': profile})


@permission_required('relationship_app.can_view_userprofile', raise_exception=True)
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'relationship_app/profile_list.html', {'profiles': profiles})