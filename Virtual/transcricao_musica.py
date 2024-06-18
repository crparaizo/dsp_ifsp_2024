import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from gtts import gTTS
from playsound import playsound


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    # Salva o arquivo de audio
    tts.save('Virtual/audios/vozGoogle.mp3')
    # print("Estou aprendendo o que você disse...")
    # Da play ao audio
    playsound('Virtual/audios/vozGoogle.mp3')
    # os.remove("audios/vozGoogle.mp3")
# Funcao responsavel por ouvir e reconhecer a fala


def transformar_arquivoMP3():
    # arquivos
    audio_mp3 = 'Virtual/musicas/Aquarela.mp3'
    audio_wav = 'Virtual/musicas/Aquarela.wav'

    # conversão de mp3 para wav
    sound = AudioSegment.from_mp3(audio_mp3)
    sound.export(audio_wav, format='wav')

    # selecionando audio
    audio = AudioSegment.from_file(audio_wav, 'wav')
    # Tamanho em milisegundos
    tamanho = 30000
    # divisão do audio em partes
    partes = make_chunks(audio, tamanho)
    partes_audio = []
    for i, parte in enumerate(partes):
        # Enumerando arquivo particionado
        parte_name = 'Virtual/musicas/Parte{0}.wav'.format(i)
        # Guardando os nomes das partições em uma lista
        partes_audio.append(parte_name)
        # Exportando arquivos
        parte.export(parte_name, format='wav')
    return partes_audio


def transcreve_audio(nome_audio, contador):
    # Selecione o audio para reconhecimento
    r = sr.Recognizer()
    with sr.AudioFile(nome_audio) as source:
        audio = r.record(source)  # leitura do arquivo de audio

    # Reconhecimento usando o Google Speech Recognition
    try:
        print(f'\nParte {contador}: ' +
              r.recognize_google(audio, language='pt-BR'))
        texto = r.recognize_google(audio, language='pt-BR').lower()
    except sr.UnknownValueError:
        print('\nGoogle Speech Recognition NÃO ENTENDEU o audio')
        texto = ''
    except sr.RequestError as e:
        print(
            '\nNão foi possível solicitar resultados do serviço Google Speech Recognition; {0}'.format(e))
        texto = ''
    return texto


# estrutura de loop
while True:

    contador = 0

    retorno = transformar_arquivoMP3()

    # Aplicando a função de reconhecimento de voz em cada parte
    texto = ''
    for parte in retorno:
        contador = contador + 1
        texto = texto + ' ' + transcreve_audio(parte, contador)

    continuar = str(input("\nDeseja ouvir a transcrição? S/N\n")).upper()[0]

    if continuar == "S":
        cria_audio(texto)
    elif continuar == "N":
        break
    else:
        print("Digite um comando válido")
