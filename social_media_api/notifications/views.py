from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    notifications = request.user.notifications.filter(read=False)
    return render(request, 'notifications/notifications.html', {'notifications': notifications})
