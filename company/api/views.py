from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from company.models import Company
from .serializers import CompanySerializer, CompanyUpdateSerializer


class CompanyDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    class Meta:
        model = Company


class CompanyUpdateAPIView(UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()

    class Meta:
        model = Company
