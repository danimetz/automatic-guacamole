from tastypie.resources import ModelResource
from api.models import Track
from api.models import User

class TrackResource(ModelResource):
    class Meta:
        queryset= Track.objects.all()
        resrouce_name = 'track'

class UserResource(ModelResource):
    class Meta:
        queryset= User.objects.all()
        resrouce_name = 'user'
