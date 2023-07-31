from pytube import YouTube
from colorama import init, Fore, Style
from pySmartDL import SmartDL
import os

# Inicializar colorama
init(autoreset=True)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"{Fore.CYAN}Progreso: {percentage:.1f}%{Style.RESET_ALL}", end="\r")

def select_resolution(video):
    available_resolutions = video.streams.filter(file_extension='mp4').order_by('resolution').desc()
    print(f"{Fore.YELLOW}Resoluciones disponibles para el video:")
    for i, stream in enumerate(available_resolutions, start=1):
        print(f"{i}. {stream.resolution} ({stream.mime_type.split('/')[1].upper()})")
    option = int(input("Selecciona el número de la resolución que deseas descargar: "))
    return available_resolutions[option - 1]

def select_audio_quality(video):
    available_audio = video.streams.filter(only_audio=True).order_by('abr').desc()
    print(f"{Fore.YELLOW}Calidades disponibles para el audio:")
    for i, stream in enumerate(available_audio, start=1):
        print(f"{i}. {stream.abr} kbps")
    option = int(input("Selecciona el número de la calidad que deseas descargar: "))
    return available_audio[option - 1]

def reload_video(video_url):
    try:
        # Descargar el video
        video = YouTube(video_url, on_progress_callback=on_progress)
        print(f"{Fore.GREEN}Video encontrado: {video.title}{Style.RESET_ALL}")

        # Mostrar opciones de descarga
        print(f"{Fore.YELLOW}Opciones de descarga:")
        print("1. Video (MP4)")
        print("2. Solo Audio (MP3)")

        option = input("Selecciona el número de la opción que deseas descargar: ")

        # Recargar el video o solo el audio según la elección
        if option == "1":
            stream = select_resolution(video)
            print(f"{Fore.YELLOW}Descargando video (MP4) en {stream.resolution}: {video.title}{Style.RESET_ALL}")
            file_name = "video_" + video.title + ".mp4"
            destination = os.path.join(os.getcwd(), file_name)
            dl = SmartDL(stream.url, destination, progress_bar=False)
            dl.start()
            print(f"{Fore.GREEN}Descarga de video (MP4) completada con éxito.{Style.RESET_ALL}")
        elif option == "2":
            stream = select_audio_quality(video)
            print(f"{Fore.YELLOW}Descargando audio (MP3) en {stream.abr} kbps: {video.title}{Style.RESET_ALL}")
            file_name = "audio_" + video.title + ".mp3"
            destination = os.path.join(os.getcwd(), file_name)
            dl = SmartDL(stream.url, destination, progress_bar=False)
            dl.start()
            print(f"{Fore.GREEN}Descarga de audio (MP3) completada con éxito.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Opción no válida. Asegúrate de seleccionar la opción correcta.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Error durante la recarga: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}Bienvenido al recargador de videos.{Style.RESET_ALL}")
    video_url = input(f"{Fore.YELLOW}Ingresa la URL del video que deseas recargar: {Style.RESET_ALL}")

    reload_video(video_url)
