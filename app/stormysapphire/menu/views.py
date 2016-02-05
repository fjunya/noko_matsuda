import logging

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from menu.models import Information
from menu.forms import InformationEditForm

logger = logging.getLogger('common')

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin(request):
    return render(request, 'menu/admin.html')

@csrf_protect
@login_required
def main(request):
    information = Information.objects.filter(type=Information.MENU_TYPE
                                             ).order_by('-created_at').first()
    if request.method == 'POST':
        query = request.POST.copy()
        form = InformationEditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    information = Information(
                        body=form.cleaned_data['body'],
                        type=Information.MENU_TYPE,
                        user=User.objects.get(pk=request.user.id))
                    information.save()
            except Exception:
                logger.exception(None)
                raise 
            return redirect('main_menu')
    else:
        form = InformationEditForm(
            initial={'body': information.body if information else None})
    return render(
        request, 'menu/main.html', {'form': form, 'information': information})
