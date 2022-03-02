from product.models import UserProduct
from content.models import Question, Answer

from django.db import models


# Create your models here.
class Quiz(models.Model):
    user_product = models.ForeignKey(UserProduct, on_delete=models.SET_NULL, null=True)

    submissions = models.ManyToManyField('Submission', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

        ordering = ('-id',)

    def __str__(self):
        return 'Quiz: {} - {}'.format(self.user_product.product.name, self.user_product.user.username)


class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

        ordering = ('-id',)
    
    def __str__(self):
        return 'Submission: {} - {}'.format(self.answer.is_correct, self.question.content)
