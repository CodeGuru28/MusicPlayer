from sre_parse import State
import tkinter as tk
import os
import pickle
import pygame
from tkinter import PhotoImage
from tkinter import filedialog
from pygame import mixer

# Constant Colors

# Const Variables
State = 'Stop'
paused = False

class Player(tk.Tk):
    
    def __init__(self):
# Basic tkinter start work
        pygame.mixer.init()
        self.window = tk.Tk()
        self.window.geometry("1000x600")
        self.window.title("Music Player")
        self.window.configure(bg='#0f1a2b')
        self.path_songs = []



# Creating the TopMost Frame
        self.Top_Frame = self.create_top_frame()


# Creating the Buttons
        self.play_Button = self.create_play_button()
        self.pause_button = self.create_pause_button()
        self.resume_button = self.create_resume_button()
        self.stop_button = self.create_stop_button()



        self.menu = self.create_menu()
        self.menu_frame = self.create_menu_frame()
        self.folder_song_Add = self.create_add_button()

        self.playlist = self.play_list()

    def create_top_frame(self):
        Top = PhotoImage(file='Images/top.png')
        tk.Label(self.window, image=Top, bg='#0f1a2b').pack(fill=tk.X)
        return Top



    def create_play_button(self):
# Making play button
        play_button = PhotoImage(file='Images/play.png')
        Ply = tk.Button(self.window, image=play_button, bg='#0f1a2b', bd=0, command=self.play_song).place(x=100, y=400)
        return play_button


    def create_pause_button(self):
# Making pause and unpause button
        pause_button = PhotoImage(file='Images/pause.png')
        tk.Button(self.window, image=pause_button, bg='#0f1a2b', bd=0, command=self.stop_song).place(x=200, y=500)
        return pause_button


    def create_resume_button(self):
        resume_button = PhotoImage(file='Images/resume.png')
        tk.Button(self.window, image=resume_button,bg='#0f1a2b', bd=0,command=mixer.music.unpause).place(x=115, y=500)
        return resume_button


    def create_stop_button(self):
        stop_button = PhotoImage(file='Images/stop.png')
        tk.Button(self.window, image=stop_button,bg='#0f1a2b', bd=0,command=mixer.music.stop).place(x=30, y=500)
        return stop_button


    def create_menu(self):
        Menu = PhotoImage(file='Images/menu.png')
        tk.Label(self.window, image=Menu, bg='#0f1a2b').pack(padx=10, pady=50, side=tk.RIGHT)
        return Menu

    def create_menu_frame(self):
        music_frame = tk.Frame(self.window, bd=2, relief=tk.RIDGE)
        music_frame.place(x=400, y=295, width=560, height=250)
        return music_frame

    def create_add_button(self):
        btn = tk.Button(self.window, text="    Add Folder Songs     ", width=15, height=2, font=("Arial", 10, "bold"), fg="white", bg='#21b3de', command = self.add_song_folder_command).place(x=400, y=240)
        return btn

    def play_list(self):
        scroll = tk.Scrollbar(self.menu_frame)
        playlist = tk.Listbox(self.menu_frame, width=100, font=('Arial', 10), bg='#333333', fg='green', selectbackground='lightblue', cursor='hand2', bd=0, yscrollcommand=scroll.set)
        playlist.bind('<Return>', self.play_song_event)
        playlist.bind('<Double-Button-1>', self.play_song_event)
        # playlist.bind('<space>', stop_song)
        scroll.config(command=playlist.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        playlist.pack(side=tk.LEFT, fill=tk.BOTH)
        return playlist




    def add_song_folder_command(self):
        self.path_song = filedialog.askdirectory()
        if self.path_song:
            os.chdir(self.path_song)
            self.path_songs.append(self.path_song)
            songs = os.listdir(self.path_song)
            for song in songs:
                if(song.endswith('.mp3')):
                    self.playlist.insert(tk.END, song)


    def create_frames(self):
        pass;


    def play_song(self):
        self.song = self.playlist.get(tk.ACTIVE)
        try:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(loops=0)
        except Exception as e:
            for i in range(int(len(self.path_songs))):
                try:
                    change_dir = os.chdir(self.path_songs[i])
                    pygame.mixer.music.load(f'{self.path_songs[i]}/{self.song}')
                    # pygame.mixer.music.load(f'{change_dir}/{self.song}')
                    pygame.mixer.music.play(loops=0)
                except Exception as e:
                    continue


    def play_song_event(self, event):
        self.song = self.playlist.get(tk.ACTIVE)
        try:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(loops=0)
        except Exception as e:
            for i in range(int(len(self.path_songs))):
                try:
                    os.chdir(self.path_songs[i])
                    pygame.mixer.music.load(f'{self.path_songs[i]}/{self.song}')
                    pygame.mixer.music.play(loops=0)
                except Exception as e:
                    continue



    def stop_song(self):
        pass;

    def run(self):
        self.window.mainloop()

if(__name__ == "__main__"):
    Music_Player = Player()
    Music_Player.run()

