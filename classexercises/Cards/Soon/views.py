from django.shortcuts import render, get_object_or_404

from django.template.defaultfilters import slugify
from .models import Post

from .forms import PostForm
from taggit.models import Tag

def home_view(request):
    posts = Post.objects.order_by('-published')
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()

        context = {
            'posts' : posts,
            'common_tags' : common_tags,
            'form' : form,

        }
        return render(request, 'home.html', context)

    def detail_view(request, slug):
        post = get_object_or_404(post, slug=slug)
        return render(request, 'detail.html', {'post' : post})

    def tagged(request,slug):
        tag = get_object_or_404(Tag, slug=slug)

        posts = Post.objects.filter(tags=tag)
        context = {
            'tag' : tag,
            'posts' : posts,
        }
        return render(request, 'home.html', context)

# names = ["Smart", "Ayo", "Bimpe"]
# touch = names[0]
# touch1 = names[1]
# touch2 = names[2]


# # Create your views here.
# def names(request):
#     return render(request, 'Soon/name.html', {
#         'ans' : touch,
#         'ans1' : touch1,
#         'ans2' : touch2
#     })
