from django.urls import path
from .views import (
    SnackCreateView,
    SnackDeleteView,
    SnackDetailView,
    SnackListView,
    SnackUpdateView,
)

urlpatterns = [
    path(
        "", SnackListView.as_view(), name="snack_list"
    ),  # a list is an HTTP GET call on a general table
    path(
        "<int:pk>/", SnackDetailView.as_view(), name="snack_detail"
    ),  # an HTTP GET on a specific record
    path(
        "create/", SnackCreateView.as_view(), name="snack_create"
    ),  # an HTTP POST to the whole table; will add one record but don't know the primary key of the record
    path(
        "<int:pk>/update/", SnackUpdateView.as_view(), name="snack_update"
    ),  # 2 HTTP methods: PATCH (updating at least one field), PUT (provide the info for all fields, even if they stay the same or will change) ;update a record by using the primary key.
    path(
        "<int:pk>/delete/", SnackDeleteView.as_view(), name="snack_delete"
    ),  # HTTP DELETE; pk/DELETE
]
