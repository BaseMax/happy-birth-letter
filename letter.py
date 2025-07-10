import time
import pygame
import os
import shutil
from itertools import cycle
from colorama import init, Fore

init(autoreset=True)

frames = [
    r"""
       (\(^_^)/)
         \   /
          | |
        🎵 Happy
    """,
    r"""
       (/^_^)\
        /   \
        | |
     🎶 Birthday
    """,
    r"""
       (\^-^/)
        \   /
        | |
      🥳 John!
    """,
    r"""
        (•‿•)
        \o/
        |
   💃 Celebrate!
    """,
    r"""
       \(^o^)/
        (   )
        | |
     🎂 Cheers!
    """
]

color_cycle = cycle([Fore.CYAN, Fore.YELLOW, Fore.MAGENTA, Fore.GREEN, Fore.BLUE, Fore.RED])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text):
    columns = shutil.get_terminal_size().columns
    return '\n'.join(line.center(columns) for line in text.strip('\n').split('\n'))

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dance_animation(repeat=3, delay=0.4):
    for _ in range(repeat):
        for frame in frames:
            clear()
            color = next(color_cycle)
            print()
            print(color + center_text(frame))
            print()
            print(Fore.LIGHTWHITE_EX + center_text("🎊 " * ((_ % 2) + 3)))
            time.sleep(delay)

def greet():
    clear()

    print()
    print(Fore.LIGHTMAGENTA_EX + center_text("🎉🎉🎉 Let's Celebrate! 🎉🎉🎉"))
    time.sleep(1)

    text = "Happy Birthday, John from Brisbane! 🦘"
    print(Fore.YELLOW + text.center(shutil.get_terminal_size().columns))
    time.sleep(1)

    dance_animation()
    time.sleep(1)

    text = "Wishing you all the joy, love, and cake you can handle! 🎂🍰🎁"
    print(Fore.GREEN + text.center(shutil.get_terminal_size().columns))
    time.sleep(0.5)

    print(Fore.BLUE + center_text("Made with ❤️ in Python by Max"))
    print()

def play_music():
    music_path = os.path.abspath("happy-birthday.mp3")
    print("Playing:", music_path)
    
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print("Music playback failed:", e)


if __name__ == "__main__":
    play_music()
    greet()
