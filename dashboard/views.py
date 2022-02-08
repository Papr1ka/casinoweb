from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from markdown import markdown
from .forms import PostForm
from .models import Post
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q

kwargs = {
    'app_name': "Casino"
}
POSTS_PER_PAGE = 10


def superuser_required(func):
    def wrapper(*args, **kwargs):
        if args[1].user.is_superuser:
            return func(*args, **kwargs)
        else:
            raise PermissionDenied()
    return wrapper

# Create your views here.
def posts(request):
    search_query = request.GET.get('search', '')
    if search_query:
        search_query = search_query.lower()
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    p = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page = p.get_page(page_number)
    
    page_nums = [p.page_range[0]]
    j = 0
    for i in range(page.number - 3 if page.number - 3 >= p.page_range[0] else p.page_range[0], page.number):
        if j < 3:
            if i == p.page_range[0] or i == p.page_range[-1]:
                continue
            page_nums.append(i)
        else:
            break
        j += 1
    j = 0
    for i in range(page.number, p.page_range[-1]):
        if j < 4:
            if i == p.page_range[0] or i == p.page_range[-1]:
                continue
            page_nums.append(i)
        else:
            break
        j += 1
    
    prev_url = f'?page={page.previous_page_number()}' if page.has_previous() else ''
    next_url = f'?page={page.next_page_number()}' if page.has_next() else ''
    is_paginated = page.has_other_pages()
    
    page_nums.append(p.page_range[-1])
    print(page_nums)
    
    return render(request, 'dashboard/main.html', context={**kwargs, 'page_obj': page, 'page_numbers': page_nums, 'prev_url': prev_url, 'next_url': next_url, 'is_paginated': is_paginated})

class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'dashboard/post_detail.html', context={'post': post, **kwargs, 'admin_object': post, 'detail': True})

class PostCreate(View):
    @superuser_required
    def get(self, request):
        form = PostForm()
        return render(request, 'dashboard/post_create.html', context={'form': form, **kwargs})
    
    @superuser_required
    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, 'dashboard/post_create.html', context={'form': bound_form})

class PostUpdate(View):
    @superuser_required
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'dashboard/post_update.html', context={'form': bound_form, 'post': post})

    @superuser_required
    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'dashboard/post_update.html', context={'form': bound_form, 'post': post})

class PostDelete(View):
    @superuser_required
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'dashboard/post_delete.html', context={'post': post})

    @superuser_required
    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('post_list_url'))

class PrivacyPolicy(View):
    def get(self, request):
        return render(request, 'dashboard/privacy_policy.html')

class TermsOfUse(View):
    def get(self, request):
        return render(request, 'dashboard/terms_of_use.html')

class Commands(View):
    def get(self, request):
        return render(request, 'dashboard/commands.html')
    