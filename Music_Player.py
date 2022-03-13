# --------------------------Imports--------------
import tkinter as tk
import os
import pickle
import pygame
from tkinter import PhotoImage
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk

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
        # self.window.resizable(0,0)

# For Music Playing Logic
        self.path_songs = []
        self.is_playing = False
        self.is_paused = False



# Creating the TopMost Frame
        self.Top_Frame = self.create_top_frame()


# Creating the Buttons
        self.play_Button = self.create_play_button()
        self.pause_button = self.create_pause_button()
        self.resume_button = self.create_resume_button()
        self.stop_button = self.create_stop_button()
        self.forward_button_ = self.create_forward_button()



        self.menu = self.create_menu()
        self.menu_frame = self.create_menu_frame()

        self.folder_song_Add = self.create_add_button()

        self.playlist = self.play_list()

        self.created_menu = self.create_menu_dropdown()
        self.add_song_menu = self.menu_dropdown_one()
        self.one_menu = self.menu_dropdown_one_o()

    def create_top_frame(self):
        '''Creating the top frame'''
        Top = PhotoImage(file='Images/top.png')
        tk.Label(self.window, image=Top, bg='#0f1a2b').pack(fill=tk.X)
        return Top



    def create_play_button(self):
        '''Creating the play button'''
        play_button = PhotoImage(file='Images/play.png')
        Ply = tk.Button(self.window, image=play_button, bg='#0f1a2b', bd=0, command=self.play_song).place(x=100, y=400)
        return play_button




    def create_pause_button(self):
        '''Making pause button'''
        pause_button = PhotoImage(file='Images/pause.png')
        tk.Button(self.window, image=pause_button, bg='#0f1a2b', bd=0, command=self.pause_song).place(x=200, y=500)
        return pause_button


    def create_resume_button(self):
        '''Making the unpause button'''
        resume_button = PhotoImage(file='Images/resume.png')
        tk.Button(self.window, image=resume_button,bg='#0f1a2b', bd=0,command=self.resume_song).place(x=115, y=500)
        return resume_button


    def create_stop_button(self):
        '''Creating stop button'''
        stop_button = PhotoImage(file='Images/stop.png')
        tk.Button(self.window, image=stop_button,bg='#0f1a2b', bd=0,command=self.stop_song).place(x=30, y=500)
        return stop_button



    def create_forward_button(self):
        forward_button_ = Image.open('Images/Next.png')
        forward_button_ = forward_button_.resize((40, 50), Image.ANTIALIAS)

        forward_button = ImageTk.PhotoImage(forward_button_)
        tk.Button(self.window, image=forward_button,bg='#0f1a2b', bd=0, command=self.forward_song).place(x=390, y=550)
        return forward_button
    


    def create_menu(self):
        '''Creating menu for our listbox(playlist)'''
        Menu = PhotoImage(file='Images/menu.png')
        tk.Label(self.window, image=Menu, bg='#0f1a2b').pack(padx=10, pady=50, side=tk.RIGHT)
        return Menu


    def create_menu_dropdown(self):
        my_menu = tk.Menu(self.window)
        self.window.config(menu=my_menu)
        return my_menu


    def menu_dropdown_one(self):
        add_song_menu = tk.Menu(self.created_menu)
        self.created_menu.add_cascade(label="Add songs", menu=add_song_menu)
        return add_song_menu


    def menu_dropdown_one_o(self):
        self.add_song_menu.add_command(label='Add One Song', command=self.add_one_song)
        self.add_song_menu.add_command(label='Add Songs', command=self.add_songs)



    def add_one_song(self):
        song_with_path = filedialog.askopenfilename(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
        import os
        song = os.path.basename(song_with_path)
        self.path_songs.append(song_with_path.replace(song, ''))
        self.playlist.insert(tk.END, song)


    def add_songs(self):
        song_with_path = filedialog.askopenfilenames(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
        import os
        # for i in range(int(len(song_with_path))):
            # song = os.path.basename(song_with_path)
        # tp = []
        for song_path in song_with_path:
            # tp.append(song_path)
            song = os.path.basename(song_path)
            self.path_songs.append(song_path.replace(song, ''))
            self.playlist.insert(tk.END, song)


    def create_menu_frame(self):
        '''Creating the menu frame for our playlist'''
        music_frame = tk.Frame(self.window, bd=2, relief=tk.RIDGE)
        music_frame.place(x=400, y=295, width=560, height=250)
        return music_frame



    def create_add_button(self):
        '''Creating the Button for adding songs from folders'''
        btn = tk.Button(self.window, text="    Add Folder Songs     ", width=15, height=2, font=("Arial", 10, "bold"), fg="white", bg='#21b3de', command = self.add_song_folder_command).place(x=400, y=240)
        return btn

    def play_list(self):
        '''Making the playlist'''
        scroll = tk.Scrollbar(self.menu_frame)
        playlist = tk.Listbox(self.menu_frame, width=100, font=('Arial', 10), bg='#333333', fg='green', selectbackground='lightblue', cursor='hand2', bd=0, yscrollcommand=scroll.set)
        playlist.bind('<Return>', self.play_song_event)
        playlist.bind('<Double-Button-1>', self.play_song_event)
        playlist.bind('<space>', self.resume_or_pause_song_event)
        playlist.bind('<f>', self.forward_song_event)
        playlist.bind('<b>', self.back_song)
        scroll.config(command=playlist.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        playlist.pack(side=tk.LEFT, fill=tk.BOTH)
        return playlist

    def forward_song_event(self, event):
        next_one = self.playlist.curselection()
        next_one = next_one[0]+1
        song = self.playlist.get(next_one)


        self.playlist.selection_clear(0, tk.END)
        self.playlist.activate(next_one)
        self.playlist.selection_set(next_one, last=None)
        self.play_song()


    def forward_song(self):
        next_one = self.playlist.curselection()
        next_one = next_one[0]+1
        song = self.playlist.get(next_one)


        self.playlist.selection_clear(0, tk.END)
        self.playlist.activate(next_one)
        self.playlist.selection_set(next_one, last=None)
        self.play_song()


    def back_song(self, event):
        next_one = self.playlist.curselection()
        try:
            next_one = next_one[0]-1
            song = self.playlist.get(next_one)
        except Exception as e:
            song = next_one

        finally:
            self.playlist.selection_clear(0, tk.END)
            self.playlist.activate(next_one)
            self.playlist.selection_set(next_one, last=None)
            self.play_song()


    def add_song_folder_command(self):
        '''Add a folder elements'''

# Asking for the folder directory
        self.path_song = filedialog.askdirectory()

        if self.path_song:
# Changing the current directory to the folder of songs
            os.chdir(self.path_song)

# Adding the path in the path list
            self.path_songs.append(self.path_song)

# Adding the songs(mp3 files) in the playlist
            songs = os.listdir(self.path_song)
            for song in songs:
                if(song.endswith('.mp3')):
                    self.playlist.insert(tk.END, song)


    def create_frames(self):
        pass;


    def play_song(self):
        '''Play command'''
# Getting the active listbox element(song to play)
        self.song = self.playlist.get(tk.ACTIVE)

# Using try so that can also play songs which are not in the last folder directory which was added
        try:
# Trying to play the music
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(loops=0)
            self.is_playing = True
            self.is_paused = False

        except Exception as e:
# Song not in the last current directory
# Using the path list

            for i in range(int(len(self.path_songs))):
                try:
# Changing the directories to play yhe song
                    change_dir = os.chdir(self.path_songs[i])
                    pygame.mixer.music.load(f'{self.path_songs[i]}/{self.song}')
                    # pygame.mixer.music.load(f'{change_dir}/{self.song}')
                    self.is_playing = True
                    self.is_paused = False
                    pygame.mixer.music.play(loops=0)
                except Exception as e:
                    continue



    def play_song_event(self, event):
        self.song = self.playlist.get(tk.ACTIVE)
        try:
            pygame.mixer.music.load(self.song)
            pygame.mixer.music.play(loops=0)
            self.is_playing = True
            self.is_paused = False
        except Exception as e:
            for i in range(int(len(self.path_songs))):
                try:
                    os.chdir(self.path_songs[i])
                    pygame.mixer.music.load(f'{self.path_songs[i]}/{self.song}')
                    self.is_playing = True
                    self.is_paused = False
                    pygame.mixer.music.play(loops=0)
                except Exception as e:
                    continue



    def stop_song(self):
        self.is_playing = False
        pygame.mixer.music.stop()


    def resume_song(self):
        if(self.is_paused):
            pygame.mixer.music.unpause()
            self.is_paused = False;
        if(self.is_playing == False):
            self.is_playing = True
            self.play_song()
    def pause_song(self):
        if(self.is_paused == False):
            pygame.mixer.music.pause()
            self.is_paused = True;

    def resume_or_pause_song_event(self, event):
        if(self.is_playing == False):
            self.is_playing = True
            self.play_song()
        elif(self.is_paused):
            pygame.mixer.music.unpause()
            self.is_paused = False;
        elif(self.is_paused == False):
            pygame.mixer.music.pause()
            self.is_paused = True;

    def run(self):
        self.window.mainloop()

if(__name__ == "__main__"):
    Music_Player = Player()
    Music_Player.run()

