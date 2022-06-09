from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest = Post.objects.order_by("-pub_date")[:10]
    return render(request, "posts/index.html", {"posts": latest})


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {'group': group, 'posts': posts}
    return render(request, template, context)


def group_index(request):
    groups = Group.objects.all()
    return render(request, 'posts/group_index.html', {'groups': groups})