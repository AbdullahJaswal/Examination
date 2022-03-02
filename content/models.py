from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=False)

    sub_topics = models.ManyToManyField('SubTopic', blank=True)

    is_active = models.BooleanField(default=False, blank=False)

    order = models.IntegerField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

        ordering = ('order',)

    def __str__(self):
        return str(self.name)


class SubTopic(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=255, blank=False)

    questions = models.ManyToManyField('Question', blank=True)

    is_active = models.BooleanField(default=False, blank=False)

    order = models.IntegerField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'SubTopic'
        verbose_name_plural = 'SubTopics'

        ordering = ('order',)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    content = models.TextField(blank=False)
    explanation = models.TextField(blank=False)

    answers = models.ManyToManyField('Answer', blank=True)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

        ordering = ('id',)

    def __str__(self):
        return str(self.content)


class Answer(models.Model):
    content = models.TextField(blank=False)
    is_correct = models.BooleanField(default=False, blank=False)

    is_active = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

        ordering = ('id',)

    def __str__(self):
        return str(self.content)
