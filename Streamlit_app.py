import streamlit as st
from PIL import Image
import time
transition_duration = 5  # Duración de la transición en segundos
title_page_web='Reborn' #Título del Dashboard
title_portada='SIEMPRE LUCHASTE POR SER LA MEJOR🚗🤠🚲🎥🎵' #Título del Dashboard


sms_img=[
    "Ella es Grachi 😍",
    "tiene una gran familia❤️,",
    "le gusta conocer nuevos lugares🛣️.",
    "Donde a veces muestra su inmenso corazón 🤫",
    "sin que suela perder su sonrisa😊.",
    "Siempre muestra empeño en lo que hace🤓,",
    "y tiene un tesoro valioso👩‍👧...",
    "Además, estima a más personas💛",
    "logro rodearse de buenas amigas 🎓,",
    "aunque siempre hay una mejor amiga 🫂.",
    "Lograron superar con creces un desafío importante✨,",
    "debido a que ella nunca dejó de confiar en sí 😌🙌."
]



# 3° Nombres de la página web.
st.set_page_config(page_title = title_page_web, #Nombre de la pagina, sale arriba cuando se carga streamlit
                   page_icon = '💪', # https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")

st.markdown(f"<h1 style='text-align: center;'>{title_portada}</h1>", unsafe_allow_html=True)
st.markdown("---")




def main():
    #4° Insertar música: Sin que esta se pare...
    audio1=open("Music.mp3","rb")
    st.write("<REPRODUCEME 🎧🎵")
    st.audio(audio1)

    # # Función para cargar y reproducir música en un hilo separado
    # import pygame
    # import threading
    # import time
    # def play_music(file_path, music_state):
    #     pygame.mixer.init()
    #     pygame.mixer.music.load(file_path)
    #     while music_state["playing"]:
    #         pygame.mixer.music.play()
    #         time.sleep(pygame.mixer.music.get_length())
    #     pygame.mixer.music.stop()

    # # Ruta al archivo de música
    # music_file_path = "Music.mp3"

    # # Crear un diccionario para almacenar el estado de la música
    # music_state = {"playing": False}

    # # Almacenar el estado de la música en la sesión de Streamlit
    # if "music_state" not in st.session_state:
    #     st.session_state.music_state = music_state

    # # Iniciar la música al cargar la aplicación
    # if not st.session_state.music_state["playing"]:
    #     st.session_state.music_state["playing"] = True
    #     music_thread = threading.Thread(target=play_music, args=(music_file_path, st.session_state.music_state), daemon=True)
    #     music_thread.start()

    # Lista de rutas de imágenes
    image_paths = ["Imagen1.jpg", "Imagen2.jpg", "Imagen3.jpg", "Imagen4.jpg", "Imagen5.jpg",
                "Imagen6.jpg", "Imagen7.jpg", "Imagen8.jpg", "Imagen9.jpg", "Imagen10.jpg",
                "Imagen11.jpg", "Imagen12.jpg"]

    # Lista de imágenes PIL
    images = [Image.open(path) for path in image_paths]
    list_img_ancho=[
        3,3.95,3,
        3,3.9,3.9,
        3.55,3,3.55,
        3,3,5
    ]
    # Muestra las imágenes con transiciones
    for i in range(0,12,3):
        col1, col2, col3, col4, col5 = st.columns([4,list_img_ancho[i],list_img_ancho[i+1],list_img_ancho[i+2],4]) #Centrar el botón

        col2.image(images[i % len(images)], use_column_width=True, caption=f"{sms_img[i]}")
        time.sleep(transition_duration)

        col3.image(images[(i + 1) % len(images)], use_column_width=True, caption=f"{sms_img[i+1]}")
        time.sleep(transition_duration)

        col4.image(images[(i + 2) % len(images)], use_column_width=True, caption=f"{sms_img[i+2]}")
        time.sleep(transition_duration)
        
if __name__ == "__main__":
    main()
