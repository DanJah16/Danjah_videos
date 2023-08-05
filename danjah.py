from pytube import YouTube
from colorama import init, Fore, Style
from pySmartDL import SmartDL
import os

# Inicializar colorama
init(autoreset=True)

def select_resolution(video):
    available_resolutions = video.streams.filter(file_extension='mp4').order_by('resolution').desc()
    print(f"{Fore.YELLOW}{'-' * 20}")
    print("  Resoluciones disponibles para el video:")
    for i, stream in enumerate(available_resolutions, start=1):
        print(f"  {i}. {stream.resolution}")
    option = int(input("  Selecciona el número de la resolución que deseas descargar: "))
    return available_resolutions[option - 1]

def select_audio_quality(video):
    available_audio = video.streams.filter(only_audio=True).order_by('abr').desc()
    print(f"{Fore.YELLOW}{'-' * 20}")
    print("  Calidades disponibles para el audio:")
    for i, stream in enumerate(available_audio, start=1):
        print(f"  {i}. {stream.abr} kbps")
    option = int(input("  Selecciona el número de la calidad que deseas descargar: "))
    return available_audio[option - 1]

# ...

def reload_video(video_url):
    try:
        # Descargar el video
        video = YouTube(video_url)
        print(f"{Fore.GREEN}{'-' * 30}")
        print(f"  {Fore.MAGENTA}BIENVENIDO AL RECARGADOR DE VIDEOS.")
        print(f"{'-' * 30}{Style.RESET_ALL}")

        # Mostrar opciones de descarga
        print(f"{Fore.YELLOW}{'-' * 20}")
        print(f"  {Fore.CYAN}OPCIONES DE DESCARGA:")
        print(f"  {Fore.CYAN}1. Video (MP4)")
        print(f"   2. Solo Audio (MP3)")
        print(f"{'-' * 20}{Style.RESET_ALL}")

        option = input("  Selecciona el número de la opción que deseas descargar: ")

        # Recargar el video o solo el audio según la elección
        if option == "1":
            stream = select_resolution(video)
            print(f"{Fore.YELLOW}{'-' * 20}")
            print(f"  {Fore.CYAN}DESCARGANDO VIDEO (MP4) EN {stream.resolution}: {video.title}")
            print(f"{'-' * 20}{Style.RESET_ALL}")
            file_name = "danjah_" + video.title + ".mp4"
            destination = os.path.join("/sdcard/", file_name)  # Ruta en la tarjeta SD
            dl = SmartDL(stream.url, destination)
            dl.start()
            print(f"{Fore.GREEN}  Descarga de video (MP4) completada con éxito.{Style.RESET_ALL}")
        elif option == "2":
            stream = select_audio_quality(video)
            print(f"{Fore.YELLOW}{'-' * 20}")
            print(f"  {Fore.CYAN}DESCARGANDO AUDIO (MP3) EN {stream.abr} kbps: {video.title}")
            print(f"{'-' * 20}{Style.RESET_ALL}")
            file_name = "danjah_" + video.title + ".mp3"
            destination = os.path.join("/sdcard/", file_name)  # Ruta en la tarjeta SD
            dl = SmartDL(stream.url, destination)
            dl.start()
            print(f"{Fore.GREEN}  Descarga de audio (MP3) completada con éxito.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{'-' * 20}")
            print("  Opción no válida. Asegúrate de seleccionar la opción correcta.")
            print(f"{'-' * 20}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}{'-' * 20}")
        print(f"  ERROR DURANTE LA DESCARGA: {e}")
        print(f"{'-' * 20}{Style.RESET_ALL}")

# ...



if __name__ == "__main__":
    print(f"{Fore.MAGENTA}{'-' * 30}")
    print("  BIENVENIDO A DANJAH VIDEOS.")
    print(f"{'-' * 30}{Style.RESET_ALL}")
    video_url = input(f"{Fore.YELLOW}Ingresa la URL del video que deseas recargar: {Style.RESET_ALL}")

    reload_video(video_url)
        
