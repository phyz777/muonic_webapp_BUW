from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]