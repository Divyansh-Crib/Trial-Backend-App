from rest_framework import serializers
from . models import biller

class billerSerializers(serializers.ModelSerializer):
    class Meta:
        model=biller
        fields='__all__'

class billerSerializers2(serializers.ModelSerializer):
    class Meta:
        model=biller
        fields=('item_id','item_name')
class billerSerializers3(serializers.ModelSerializer):
    class Meta:
        model=biller
        fields=fields=('item_id','item_category')
class billerSerializers4(serializers.ModelSerializer):
    class Meta:
        model=biller
        fields=fields=('item_id','item_subcategory')

