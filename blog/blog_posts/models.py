from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок поста', blank=True, default='', max_length=150)
    description = models.TextField('Текст поста', blank=True, default='')
    author = models.CharField('Имя автора', max_length=100)
    post_date = models.DateField('Дата создания поста', auto_now_add=True)
    img = models.ImageField('Изображение', upload_to='image/%Y', default='image/default.jpg')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['post_date']


class Comments(models.Model):
    user_email = models.EmailField()
    user_name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=200)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


