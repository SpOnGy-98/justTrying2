from django.shortcuts import render, redirect
from . import models
from . import forms
def index(request):
    comments = models.Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'product1/indexdown.html', context)


def sign(request):
    if request.method == 'POST':
        form = forms.CommentForms(request.POST)

        if form.is_valid():
            new_comment = models.Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('indexPage')

    else:
        form = forms.CommentForms()

    context = {'form':form}
    return render(request, 'product1/signdown.html', context)