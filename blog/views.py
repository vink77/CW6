# Create your views here.
from django.urls import reverse_lazy, reverse

from blog.models import Blog
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'conteхt')
    success_url = reverse_lazy('blog:list')



class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'conteхt')
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    context_object_name = 'object_list'

    def get_queryset(self):
       return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
