from django.conf.urls import url
from api.views import lol_views, champs_views, items_views, naive_view, items_name_views, ban_views, addTeamDataView, items_chart_views, lol_ban_views, randomforest_views, user_views, naive_data_views
from django.urls import path
urlpatterns = [
    url('lol-champion-list/$', champs_views.champions, name='lol-champion-list'),
    url('lol-item-list/$', items_views.items_data3, name='lol-item-list'),
    url('lol-lolgating-list/$', naive_view.champion_data, name='lol-lolgating-list'),
    url('lol-item-name-list/$', items_name_views.Name_data1, name='lol-item_name-list'),
    url('lol-pickban-list/$', ban_views.pickbans, name='lol-pick-ban-list'),
    url('lol-addTeamData-list/$', addTeamDataView.champion_data, name='lol-addTeamData-list'),
    url('lol-item-chart-list/$', items_chart_views.itempick1, name='lol-item-chart-list'),
    url('lol-ban-count-list/$', lol_ban_views.bancounting1, name='lol-ban-count-list'),
    url('lol-user-info/$', user_views.users, name='lol-user-info'),
    url('lol-navie-data-list/$', naive_data_views.naive_data, name='navie-data-list'),
    url('lol-win-variable/$', randomforest_views.win_variable, name='lol-win-variable'),



]
