from tkinter import *
def base():
  from tkinter import Tk
  import tkinter as tk
  def default_player():
    from default import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def bloody_player():
    from bloody import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def cute_player():
    from cute import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def neon_player():
    from neon import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  def sea_player():
    from sea import MusicPlayer
    # Passing Root to MusicPlayer Class
    MusicPlayer(root)
  # Creating TK Container
  root=Tk()
  # Window Title
  root.title("Nolae")
  # Icon
  #root.iconbitmap(r'n1.ico')
  # Window Geometry
  root.geometry("500x350")
  # Disable resizing
  root.resizable(False,False)
  
  # Creating Button Frame For Light Theme
  def light():
    '''
    buttonframe = LabelFrame(root,text="",bg="#E1E1E1",fg="black",bd=5,relief=FLAT)
    buttonframe.place(x=0,y=100,width=500,height=100)
    # Inserting Buttons
    default_btn = Button(buttonframe,text="Default",command=default_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=20,pady=15)
   
    bloody_btn = Button(buttonframe,text="Bloody",command=bloody_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=10,pady=15)
   
    cute_btn = Button(buttonframe,text="Cute",command=cute_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)
    neon_btn = Button(buttonframe,text="Neon",command=neon_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=9,padx=10,pady=15)
    sea_btn = Button(buttonframe,text="Sea",command=sea_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=11,padx=10,pady=15)
    '''
    # Frame for Colors
    colors_buttonframe = LabelFrame(root,text="Colors",bg="#E1E1E1",fg="black",bd=5,relief=FLAT)
    colors_buttonframe.place(x=0,y=0,width=700,height=100)
    # Inserting Buttons of Colors frame
    light_btn = Button(colors_buttonframe,text="Light",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=20,pady=15)
    dark_btn = Button(colors_buttonframe,text="Dark",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=20,pady=15)
    pastel_btn = Button(colors_buttonframe,text="Pastel",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
    neon_btn = Button(colors_buttonframe,text="Neon",command=neon_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)
    # Frame for Seasons
    seasons_buttonframe = LabelFrame(root,text="Seasons",bg="#E1E1E1",fg="black",bd=5,relief=FLAT)
    seasons_buttonframe.place(x=0,y=100,width=700,height=100)
    # Inserting Buttons of Seasons Frame
    spring_btn = Button(seasons_buttonframe,text="Spring",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=20,pady=15)
    summer_btn = Button(seasons_buttonframe,text="Summer",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=20,pady=15)
    autumn_btn = Button(seasons_buttonframe,text="Autumn",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
    winter_btn = Button(seasons_buttonframe,text="Winter",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#f3f3f3",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=20,pady=15)

    # Frame for Others
    others_buttonframe = LabelFrame(root,text="Others",bg="#E1E1E1",fg="black",bd=5,relief=FLAT)
    others_buttonframe.place(x=0,y=200,width=700,height=100)
    # Inserting Buttons of Others Frame
    bloody_btn = Button(others_buttonframe,text="Bloody",command=bloody_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=10,pady=15)
    cute_btn = Button(others_buttonframe,text="Cute",command=cute_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=10,pady=15)
    alien_btn = Button(others_buttonframe,text="Alien",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#141414",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=10,pady=15)
    sea_btn = Button(others_buttonframe,text="Sea",command=sea_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#141414",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)


  # Creating Button Frame For Dark Theme
  def dark():
    # Frame for Colors
    colors_buttonframe = LabelFrame(root,text="Colors",bg="#141414",fg="black",bd=5,relief=FLAT)
    colors_buttonframe.place(x=0,y=0,width=700,height=100)
    # Inserting Buttons of Colors frame
    light_btn = Button(colors_buttonframe,text="Light",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=20,pady=15)
    dark_btn = Button(colors_buttonframe,text="Dark",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=20,pady=15)
    pastel_btn = Button(colors_buttonframe,text="Pastel",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
    neon_btn = Button(colors_buttonframe,text="Neon",command=neon_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)
    # Frame for Seasons
    seasons_buttonframe = LabelFrame(root,text="Seasons",bg="#141414",fg="black",bd=5,relief=FLAT)
    seasons_buttonframe.place(x=0,y=100,width=700,height=100)
    # Inserting Buttons of Seasons Frame
    spring_btn = Button(seasons_buttonframe,text="Spring",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=20,pady=15)
    summer_btn = Button(seasons_buttonframe,text="Summer",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=20,pady=15)
    autumn_btn = Button(seasons_buttonframe,text="Autumn",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
    winter_btn = Button(seasons_buttonframe,text="Winter",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=20,pady=15)

    # Frame for Others
    others_buttonframe = LabelFrame(root,text="Others",bg="#141414",fg="black",bd=5,relief=FLAT)
    others_buttonframe.place(x=0,y=200,width=700,height=100)
    # Inserting Buttons of Others Frame
    bloody_btn = Button(others_buttonframe,text="Bloody",command=bloody_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=1,padx=10,pady=15)
    cute_btn = Button(others_buttonframe,text="Cute",command=cute_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=3,padx=10,pady=15)
    alien_btn = Button(others_buttonframe,text="Alien",width=5,height=1,font=("times new roman",16,"bold"),#no command
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=10,pady=15)
    sea_btn = Button(others_buttonframe,text="Sea",command=sea_player,width=5,height=1,font=("times new roman",16,"bold"),
                        fg="#E1E1E1",bg="#ff66dd",relief=FLAT, activebackground="#ff92ed").grid(row=0,column=7,padx=10,pady=15)
    
  # View the Default Light theme first

  # Frame for radio buttons
  radframe = LabelFrame(root, text="Select Current Theme", font=("Fixedsys", 12, "bold"), bg="#E1E1E1")
  radframe.place(x=0, y=300, height=50, width= 500)
  # Radio buttons to change light theme and dark theme
  
  R1 = Radiobutton(radframe, text="Dark", value=1 ,command=dark, font=("Fixedsys", 12))
  R1.grid(row= 0, column=2, padx=5, pady=5)

  R2 = Radiobutton(radframe, text="Light", value=2 ,command=light, font=("Fixedsys", 12))
  R2.grid(row= 0, column=4, padx=5, pady=5)



  # Root Window Looping
  root.mainloop()
