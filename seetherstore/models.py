from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    child_category = models.BooleanField(default=False)
    """parent_category = models.ForeignKey(
        'self', related_name='sub_categories',
        on_delete=models.SET_NULL, null=True, blank=True,
    )"""

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='products_sub_category', on_delete=models.CASCADE,
                                     null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    has_attributes = models.BooleanField(default=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

        def __str__(self):
            return self.name

        def __str__(self):
            return self.sub_category
