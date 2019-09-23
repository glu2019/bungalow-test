from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from drf import views

router = routers.SimpleRouter()
router.register(r'bungalow', views.BungalowViewSet)

urlpatterns = format_suffix_patterns([
    url(r'', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title="Bungalow Rest APIs")),
])
urlpatterns += router.urls