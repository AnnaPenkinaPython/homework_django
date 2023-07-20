from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {
        "title": "Новости дня"
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

    def get_object(self, queryset=None):
        object_item = super().get_object(queryset)
        object_item.increase_count_of_view()
        object_item.save()
        return object_item


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Blog
    fields = ('title', 'content', 'image', 'create_date')
    blogs = Blog.objects.all()
    for blog in blogs:
        blog.save()
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.add_blog'


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'create_date')
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.delete_blog'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset