from content.models import Topic

from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    order = models.IntegerField(unique=True, blank=False)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        ordering = ("order",)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    order = models.IntegerField(unique=True, blank=False)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

        ordering = ("order",)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    TYPE_CHOICES = (
        ('C', 'Course'),
        ('B', 'Book'),
        ('MT', 'Mock Test'),
        ('O', 'Other')
    )

    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='O', blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(unique=True, max_length=255, blank=False)

    value = models.FloatField(default=0.0, blank=False)
    discount = models.FloatField(default=0.0, blank=False)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=False)

    topics = models.ManyToManyField(Topic, blank=True)

    is_paid = models.BooleanField(default=False, blank=False)
    is_active = models.BooleanField(default=False, blank=False)

    meta_tag = models.CharField(max_length=2000, blank=True)
    meta_description = models.CharField(max_length=2000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Product"
        verbose_name_plural = "User Products"

        ordering = ("-id",)

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.user.username)
