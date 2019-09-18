from rest_framework import serializers

from .models import Category

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CreateCategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)

    def get_fields(self):
        fields = super(CreateCategorySerializer, self).get_fields()
        fields['children'] = CreateCategorySerializer(many=True, required=False)
        return fields


    def create(self, validated_data):
        print(validated_data)
        print('!'*30)
        children = validated_data.pop('children', [])
        top_cat = super().create(validated_data)
        for child in children:
            child['parent'] = top_cat
            CreateCategorySerializer().create(child)
        return top_cat


    class Meta:
        model = Category
        fields = ('name', 'parent', 'children')


class ReadCategorySerializer(serializers.ModelSerializer):
    parents = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    def get_parents(self, obj):
        if obj.parent:
            qs = Category.objects.filter(pk=obj.parent.pk)
        else:
            qs = Category.objects.none()
        serializer = SubCategorySerializer(qs, many=True)
        return serializer.data


    def get_children(self, obj):
        children = obj.children.all()
        serializer = SubCategorySerializer(children, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name',  'parents', 'children')