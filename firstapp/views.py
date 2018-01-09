from django.shortcuts import render, redirect
from firstapp.models import Article, Comment
from firstapp.forms import CommentForm

# Create your views here.


def index(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    return render(request, 'index.html', context)


# def detail(request, page_num):
#     if request.method == 'GET':
#         form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             article = Article.objects.get(id=page_num)
#             Comment(name=name, content=comment, belong_to=article).save()
#             return redirect(to='detail', page_num=page_num)
#     context = {}
#     article = Article.objects.get(id=page_num)
#     best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     context['article'] = article
#     context['form'] = form
#     return render(request, 'detail.html', context)


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
