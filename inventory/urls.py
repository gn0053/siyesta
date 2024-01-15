from django.urls import path

from . import views

app_name="inventory"
urlpatterns = [
    path("", views.index, name="index"),
    path("load-inventory/", views.load_inventory, name="load_inventory"),
    path("save-item/", views.save_item, name="save_item"),
    path("remove-item/", views.remove_item, name="remove_item"),
    path("restore-item/", views.restore_item, name="restore_item"),
    path("status-change/", views.change_status, name="change_status"),
    path("export-items/", views.exportItems, name="exportItems"),
]