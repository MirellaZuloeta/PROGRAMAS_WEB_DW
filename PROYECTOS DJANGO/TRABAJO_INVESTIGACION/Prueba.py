from textblob import TextBlob
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
#import pyjokes
import subprocess as sub

escuchador=sr.Recognizer()
myarray=[]

def talk(text):
    voice=pyttsx3.init()
    voices=voice.getProperty('voices')
    voice.setProperty('voice',voices[0].id)
    voice.setProperty('rate',140)
    voice.say(text)
    voice.runAndWait()

def take_comando():
    try:
        with sr.Microphone() as source:
            #print('Escuchando...')
            myarray.append('Escuchando...')
            voice = escuchador.listen(source)
            comando = escuchador.recognize_google(voice, language='es-PE')
            comando = comando.lower() 
            if 'alexa' in comando:               
                myarray.append(comando.upper())
                comando = comando.replace('alexa', '')               
                #print(comando)

    except:
        talk('Intenta denuevo porfavor')
    return comando


def run_alexa():
    myarray.clear()
    comando = take_comando()
    #print(comando)
        
    if 'abre' in comando:
            sites={
                'google':'google.com',
                'youtube':'youtube.com',
                'instagram':'instagram.com',
                'usat':'https://intranet.usat.edu.pe/campusestudiante/Default.aspx',
                'peli':'cuevana3.io'
            }

            for i in list(sites.keys()):
                if i in comando:
                    sub.call(f'start opera.exe {sites[i]}', shell=True)
                    talk(f'Abriendo {i}')


    elif 'traducir' in comando:
        Texto = comando.replace('traducir', '')
        traduccion=TextBlob(Texto)
        idioma=traduccion.translate(to='en')
        talk(f'La traduccion es {idioma}')
        #print(f'La traduccion es {idioma}')
        myarray.append(f'La traduccion es {idioma}')

    elif 'reproducir' in comando:
        song = comando.replace('reproducir', '')
        talk('reproduciendo ' + song)
        pywhatkit.playonyt(song)
        
    elif 'buscar' in comando:
        busqueda = comando.replace('buscar', '')
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda) 

    elif 'escribe' in comando:
            texto = comando.replace('escribe', '')
            talk(texto)
            #print(texto)
            myarray.append(texto)
    elif 'mandar' in comando:
        try:
            mensaje = comando.replace('mandar', '')
            pywhatkit.sendwhatmsg("+51957355236",  
                        mensaje,  
                        14,28) 
            print("Envio Exitoso!") 
        
        except:
            print("Ha ocurrido un error!")

    elif 'tiempo' in comando:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('La hora es ' + time)

    elif 'wiki' in comando:
            objeto = comando.replace('wiki', '')
            info = wikipedia.set_lang("es")
            info = wikipedia.summary(objeto)    
            myarray.append(wikipedia.summary(objeto)  )
            #talk(info)
            
    elif 'cómo estás' in comando:
        talk('Bien gracias por preguntar')

    elif 'estás soltera' in comando:
        talk('No, estoy en una relación')

    else:
        talk('Intenta denuevo porfavor')
        
    #return 'Alexa '+ comando
    
    return myarray
    