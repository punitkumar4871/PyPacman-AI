import tkinter as tk
import pygame
import time
from PIL import Image, ImageTk
from window import Window
import os

pygame.mixer.init()

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SRC_DIR)
STATIC_DIR = os.path.join(BASE_DIR, 'static')

background_music = os.path.join(STATIC_DIR, 'images', 'bgmusic.mp3')
button_click_sound = os.path.join(STATIC_DIR, 'images', 'btmusic.mp3')
gamesound = os.path.join(STATIC_DIR, 'images', 'audio.mp3')
background_image = os.path.join(STATIC_DIR, 'images', 'bgimage.jpg')

def start_game():
    root.destroy()
    game_window = tk.Tk()
    game_window.title("Pacman Game")
    pygame.mixer.music.fadeout(3)
    game_window.focus_force()
    game_window.lift()
    game_window.grab_set()

    def play_game_sound():
        pygame.mixer.music.load(gamesound)
        pygame.mixer.music.play(-1)

    game_window.after(3000, play_game_sound)
    pacman = Window(game_window)
    pacman.run()
    game_window.bind("<FocusIn>", lambda event: game_window.focus_force())

def play_button_click_sound():
    pygame.mixer.Sound(button_click_sound).play()

def play_background_music():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)

def show_options():
    options_window = tk.Toplevel(root)
    options_window.title("Options")
    options_window.geometry('400x200')
    credit_label = tk.Label(options_window, text="Credits", font=('Arial', 20), fg='black')
    credit_label.pack(pady=50)

def quit_game():
    pygame.mixer.music.stop()
    root.quit()
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Pacman Start Screen")
    root.configure(bg='black')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f'{screen_width}x{screen_height}')

    bg_image = Image.open(background_image)
    bg_image = bg_image.resize((screen_width, screen_height))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    ascii_art = """
███████ ████████  █████  ██████  ████████      ██████   █████  ███    ███ ███████
██          ██    ██   ██ ██   ██    ██        ██      ██   ██ ████  ████ ██
███████     ██    ███████ ██████     ██        ██  ███ ███████ ██ ████ ██  █████
      ██     ██    ██   ██ ██   ██    ██        ██   ██ ██   ██ ██  ██  ██ ██
███████     ██    ██   ██ ██   ██    ██         ██████  ██   ██ ██      ██ ███████
"""
    ascii_label = tk.Label(root, text=ascii_art, font=('Courier', 10), bg='black', fg='white')
    ascii_label.pack(pady=30)

    start_button = tk.Button(root, text="Start", font=('Arial', 24), bg='white', fg='black', command=lambda: [play_button_click_sound(), start_game()])
    start_button.pack(pady=0)

    ascii_art1 = """
 ██████  ██████  ████████ ██  ██████  ███    ██ ███████
██    ██ ██   ██    ██    ██ ██    ██ ████   ██ ██
██    ██ ██████     ██    ██ ██    ██ ██ ██  ██ ███████
██    ██ ██         ██    ██ ██    ██ ██  ██ ██       ██
 ██████  ██         ██    ██  ██████  ██   ████ ███████
"""
    ascii_label1 = tk.Label(root, text=ascii_art1, font=('Courier', 10), bg='black', fg='white')
    ascii_label1.pack(pady=30)
    option_button1 = tk.Button(root, text="Options", font=('Arial', 24), bg='white', fg='black', command=lambda: [play_button_click_sound(), show_options()])
    option_button1.pack()

    ascii_art2 = """

 ██████  ██    ██ ██ ████████
██    ██ ██    ██ ██    ██
██    ██ ██    ██ ██    ██
██  ▄▄ ██ ██    ██ ██    ██
 ██████   ██████  ██    ██
   ▀▀


"""
    ascii_label2 = tk.Label(root, text=ascii_art2, font=('Courier', 10), bg='black', fg='white')
    ascii_label2.pack(pady=30)

    option_button2 = tk.Button(root, text="Quit", font=('Arial', 24), bg='white', fg='black', command=lambda: [play_button_click_sound(), quit_game()])
    option_button2.pack()

    play_background_music()

    root.mainloop()