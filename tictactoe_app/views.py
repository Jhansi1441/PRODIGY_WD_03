# tictactoe/views.py
from django.shortcuts import render

def tictactoe_game(request):
    return render(request, 'index.html')
