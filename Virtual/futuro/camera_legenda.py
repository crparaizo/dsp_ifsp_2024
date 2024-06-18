import cv2
import numpy as np
import speech_recognition as sr
import mtranslate as mt

# Definir idiomas de entrada e saída
lang_input = 'pt'
lang_output = 'en'

# Inicializar o reconhecimento de fala
r = sr.Recognizer()

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

# Definir a largura e a altura da imagem capturada
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Definir a taxa de quadros do vídeo para 60 fps
cap.set(cv2.CAP_PROP_FPS, 60)

# Definir fonte e cor da legenda
font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 255)

while True:
    # Ler o próximo frame da câmera
    ret, frame = cap.read()

    # Converter o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Utilizar o microfone como fonte de áudio
    with sr.Microphone() as source:
        # Ajustar ruído
        r.adjust_for_ambient_noise(source, duration=1)
        # Ouvir o áudio
        audio = r.listen(source)
        
    

    try:
        # Transcrever o áudio em texto
        text = r.recognize_google(audio, language=lang_input)
        # Traduzir o texto
        translation = mt.translate(text)
        # Obter o tamanho da legenda
        text_size, _ = cv2.getTextSize(translation, font, 0.5, 1)
        # Escrever a transcrição na imagem
        cv2.putText(frame, translation, (10, frame.shape[0]-10), font, 0.5, color, 1, cv2.LINE_AA)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Erro ao se comunicar com o Google Speech Recognition: {0}".format(e))

    # Mostrar a imagem com a legenda
    cv2.imshow('frame', frame)

    # Parar o programa se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura de vídeo e fechar as janelas
cap.release()
cv2.destroyAllWindows()
