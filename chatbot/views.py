from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Create your views here.
#iBot = ChatBot('iCloseBot')
chatbot = ChatBot("webmind-chatBot")

dataReply = []
def index(request):
    #return render(request,'home.html')
    template = loader.get_template('chatbot.html')
    dataReply.clear()
    data = {'chatbot'}
    value ={
            'data':data
        }
    return HttpResponse(template.render(value,request))

import re
def trainChatBot(request):
    dataReply.clear()
    train_data = []
    #chatbot.storage.drop()
    trainDataPath = "E:\Brajendra\Python-Projects\DjangoProject\iCloseChatBot\data\english/"
    chatbot.set_trainer(ListTrainer)
    for files in os.listdir(trainDataPath):
        data = open(trainDataPath + files,'r')
        for line in data:
            m = re.search('(Q:|A:)?(.+)', line)
            if m:
                train_data.append(m.groups()[1])
        chatbot.train(train_data)
    data = {
            'chatbotData': "Data trained!!"
            }
    return JsonResponse(data)
"""This below function will call when you click Send button for chatting"""
def letsChat(request):
    while True:
        #message = input('You:')
        dataReply.clear()
        message = request.GET.get('userData', None)
        dataReply.append("You- " + str( message))
        if message.lower().strip() !='Bye'.lower():
            reply = chatbot.get_response(message)
            dataReply.append("Bot- " + str(reply))
        if message.lower().strip()=='Bye'.lower():
            break
        return render(request, 'iCloseChatBotMsg.html', {'data':dataReply})