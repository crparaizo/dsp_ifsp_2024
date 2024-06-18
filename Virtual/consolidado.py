# instalação das bibliotecas necessárias
# pip install PyAudio # leitura do audio do microfone
# pip install SpeechRecognition # reconhecimento da a voz
# pip install os # sistema operacional
# pip install speech_recognition as sr
# pip install gTTS # google tradutor, de texto para discurso
# pip install playsound # reprodução de audio - "voz do google"

# fluxo do processamento: fala (onda sonora) -> energia eletrica (sinal analogico) -> sinal digital -> texto
# pega o audio, divide em pequenas fatias, e através de algoritmos tenta identificar qual palavra se encaixa
# com os padrões da base de dados (de cada idioma)

# importanto pacote
import speech_recognition as sr
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# funções para ouvir e reconhecer a fala
# captura, reconhece e printa

# listar microfones do computador
'''
nomes_microfones = sr.Microphone.list_microphone_names()
print("Microfones disponíveis:")
for id, nome in enumerate(nomes_microfones):
    print(f"{id}: {nome}")
'''


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    # Salva o arquivo de audio
    tts.save('audios/vozGoogle.mp3')
    # print("Estou aprendendo o que você disse...")
    # Da play ao audio
    playsound('audios/vozGoogle.mp3')
    # os.remove("audios/vozGoogle.mp3")
# Funcao responsavel por ouvir e reconhecer a fala


def ouvir_microfone():
    # habilita microfone do usuario
    microfone = sr.Recognizer()
    textoDetalhado = "Não foi possível identificar o audio. Tente novamente."
    textoPuro = "Não foi possível identificar o audio. Tente novamente."
    # com with não precisa controlar tempo que mic ficará ativo/fechado
    # with sr.Microphone(1) as mic:
    with sr.Microphone() as gravacao:
        # algoritmo de redução de ruídos no som (principalmente quando fica-se em silencio)
        # após 0.3 segs de silêncio encerrará gravação
        microfone.adjust_for_ambient_noise(gravacao, duration=1)
        print("\nInício da gravação... \n")
        audio = microfone.listen(gravacao)
        # audio = rec.listen(mic, timeout=4) #gravando por 4 segundos

        try:
            # utiliza inteligencia artificial de uma empresa (google, amazon, etc) para reconhecer padrões
            textoDetalhado = microfone.recognize_google(
                audio, language='pt-BR', show_all=True)

            textoPuro = str(
                textoDetalhado['alternative'][0]['transcript']).lower()

            # print ("O Pyhton entendeu que você disse isso: ", texto)
            print("\nTranscrição: " +
                  str(textoDetalhado['alternative'][0]['transcript']))
            print("\nConfiabilidade: " +
                  str(textoDetalhado['alternative'][0]['confidence']))

            if "navegador" in textoPuro:
                os.system("start Chrome.exe")

            if "excel" in textoPuro:
                os.system("start Excel.exe")

            if "word" in textoPuro:
                os.system("start Word.exe")

        # caso não reconheça padrão de fala
        except sr.UnknownValueError:
            print("\nNão foi possível identificar o audio.")
            microfone

        except sr.RequestError as e:
            print(
                "\nProblema ao fazer requisição para serviço Google Speech Recognition; {0}".format(e))

        return textoPuro


while True:
    frase = ouvir_microfone()

    continuar = str(input("\nDeseja ouvir transcrição? S/N\n")).upper()[0]

    if continuar == "S":
        cria_audio(frase)
    elif continuar == "N":

        continuar = str(
            input("\nDeseja realizar nova gravação? S/N\n")).upper()[0]
        if continuar == "S":
            continue
        elif continuar == "N":
            break
        else:
            print("\nDigite um comando .")
    else:
        print("\nDigite um comando válido.")

    continuar = str(input("\nDeseja realizar nova gravação?\n")).upper()[0]
    if continuar == "S":
        continue
    elif continuar == "N":
        break
    else:
        print("\nDigite um comando válido.")

    # type (texto)

    # a fazer
    # subistituir palavars ponto, interrogação, exclamação por simbolos da pontuação
    # converter em outro idioma
    # salvar em arquivo
