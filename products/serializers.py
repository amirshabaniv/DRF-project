from rest_framework import serializers
from .models import Product, Category, Representation, CreateRepresentation, ProImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'available',
                  'warranty_validity', 'representation',
                  'specifications', 'guide', 'educational_film',
                  'category', 'views_count', 'images', 'uploaded_images']
        
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image = ProImage.objects.create(product=product, image=image)
        return product


class ProductForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'available', 'image1']


class CategorySeializer(serializers.ModelSerializer):
    products = ProductForCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class RepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Representation
        fields = ['id', 'name', 'manager', 'representation_type',
                  'sales_representative', 'service_representative',
                  'province', 'city', 'address']


class CreateRepresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreateRepresentation
        fields = ['id', 'name', 'family', 'national_code',
                  'email', 'place_of_birth', 'date_of_birthday',
                  'province', 'city', 'phone_number', 'whatsapp_number']


