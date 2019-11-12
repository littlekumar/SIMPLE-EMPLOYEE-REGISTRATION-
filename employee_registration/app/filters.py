import django_filters

from app.models import Employee_Personal_Information


class PersonFilter(django_filters.FilterSet):
    lastName = django_filters.CharFilter(lookup_expr='icontains')
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee_Personal_Information
        fields = ['lastName', 'firstName']