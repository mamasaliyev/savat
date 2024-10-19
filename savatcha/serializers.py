from rest_framework import serializers
from .models import Mahsulot, Savat

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = ['id' ,'title', 'description', 'price', 'image', 'quantity']



class SavatSerializer(serializers.ModelSerializer):
    mahsulot = serializers.PrimaryKeyRelatedField(queryset=Mahsulot.objects.all())
    mahsulot_title = serializers.CharField(source='mahsulot.title', read_only=True)

    class Meta:
        model = Savat
        fields = ['id', 'mahsulot', 'mahsulot_title', 'miqdor']


