from rest_framework import mixins, viewsets


class FollowMixin(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    pass
