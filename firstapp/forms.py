from django import forms
from django.core.validators import ValidationError


def words(comment):
    if len(comment) < 4:
        raise ValidationError('not ength words')


def keys_words(comment):
    keys = ['钱', '发票']
    for key in keys:
        if key in comment:
            raise ValidationError(
                'Your comment contains invalid words,please check it again.')


class CommentForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(
        widget=forms.Textarea(),
        validators=[words, keys_words],
    )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
