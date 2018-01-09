from django.shortcuts import render, redirect, HttpResponse
from firstapp.models import Article, Comment, Ticket
from firstapp.forms import CommentForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login  # authenticate,
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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
    # 获取传入page_num的文章
    article = Article.objects.get(id=page_num)
    if isinstance(request.user, User):
        voter_id = request.user.profile.id
        # 此处id 为投票人id是django在创建用户是自动生成的,
        # voter_id为获取投票用户
        # like_counts获取此文章点赞数
        like_counts = Ticket.objects.filter(
            choice='like', video_id=page_num).count()
        context['like_counts'] = like_counts
        try:
            user_ticket_for_this_article = Ticket.objects.get(
                voter_id=voter_id, video_id=page_num)
            context['user_ticket'] = user_ticket_for_this_article
        except:
            pass
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    context['article'] = article
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'detail.html', context)


def detail_vote(request, page_num):
    if not isinstance(request.user, User):
        return redirect(to='detail', page_num=page_num)

    voter_id = request.user.profile.id
    try:
        user_ticket_for_this_video = Ticket.objects.get(
            voter_id=voter_id, video_id=page_num)
        user_ticket_for_this_video.choice = request.POST['vote']
        user_ticket_for_this_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(
            voter_id=voter_id, video_id=page_num, choice=request.POST['vote'])
        new_ticket.save()
    if request.POST["vote"] == "like":
        article = Article.objects.get(id=page_num)
        article.favs += 1
        article.save()
    return redirect(to='detail', page_num=page_num)


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
