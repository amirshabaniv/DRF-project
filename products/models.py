from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Representation(models.Model):
    REPRESENTATION_TYPE = (
        ('رسمی', 'رسمی'),
        ('عاملیت فروش', 'عاملیت فروش')
    )
    name = models.CharField(max_length=150)
    manager = models.CharField(max_length=150)
    representation_type = models.CharField(choices=REPRESENTATION_TYPE, max_length=35)
    sales_representative = models.BooleanField(default=False)
    service_representative = models.BooleanField(default=False)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING, related_name='representations')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='representations')
    address = models.TextField()

    def __str__(self):
        return f'{self.name} managed by {self.manager}'
    

class Category(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name    
    

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=350)
    available = models.BooleanField(default=True)
    warranty_validity = models.BooleanField()
    representation = models.ForeignKey(Representation, on_delete=models.DO_NOTHING, related_name='products')
    specifications = models.TextField()
    guide = models.FileField(upload_to='files/products_guides')
    educational_film = models.FileField(upload_to='files/products_films')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    views_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/product_images', null=True, blank=True)

    def __str__(self):
        return self.name


class ProImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/product_images', null=True, blank=True)

    def __str__(self):
        return self.product


class CreateRepresentation(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    national_code = models.CharField(max_length=40)
    email = models.EmailField()
    place_of_birth = models.CharField(max_length=50)
    date_of_birthday = models.DateField()
    province = models.OneToOneField(Province, on_delete=models.CASCADE)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.family} requested representation'