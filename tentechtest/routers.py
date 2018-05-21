"""Router to connect urls across apps."""

from rest_framework import routers
from rest_framework.permissions import AllowAny


class APIRootView(routers.APIRootView):
    """Define specific permissions (AllowAny) for the API root view."""

    permission_classes = (AllowAny,)


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class.

    Use our custom APIRootView.
    Adds a method for extending url routes from another router.
    """

    APIRootView = APIRootView

    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)
