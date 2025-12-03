from rest_framework import serializers
from .models import Category, Product

#Defina serializers para Category e Product.
#O serializador de Product deve exibir o nome da categoria, não apenas seu ID.
#Use ViewSets para fornercer funcionalidade CRUD completa para Category e Product.
#Configure urls usando DefaultRouter do DRF para registrar os ViewSets.

class CategorySerializer(serializers.ModelSerializers):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category', read_only=True)      
    category_id = serializers.PrimaryKeyRelatedField( queryset=Category.objects.all(), source='category', 
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']