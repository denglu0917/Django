from django.shortcuts import render, redirect, HttpResponse
from firstapp.models import Article, Comment
from firstapp.forms import CommentForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login  # authenticate,
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


# 使用django自带的登陆注册
def index_login(request):
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='index')
    context = {}
    context['form'] = form
    return render(request, 'login.html', context)


def index_register(request):
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')  # 注册后跳转到登陆
    context = {}
    context['form'] = form
    return render(request, 'register.html', context)


# 通过自己写的用户登陆
# def index_login(request):
#     if request.method == 'GET':
#         form = LoginForm
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect(to='index')
#             else:
#                 return HttpResponse('<h1>Not A User<h1>')
#     context = {}
#     context['form'] = form
#     return render(request, 'login.html', context)


def index(request, cate=None):
    context = {}
    if cate is None:
        article_list = Article.objects.all()
    if cate == 'editors':
        article_list = Article.objects.filter(editors_choice=True)
    else:
        article_list = Article.objects.all()
    page_robot = Paginator(article_list, 3)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    context['article_list'] = article_list
    return render(request, 'index.html', context)


def detail(request, page_num, error_form=None):
    form = CommentForm
    context = {}
    article = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    context['article'] = article
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'detail.html', context)


def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        article = Article.objects.get(id=page_num)
        Comment(name=name, content=comment, belong_to=article).save()
    else:
        return detail(request, page_num, error_form=form)
    return redirect(to='detail', page_num=page_num)
