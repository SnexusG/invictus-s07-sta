from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import CustomUser, Post, Comment
from django.contrib.postgres.search import SearchVector
from chat.models import Thread


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = CustomUser
    context_object_name = 'customUser'  

class updateUserDetailView(UpdateView):
    template_name = 'user_detail_update.html'
    model = CustomUser
    fields = ['username', 'age', 'name', 'gender',  'email', 'isExpert', 'documents_link']
    success_url = reverse_lazy('home')


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'home.html'


class PostCreateView(View):
    form_class = PostForm
    template_name = 'postCreate.html'
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            post = Post(authorID=request.user, title=title, body=body)
            post.save()
            return redirect('/')
        return render(request, self.template_name, {'form' : form})
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

def postDetailView(request, *args, **kwargs):
    global post, comment
    if request.method == "GET":
        template_name = 'post_details.html'
        form = CommentForm()
        post = Post.objects.get(pk = kwargs['pk'])
        comment = Comment.objects.filter(postID = post)
        return render(request, template_name, {'post':post, 'comments':comment, 'form':form})   

    if request.method == "POST":
        template_name = 'post_details.html'
        form = CommentForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            authorID = request.user
            postID = post
            comment = Comment(authorID=authorID, postID=postID, body=body)
            comment.save()
            comments = Comment.objects.filter(postID = post)
            form = CommentForm()
            return render(request, template_name, {'post' : post, 'comments' : comments, 'form' : form})
        return HttpResponse('Failed')
        


class SearchView(ListView):
    def get(self, request, *args, **kwargs):
        query = request.GET['search']
        results = Post.objects.annotate(search=SearchVector('title', 'body'),).filter(search=query)
        return render(request, 'search_post.html', {'results': results, 'query' : query}, )

def searchDoctorView(request):
    template_name = 'search_doctor.html'
    if request.method == 'GET':
        users = CustomUser.objects.filter(isExpert=True, isVerified=True)
        return render(request, template_name, {'users' : users})

def makeThreadView(request, *args, **kwargs):
    if request.method == 'GET':
        doctor = CustomUser.objects.filter(pk=kwargs['pk'])[0]
        user = request.user
        threads = Thread.objects.filter()
        for t in threads:
            if (t.first_person == user and t.second_person == doctor) or (t.first_person == doctor and t.second_person == user):
                 return redirect('/chat')
        thread = Thread(first_person=user, second_person=doctor)
        thread.save()
        return redirect('/chat')
    else:
        return HttpResponse("OK")
