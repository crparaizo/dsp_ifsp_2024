# instalação das bibliotecas necessárias
# pip install SpeechRecognition
# pip install PyAudio

# importanto pacote
import speech_recognition as sr

# listar microfones do computador
'''
nomes_microfones = sr.Microphone.list_microphone_names()
print("Microfones disponíveis:")
for id, nome in enumerate(nomes_microfones):
    print(f"{id}: {nome}")
'''

# reconhece o audio e trnasforma em texto
rec = sr.Recognizer()

while True:
    try:
        texto = ""
        # com with não precisa controlar tempo que mic ficará ativo/fechado
        # with sr.Microphone(1) as mic:
        with sr.Microphone() as mic:
            # algoritmo de redução de ruídos no som (principalmente quando fica-se em silencio)
            rec.adjust_for_ambient_noise(mic, duration=0.3)
            print("Comece a falar para Python gravar")
            audio = rec.listen(mic)
            # audio = rec.listen(mic, timeout=4) #gravando por 4 segundos

            # utiliza inteligencia artificial de uma empresa (google, amazon, etc) para reconhecer padrões
            texto = rec.recognize_google(
                audio, language='pt-BR', show_all=True)

            texto2 = str(texto['alternative'][0]['transcript']).lower()

            # print ("O Pyhton entendeu que você disse isso: ", texto)
            print("Transcrição: " + str(texto['alternative'][0]['transcript']))
            print("Confidence: " + str(texto['alternative'][0]['confidence']))

            # encerrar loop
            if texto2 == "sair":
                print("Saindo...")
                break

    # caso não reconheça padrão de fala
    except sr.UnknownValueError:
        print("Não foi possível identificar o audio")
        rec
        continue

    except sr.RequestError as e:
        print("Problema para fazer requicição no serviço do Google Speech Recognition; {0}".format(e))


# type (texto)

# a fazer
# subistituir palavars ponto, interrogação, exclamação por simbolos da pontuação
# converter em outro idioma
# salvar em arquivo


# print('Confidence: {}'.format(mic.confidence))

# print(str(['alternative'][0]['transcript']))
# print(str(['alternative'][0]['confidence']))

'''
def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Não entendi")
    return frase
ouvir_microfone()
'''
