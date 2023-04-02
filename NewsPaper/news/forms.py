from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='подтвердить')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'author_post', 'post_news', 'check_box']
        # не забываем включить галочку в поля, иначе она не будет показываться на странице!