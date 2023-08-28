import django_filters
from .models import Memberdata as Member

class MemberFilter(django_filters.FilterSet)

    class Meta:
        model = Member
        fields = ('region', 'membergroup')