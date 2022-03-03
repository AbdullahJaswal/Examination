from product.models import Product
from content.models import Question, Answer

from django.db import models
from django.conf import settings


# Create your models here.
class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    submissions = models.ManyToManyField('Submission', blank=True)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Product"
        verbose_name_plural = "User Products"

        ordering = ("-id",)

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.user.username)


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)

    is_correct = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

        ordering = ('-id',)
    
    def __str__(self):
        return 'Submission: {} - {}'.format(self.answer.is_correct, self.question.content)
