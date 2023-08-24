from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('название', max_length=100)
    desc = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=3)
    auction = models.BooleanField('торг', help_text='укажите если возможен торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time

            )
        return self.create_at.strftime('%d.%m.%Y')

    @admin.display(description='Дата обновления')
    def created_update(self):
        if self.update_at.date() == timezone.now().date():
            created_up = self.create_models.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_up

            )
        return self.update_at.strftime('%d.%m.%Y')
    @admin.display(description='Изображение')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src"{url}" style="max-width: 80px; max-height: 80px;">', url=self.image.url
            )
    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    class Meta:
        db_table = "advertisements"