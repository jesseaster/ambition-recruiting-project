from rest_framework.routers import DefaultRouter

from recruiting_project.encounters.api import StarshipsModelViewSet, EncountersModelViewSet


router = DefaultRouter()
router.register(r'starships', StarshipsModelViewSet, basename='starships')
router.register(r'encounters', EncountersModelViewSet, basename='encounters')
urlpatterns = router.urls
