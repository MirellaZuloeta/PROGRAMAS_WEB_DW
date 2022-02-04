from tkinter import *
from gtts import gTTS
from playsound import playsound
from os import remove
import speech_recognition as sr

def voz_texto():
     r = sr.Recognizer() 
 
     with sr.Microphone() as source:
          print('Speak Anything : ')
          # r.adjust_for_ambient_noise(source)
          audio = r.listen(source)
     
          try:
               text = r.recognize_google(audio, language="es-ES")
               valor='Mirella dijo: {}'.format(text)
          except:
               print('Sorry could not hear')
          Label(root,text=valor,font=("Derive Unicode",20),bg="white smoke").place(x=20,y=150)

def salir():
     root.destroy()

def borrar():
     Msg.set("")

root = Tk()

root.geometry("950x550")

root.configure(bg="black")
root.title("CONVERTIDOR DE TEXTO A VOZ")


Label(root,text="Texto a voz", font=("Derive Unicode",25), bg="white smoke").pack()
Label(root,text="SIZ-0", font=("Arial",20), bg="white smoke").pack(side=BOTTOM)

#Label(root,text="Ingresar Texto",font=("Derive Unicode",20),bg="white smoke").place(x=20,y=150)

Msg=StringVar()
#entry_field=Entry(root,textvariable=Msg,width="65")
#entry_field.place(x=20,y=235,height=30)

Button(root,text="PLAY",font=("Derive Unicode",25),command=voz_texto).place(x=25,y=325)
Button(root,text="EXIT",font=("Derive Unicode",25),command=salir,bg="Orange").place(x=165,y=325)
Button(root,text="RESET",font=("Derive Unicode",25),command=borrar).place(x=300,y=325)


root.mainloop()
