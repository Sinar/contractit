from releases.models import *
from hvad.contrib.restframework import TranslatableModelSerializer


class OrganizationSerializer(TranslatableModelSerializer):
    class Meta:
        model = Organization
        extra_kwargs = {'id':{'read_only':False, 'required':False}}
        fields = ['name', 'streetAddress', 'locality', 'region', 'postalCode', 
                'countryName', 'details']
