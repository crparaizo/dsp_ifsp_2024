# instalação das bibliotecas necessárias
# pip install PyAudio # leitura do audio do microfone
# pip install SpeechRecognition # reconhece a voz 

#fala (onda sonora) -> energia eletrica (sinal analogico) -> sinal digital -> texto
#pega o audio, didide em pequenas fatias, e atraves de algoritmos tenta identificar qual palavra se encaixa com os apdrões que eles tem

# importanto pacote
import speech_recognition as sr

#importa sistema operacional
import os

# função para ouvir e reconhecer a fala
# captura, reconhece e printa
def ouvir_microfone():
    
    #habilita microfone do usuario
    microfone = sr.Recognizer()

    #usando microfone
    with sr.Microphone() as source:

        #chama um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #frase para o usuário dizer algo
        print("diga alguma coisa: ")

        #armazena o que foi dito em uma variavel
        audio = microfone.listen(source)
    try:

        #passa a variavel para o algoritmo reconhecer padrões
        #modelos matematicos já treinados
        frase = microfone.recognize_google(audio, language='pt-BR')
        
        #deixar tudo minsculo
        frase = frase.lower()

        if "navegador" in frase:
            os.system("start Chrome.exe")

        if "Excel" in frase:
            os.system("start Excel.exe")

        #retora a frase pronuniada
        print("Você disse: " + frase)
        # print(f"{frase}\n")
    
    # se não reconhecer o padrão de fala, exibe a mensagem
    except sr.UnknownValueError as error:
        print("Não entendi")
        # print(f"Erro: {error}\n")
        # ouvir_microfone()
        # continue
    
    return frase

# estrutura de loop
while True:
    ouvir_microfone ()
    continuar = str(input("Deseja Continuar? S/N")).upper()[0]

    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        print("Digite um comando válido")