from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^/?$', RedirectView.as_view(url='main_menu'), name='top'),

    url(r'^main_menu/$', 'menu.views.main', name='main_menu'),
    url(r'^admin_menu/$', 'menu.views.admin', name='admin_menu'),

    url(r'^login/?$', 'django.contrib.auth.views.login',
        {'template_name': 'menu/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'top'}, name='logout'),

    url(r'^account/create/?$', 'account.views.create', name='account_create'),
    url(r'^account/export/?$', 'account.views.export', name='account_export'),
    url(r'^account/delete/?$', 'account.views.delete', name='account_delete'),
    url(r'^account/import/?$', 'account.views.import_', name='account_import'),
    url(r'^account/listing/?$', 'account.views.list', name='account_listing'),
    url(r'^account/update/(?P<user_id>[0-9]+)/?$', 'account.views.update',
        name='account_update'),

    url(r'^account_group/create/?$', 'accountgroup.views.create',
        name='account_group_create'),
    url(r'^account_group/export/?$', 'accountgroup.views.export',
        name='account_group_export'),
    url(r'^account_group/delete/?$', 'accountgroup.views.delete',
        name='account_group_delete'),
    url(r'^account_group/import/?$', 'accountgroup.views.import_',
        name='account_group_import'),
    url(r'^account_group/listing/?$', 'accountgroup.views.list',
        name='account_group_listing'),
    url(r'^account_group/update/(?P<account_group_id>[0-9]+)/?$',
        'accountgroup.views.update', name='account_group_update'),

    url(r'^participant/create/?$', 'participant.views.create',
        name='participant_create'),
    url(r'^participant/export/?$', 'participant.views.export',
        name='participant_export'),
    url(r'^participant/delete/?$', 'participant.views.delete',
        name='participant_delete'),
    url(r'^participant/import/?$', 'participant.views.import_',
        name='participant_import'),
    url(r'^participant/listing/?$', 'participant.views.list',
        name='participant_listing'),
    url(r'^participant/update/(?P<participant_id>[0-9]+)/?$',
        'participant.views.update', name='participant_update'),
    url(r'^api/participant/listing/?$', 'participant.views.list_api',
        name='participant_listing_api'),
    url(r'^api/ping/(?P<host>[0-9\.]+)/?$', 'participant.views.ping_api',
        name='participant_ping_api'),

    url(r'^participant_group/create/?$', 'participantgroup.views.create',
        name='participant_group_create'),
    url(r'^participant_group/export/?$', 'participantgroup.views.export',
        name='participant_group_export'),
    url(r'^participant_group/delete/?$', 'participantgroup.views.delete',
        name='participant_group_delete'),
    url(r'^participant_group/import/?$', 'participantgroup.views.import_',
        name='participant_group_import'),
    url(r'^participant_group/listing/?$', 'participantgroup.views.list',
        name='participant_group_listing'),
    url(r'^participant_group/update/(?P<participant_group_id>[0-9]+)/?$',
        'participantgroup.views.update', name='participant_group_update'),

    url(r'^reserve/daily/?$', 'reserve.views.now_daily',
        name='reserve_now_daily'),
    url(r'^reserve/daily/(?P<ymd>[0-9]{8})/(?P<time>[123])/?$',
        'reserve.views.daily', name='reserve_daily'),
    url(r'^reserve/monthly/?$', 'reserve.views.now_monthly',
        name='reserve_now_monthly'),
    url(r'^reserve/monthly/(?P<ym>[0-9]{6})/?$', 'reserve.views.monthly',
        name='reserve_monthly'),
    url(r'^reserve/weekly/?$', 'reserve.views.now_weekly',
        name='reserve_now_weekly'),
    url(r'^reserve/weekly/(?P<yw>[0-9]{6})/(?P<time>[123])/?$',
        'reserve.views.weekly', name='reserve_weekly'),
    url(r'^api/reserve/listing/?$', 'reserve.views.list_api',
        name='reserve_listing_api'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
