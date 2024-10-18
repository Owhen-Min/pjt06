from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Board, Comment
from .forms import BoardForm, CommentForm
# Create your views here.

@require_http_methods(['GET'])
def index(request):
    boards = Board.objects.all()
    context = {
        'boards' : boards
    }
    return render (request, 'boards/index.html', context)

# @login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.mothod == 'GET':
        form = BoardForm()
    context = {
        'form' : form
    }
    return render(request, 'boards/create.html', context)