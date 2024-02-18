from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.views import View
from accounts.models import MyUser, UserAddress
from accounts.forms import ProfileEditForm


class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=kwargs['pk'])
        user_address = UserAddress.objects.filter(user=user)
        return render(request, 'accounts/profile.html', {'user': user, 'user_address': user_address})

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=kwargs['pk'])
        form = ProfileEditForm(self.request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تعغیرات اعمال شدن', 'success')
            return redirect('accounts:profile', pk=user.id)
        return render(request, 'accounts/profile.html', {'form': form})
