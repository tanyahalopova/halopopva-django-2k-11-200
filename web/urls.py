from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, inventory_edit_view, kind_of_sport_view, \
    kind_of_sport_delete

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('logout/', logout_view, name="logout"),
    path('inventory/add/', inventory_edit_view, name="inventory_add"),
    path('inventory/<int:id>/', inventory_edit_view, name="inventory_edit"),
    path('kind_of_sport/', kind_of_sport_view, name="kind_of_sport"),
    path('kind_of_sport/<int:id>/delete', kind_of_sport_delete, name="kind_of_sport_delete")
]
