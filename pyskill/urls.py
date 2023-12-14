from django.urls import path

from pyskill.apps import PyskillConfig
from pyskill.views import IndexView, ShowSkills, DispatchCreateView, DispatchUpdateView

app_name = PyskillConfig.name


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("skills/", ShowSkills.as_view(), name="show_skills"),
    path("dispatch/create", DispatchCreateView.as_view(), name="dispatch_create"),
    path(
        "dispatch/<int:pk>/update/",
        DispatchUpdateView.as_view(),
        name="dispatch_update",
    ),
]
