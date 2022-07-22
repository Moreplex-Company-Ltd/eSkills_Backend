from rest_framework import routers
from lessons.views import CategoriesViewSet, CourseViewSet, ModulesViewSet, User_InterestViewSet, Lesson_ResourcesViewSet, LessonsViewSet

router = routers.SimpleRouter()
router.register(r'categories', CategoriesViewSet)
router.register(r'course', CourseViewSet)
router.register(r'modules', ModulesViewSet)
router.register(r'interest', User_InterestViewSet)
router.register(r'lessin-resources', Lesson_ResourcesViewSet)
router.register(r'modules', LessonsViewSet)
urlpatterns = router.urls