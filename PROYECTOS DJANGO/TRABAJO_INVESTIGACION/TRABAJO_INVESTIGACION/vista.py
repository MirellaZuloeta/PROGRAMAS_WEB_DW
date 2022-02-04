from urllib.request import Request
from django.http import HttpResponse, request
from django.template import Template,Context
from django.shortcuts import render
import speech_recognition as sr
from textblob import TextBlob
import Prueba


def saludo(request):
     return HttpResponse('PRUEBA')


def voz_texto(request):

     if 'envia' in request.POST:
          r = sr.Recognizer()  
          with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source)
               audio = r.listen(source) 
               try:
                         text = r.recognize_google(audio, language="es-ES")
                         valor='Mirella dijo: {}'.format(text)
                         #etiqueta = '<%s><%s><%s>' % ('p',valor,'p')
               except:
                         valor='Lo siento, no te escucho' 
               contexto={
                    "valor":valor,
               }
          return render(request,"prueba.html",contexto)


     elif 'alexa' in request.POST:
          valor=Prueba.run_alexa()
          contexto={
                    "voz":valor,
          }
          return render(request,"prueba.html",contexto)

     else:
          contexto={
               "valor":'Buenas Días con Todos',
          }
          return render(request,"prueba.html",contexto)



