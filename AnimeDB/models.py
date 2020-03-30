from django.db import models
from django.core import validators
# Create your models here.
class Item(models.Model):
    TYPE_CHOICES = (
        (1, 'TVアニメ'),
        (2, '劇場アニメ'),
    )
    MEDIA_CHOICES = (
        (1, 'BD'),
        (2, 'DVD'),
        (3, 'BD/DVD両方')
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=250,
    )
    place = models.CharField(
        verbose_name='保管場所',
        max_length=250,
    )
    type = models.IntegerField(
        verbose_name='TV/映画',
        choices=TYPE_CHOICES,
        default=1,
    )
    media = models.IntegerField(
        verbose_name='メディア形式',
        choices=MEDIA_CHOICES,
        default=1,
    )
    year = models.IntegerField(
        verbose_name='制作年',
        validators=[validators.MinValueValidator(1963)],
        blank=True,
        null=True,
    )
    epsode_number = models.IntegerField(
        verbose_name='話数',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    media_number = models.IntegerField(
        verbose_name='巻数',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    production = models.CharField(
        verbose_name='制作会社',
        max_length=250,
        blank=True,
        null=True,
    )
    voiceactor = models.CharField(
        verbose_name='主演声優',
        max_length=250,
        blank=True,
        null=True,
    )
    director = models.CharField(
        verbose_name='監督',
        max_length=200,
        blank=True,
        null=True,
    )
    memo =models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True,
        blank=True,
        null=True,
    )

    # 以下は管理サイト上の表示設定
    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
