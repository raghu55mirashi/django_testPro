from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import NewsView


router = SimpleRouter()
router.register('News', NewsView)

urlpatterns = router.urls

urlpatterns = [
    path(r'^api/', include(router.urls, namespace='api')),
]


