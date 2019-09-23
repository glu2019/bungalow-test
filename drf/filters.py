import django_filters
from drf import models

class BungalowFilter(django_filters.FilterSet):

    last_sold_date = django_filters.DateFromToRangeFilter()
    rentzestimate_last_updated = django_filters.DateFromToRangeFilter()
    zestimate_last_updated = django_filters.DateFromToRangeFilter()
    
    ordering = django_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('area_unit', 'area_unit'),
            ('bathrooms', 'bathrooms'),
            ('bedrooms', 'bedrooms'),
            ('home_size', 'home_size'),
            ('home_type', 'home_type'),
            ('last_sold_date', 'last_sold_date'),
            ('last_sold_price', 'last_sold_price'),
            ('link', 'link'),
            ('price', 'price'),
            ('property_size', 'property_size'),
            ('rent_price', 'rent_price'),
            ('rentzestimate_amount', 'rentzestimate_amount'),
            ('rentzestimate_last_updated', 'rentzestimate_last_update'),
            ('tax_value', 'tax_value'),
            ('tax_year', 'tax_year'),
            ('year_built', 'year_built'),
            ('zestimate_amount', 'zestimate_amount'),
            ('zestimate_last_updated', 'zestimate_last_update'),
            ('zillow_id', 'zillow_id'),
            ('address', 'address'),
            ('city', 'city'),
            ('state', 'state'),
            ('zipcode', 'zipcode'),
        )
    )

    class Meta:
        model = models.Bungalow
        fields = {
            'id': ['exact'],
            'area_unit': ['exact'],
            'bathrooms': ['lt','exact', 'gt'],
            'bedrooms': ['lt','exact', 'gt'],
            'home_size': ['lt','exact', 'gt'],
            'home_type': ['exact'],
            'last_sold_price': ['lt','exact', 'gt'],
            'link': ['icontains'],
            'price': ['icontains'],
            'property_size': ['lt','exact', 'gt'],
            'rent_price': ['lt','exact', 'gt'],
            'rentzestimate_amount': ['lt','exact', 'gt'],
            'tax_value': ['lt','exact', 'gt'],
            'tax_year': ['lt','exact', 'gt'],
            'year_built': ['lt','exact', 'gt'],
            'zestimate_amount': ['lt','exact', 'gt'],
            'zillow_id': ['exact'],
            'address': ['icontains'],
            'city': ['exact'],
            'state': ['exact'],
            'zipcode': ['exact'],
        }