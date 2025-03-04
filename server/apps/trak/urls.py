from django.urls import include, path
from rest_framework import routers

from .views import (HandlerSearch, HandlerView, ManifestView, PullManifest,
                    RcraProfileView, SiteApi, SiteList, SiteManifest,
                    SyncProfile, SyncSiteManifest, TransporterView)
from .views.manifest import MtnList
from .views.rcra_profile import SitePermissionView

manifest_router = routers.SimpleRouter()
manifest_router.register(r'manifest', ManifestView)

urlpatterns = [
    # Rcra Profile
    path('profile/<str:user>/sync', SyncProfile.as_view()),
    path('profile/<str:user>', RcraProfileView.as_view()),
    path('permission/<int:pk>', SitePermissionView.as_view()),
    # Manifest
    path('', include(manifest_router.urls)),
    path('manifest/pull', PullManifest.as_view()),
    path('mtn', MtnList.as_view()),
    path('mtn/<str:epa_id>', MtnList.as_view()),
    # Site
    path('site/', SiteList.as_view()),
    path('site/<str:epa_id>', SiteApi.as_view()),
    path('site/<str:epa_id>/manifest', SiteManifest.as_view()),
    path('site/manifest/sync', SyncSiteManifest.as_view()),
    # Handler
    path('handler/search', HandlerSearch.as_view()),
    path('handler/details/<int:pk>', HandlerView.as_view()),
    path('transporter/<int:pk>', TransporterView.as_view()),
]
