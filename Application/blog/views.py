from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import Post, Comment

from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView, View

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from .models import Comment

from .forms import CommentFrom

# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']

class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'


   
###########

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    ## success_url = 'index'

    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    ## success_url = 'index'

    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False




# def index(request):
#     #return HttpResponse("Hello World!!")
#     context = {
#         'articles': Post.objects.all(),
#         # 'comment': Comment.objects.all()
#     }

#     return render(request, 'index.html', context)


class CommentView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs): 
        try:
            form = CommentFrom(request.POST)
            print(form.is_valid())
            if form.is_valid():
                p = Post.objects.get(id = self.kwargs.get('pk')) 
                comment = Comment.objects.create(cmt_post=p, cmt_user=request.user, comment=form.cleaned_data['comment'])
                print(comment) 
                instance_obj = {
                    'user': request.user.username, 
                    'comment': form.cleaned_data['comment'],
                }
                print(instance_obj)
                return JsonResponse({'status': 200, 'instance': instance_obj})
            else:
                errors = [(index, value[0]) for index,value in form.errors.items()]
                print(errors)
                return JsonResponse({'status': 400, 'errors': errors})

        except Post.DoesNotExist as e:
            print(e)


