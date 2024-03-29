from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO) 

def index(request):
    html = '''
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете информацию о моем первом Django-приложении.</p>
    <p>Автор: Виталий Масленников</p>
    '''
    logging.info('Посещение главной страницы')
    return HttpResponse(html)

def about(request):
    html = '''
    <h1>Обо мне</h1>
    <p>Здесь будет информация о мне и моих навыках.</p>
    <p>Автор: Виталий Масленников</p>
    '''
    logging.info('Посещение страницы "О себе"')
    return HttpResponse(html)


# Create your views here.
