from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, inventory_edit_view, kind_of_sport_edit, \
    kind_of_sport_delete, kind_of_sport_list, inventory_delete

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name="logout"),
    path('inventory/add/', inventory_edit_view, name="inventory_add"),
    path('inventory/<int:id>/', inventory_edit_view, name="inventory_edit"),
    path('inventory/<int:id>/delete', inventory_delete, name="inventory_delete"),
    path('kind_of_sport/list/', kind_of_sport_list, name="kind_of_sport_list"),
    path('kind_of_sport/<int:id>/', kind_of_sport_edit, name="kind_of_sport_edit"),
    path('kind_of_sport/add/', kind_of_sport_edit, name="kind_of_sport_add"),
    path('kind_of_sport/<int:id>/delete', kind_of_sport_delete, name="kind_of_sport_delete")
]
