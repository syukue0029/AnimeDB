
from django_filters import filters
from django_filters import FilterSet
from .models import Item

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class ItemFilter(FilterSet):

    title = filters.CharFilter(label='タイトル', lookup_expr='contains')
    place = filters.CharFilter(label='保管場所', lookup_expr='contains')
    production = filters.CharFilter(label='制作会社', lookup_expr='contains')
    voiceactor = filters.CharFilter(label='声優', lookup_expr='contains')
    director = filters.CharFilter(label='監督', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'title'),
            ('year', 'year'),
        ),
        field_labels={
            'title': 'タイトル名順',
            'year': '制作年代順',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('title','place','production','voiceactor','director','memo')
