from rest_framework import serializers

from .models import Category

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ReadCategorySerializer(serializers.ModelSerializer):
    parents = serializers.SerializerMethodField()

    def get_parents(self, obj):
        if obj.parent:
            qs = Category.objects.filter(pk=obj.parent.pk)
        else:
            qs = Category.objects.none()
        serializer = SubCategorySerializer(qs, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name',  'parents')