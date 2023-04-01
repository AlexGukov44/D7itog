from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Category
from datetime import datetime
from .forms import PostForm
from .filter import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'news.html'
    context_object_name = 'post_news'
    paginate_by = 50  # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый пост
            form.save()

        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'onenews.html'
    context_object_name = 'onenews'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'post_add.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'post_edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'