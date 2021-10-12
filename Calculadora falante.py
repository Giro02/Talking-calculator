# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:54:09 2020

@author: Pedro
"""
import speech_recognition as reconhecimento
from gtts import gTTS
import os
import playsound

#Entrada de dados
voz = reconhecimento.Recognizer()

def falar(text):
    tts = gTTS(text=text, lang="pt-BR")
    filename = "primeiro.mp3"
    os.remove('primeiro.mp3')
    tts.save(filename)
    playsound.playsound(filename)
    


def reconhecer():
    with reconhecimento.Microphone() as source:
        audio = voz.listen(source,timeout=10)
    try:
        sp=voz.recognize_google(audio, language= 'pt-BR')
        s=int(sp)
        print("Você disse: ",s)
        return s
    except Exception as e:
        print(e)
        falar('Desculpe, não entendi. Poderia repetir?')
        print("Desculpe, não entendi. Poderia repetir?")
        return reconhecer()
    
    
falar("Olá, eu sou a calculadora falante e posso realizar calculos matemáticos simples")
falar("fui desenvolvida pelo Pedro Arendit")
falar("vou demonstrar o que posso fazer")

#Entrada de dados do usuário
flag = 1
while (flag == 1):
    with reconhecimento.Microphone() as source:
        print("Fale o primeiro número: ")
        falar("fale o primeiro número")
        num1 = reconhecer()
        
        print("Fale a operação matematica. mais '+', menos '-', dividido '/', vezes 'x'")
        falar("Fale a operação matemática. mais, menos, dividido ou vezes ")
        fun = voz.listen(source, timeout=5)
        fun1 = voz.recognize_google(fun, language= 'pt-BR')
        print("Você disse: ", fun1)
        

        print("Fale o segundo número: ")
        falar("Fale o segundo número: ")
        num2 = reconhecer()
        
#Processamento de dados
       
#Código para calculo de menos
        if (fun1 == "menos" or "enos"):
            menos = num1-num2
            file1 = open("myfile.txt", "a")
            file1.truncate (0)
            file1.write(str(menos))
            file1.close()   
            
            file2 = open("myfile.txt", "r").read().replace("\n", "")
            speech = gTTS(text = str(file2), lang="pt-BR",slow=False)
            os.remove('myfile.mp3')
            speech.save('myfile.mp3')
            falar("A sua subtração é: ")
            print("A sua subtração é: ", menos)
            playsound.playsound("myfile.mp3")
            
            
            
            
#Código para calculo vezes      
        elif (fun1 == "vezes"):
           
           multiplicacao = num1*num2
           file1=open('myfile.txt','a')
           file1.truncate(0)
           file1.write(str(multiplicacao))
           file1.close()
           file2 = open('myfile.txt', 'r').read().replace("\n", " ")
           speech = gTTS(text = str(file2), lang='pt-BR',slow = False)
           os.remove('myfile.mp3')
           speech.save('myfile.mp3')
           falar("a sua multiplicação é")
           print("A sua multiplicação é: ", multiplicacao)
           playsound.playsound("myfile.mp3")
           
           
           
#Código para o cálculo da soma          
        elif (fun1 == "mais"):      
           soma = num1+num2
           file1=open('myfile.txt','a')
           file1.truncate(0)
           file1.write(str(soma))
           file1.close()
           file2 = open('myfile.txt', 'r').read().replace("\n", " ")
           speech = gTTS(text = str(file2), lang='pt-BR',slow = False)
           os.remove('myfile.mp3')
           speech.save('myfile.mp3')
           falar("a sua soma é")
           print("A sua multiplicação é: ", soma)
           playsound.playsound("myfile.mp3")
           
           
 #Código para o cálculo da divisão           
        elif (fun1 == "dividido" or "dividido por" or "/" or "pedido"):
            divisao = num1 / num2
            file1 = open("myfile.txt", "a")
            file1.truncate(0)
            file1.write(str(divisao))
            file1.close()
            file2 = open("myfile.txt", "r").read().replace("\n", " ")
            speech = gTTS(text = str(file2), lang= 'pt-BR', slow=False)
            os.remove('myfile.mp3')
            speech.save('myfile.mp3')
            falar('a sua divisão é')
            print('A sua divisão é: ', divisao)
            playsound.playsound('myfile.mp3')
          
    
            
        
 #Resto                     
        else:
            print("Desculpe, Tente novamente.")
            output = gTTS(text=fun1, language= 'pt-BR', slow=False)
            output.save('output.mp3')
        
            
          
            
            
        print("Você gostaria de realizar outra operação? 'Sim' ou 'Não'")
        falar("Você gostaria de realizar outra operação? 'Sim' ou 'Não'")
        escolha = voz.listen(source, timeout=5)
        escolha1 = voz.recognize_google(fun, language= 'pt-BR')
        if (escolha1 == "sim" or "sin"):
            falar('Okay!')
            print("Okay!")
            flag = 1
            continue

        elif (escolha1 == "nao" or "não"):
            print(escolha1)
            print("Okay! até a proxima!")
            flag = 0

        else:
            print("Desculpe, tente novamente!")

