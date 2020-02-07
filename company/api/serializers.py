from rest_framework.serializers import ModelSerializer, SerializerMethodField
from company.models import Company, Partners
from profiles.api.serializers import UserDetailSerializer
from profiles.models import UserProfile


class CompanySerializer(ModelSerializer):
    partners = SerializerMethodField()

    def get_partners(self, obj):
        return PartnerSerializer(Partners.objects.filter(company=obj), many=True).data

    class Meta:
        model = Company
        fields = [
            'name',
            'slug',
            'joined_date',
            'field',
            'partners',
        ]

        read_only_fields = ['slug', ]


class PartnerSerializer(ModelSerializer):
    partner = SerializerMethodField()

    def get_partner(self, obj):
        return str(obj.partner.username)

    class Meta:
        model = Partners
        fields = [
            'partner',
        ]


class CompanyUpdateSerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

        read_only_fields = ['slug', ]
