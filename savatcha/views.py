from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

from savatcha.models import Mahsulot, Savat
from savatcha.serializers import SavatSerializer, MahsulotSerializer


class SavatViewSet(viewsets.ModelViewSet):
    queryset = Savat.objects.all()
    serializer_class = SavatSerializer

    @action(detail=True, methods=['post'])
    def add_to_savat(self, request, pk=None):
        try:
            mahsulot_id = request.data.get('mahsulot')  # Request'dan mahsulot ID'sini olish
            miqdor = request.data.get('miqdor', 1)  # Default qiymatni 1 qilib belgilash

            # Mahsulotni olish
            mahsulot = Mahsulot.objects.get(pk=mahsulot_id)

            # Savatni yaratish yoki mavjudini olish
            savat, created = Savat.objects.get_or_create(mahsulot=mahsulot, defaults={'miqdor': miqdor})

            if not created:  # Agar savat oldin mavjud bo'lsa, miqdorni yangilaymiz
                savat.miqdor += int(miqdor)
                savat.save()

            # Mahsulot ID va miqdorni qaytarish
            return Response({'mahsulot': savat.mahsulot.id, 'miqdor': savat.miqdor}, status=status.HTTP_200_OK)
        except Mahsulot.DoesNotExist:
            return Response({'error': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)


class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
