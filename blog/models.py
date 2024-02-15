from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='заголовок'
    )
    text = models.TextField(
        verbose_name='текст'
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата создания'
    )
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='дата публикации'
    )

    def publish(self) -> None:
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(
        max_length=200,
        verbose_name='автор'
    )
    text = models.TextField(
        verbose_name='комментарий'
    )
    created_date = models.DateTimeField(
        default=timezone.now(),
        verbose_name='дата создания'
    )
    approved_comment = models.BooleanField(
        default=False
    )

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
