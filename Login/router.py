from rest_framework.routers import DefaultRouter
from . import (Viewset)

router = DefaultRouter()
router.register('api/user', Viewset.UserAPI)
