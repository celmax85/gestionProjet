import tkinter as tk
from random import *
import time


pointJ = 0
pointB = 0
def GameGuessing():

    window = tk.Tk()
    window.iconbitmap("pygame.ico")
    window.geometry("600x400")
    window.config(bg="#065569")
    window.resizable(width=True,height=False)
    window.title('Le nombre mystere')
    TARGET = randint(0, 10)
    RETRIES = 0
    
    def update_result(text):
        result.configure(text=text)
    
    def new_game():
        guess_button.config(state='normal')
        global TARGET, RETRIES
        TARGET = randint(0, 10)
        RETRIES = 0
        update_result(text="Trouvez le numbre mystere entre\n 1 et 10")
    
    def play_game():
        global RETRIES
    
        choice = int(number_form.get())
        
        if choice != TARGET:
            RETRIES += 1
        
            result = "Rater"
            if TARGET < choice:
                hint = "Le nombre mystere est compris entre 0 et {}".format(result)
            else:
                hint = "Le nombre mystere se situe entre {} et 100".format(choice)
            result += "\n\nHINT :\n" + hint
        
        else:
            result = "Vous avez deviné le bon nombre après {} essaie".format(RETRIES)
            guess_button.configure(state='disabled')
            result += "\n" + "Cliquez sur Jouer pour démarrer une nouvelle partie"
        
        update_result(result)
    
    title = tk.Label(window,text="Le nombre mystere",font=("Arial",24),fg="#fffcbd",bg="#065569")
    result = tk.Label(window, text="Cliquez sur Jouer pour démarrer une nouvelle partie", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tk.LEFT)
    play_button = tk.Button(window, text="Jouer", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)
    guess_button = tk.Button(window,text="Valider",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
    exit_button = tk.Button(window,text="Quitter",font=("Arial",14), fg="White", bg="#b82741", command = window.destroy)
    
    guessed_number = tk.StringVar()
    number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
    
    title.place(x=170, y=50)
    result.place(x=180, y=210)
    exit_button.place(x=300,y=320)
    guess_button.place(x=350, y=147) 
    play_button.place(x=170, y=320)
    number_form.place(x=180, y=150)
def ShiFuMi():
 
#definiton des fonctions
 
    def choix(element) :
        global pointJ, pointB
        BOT = randint(1,3)
    
        if BOT == 1: # Le bot a pris papier
            chaineChoixBot.configure(text = "Le bot a pris papier")
            if element ==1: # Clic sur papier
                chaine.configure(text ='égalité !')
            elif element == 3: # Clic sur ciseaux
                chaine.configure(text ='Vous gagnez un point =P')
                pointJ += 1
            else: # Clic sur ciseaux
                chaine.configure(text ='Vous perdez =(')
                pointB += 1
    
        elif BOT == 2: # Le bot a pris pierre
            chaineChoixBot.configure(text = "Le bot a pris pierre")
            if element == 2: # Clic sur pierre
                chaine.configure(text ='égalité !')
            elif element == 1: # Clic sur papier
                chaine.configure(text ='Vous gagnez un point =P')
                pointJ += 1
            else: # Clic sur papier
                chaine.configure(text ='Vous perdez =(')
                pointB += 1
    
        else: # Le bot a pris ciseaux
            chaineChoixBot.configure(text = "Le bot a pris ciseaux")
            if element ==3: # Clic sur ciseaux
                chaine.configure(text ='égalité !')
            elif element == 2: # Clic sur pierre
                chaine.configure(text ='Vous gagnez un point =P')
                pointJ += 1
            else: # Clic sur pierre
                chaine.configure(text ='Vous perdez =(')
                pointB += 1
    
        chainePointJoueur.configure(text = "Vos points :" + str(pointJ))
        chainePointBot.configure(text = "point du Bot :" + str(pointB))
    
    # programe IG affichage
    
    fenetre = tk.Tk()
    fenetre.iconbitmap("pygame.ico")
    fenetre.title("ShiFuMi")
    fenetre.geometry("600x200")
    fenetre.config(bg="#ffd966")
    texte1 = tk.Label(fenetre, text='Feuille, cailloux, ciseau, 1 2 3 !', bg="#ffd966")
    texte1.pack()
    bouton1 = tk.Button(fenetre, text="Papier", command = (lambda: choix(1)), bg="#FFFFFF", fg="#000000")
    bouton1.pack()
    bouton2 = tk.Button(fenetre, text="Pierre", command = (lambda: choix(2)), bg="#808080", fg="#FFFFFF")
    bouton2.pack()
    bouton3 = tk.Button(fenetre, text="Ciseaux", command = (lambda: choix(3)), bg="#6fa8dc", fg="#cc0000")
    bouton3.pack()
    bouton4 = tk.Button(fenetre, text="Quitter", command = fenetre.destroy, bg="#660000", fg="#f3f6f4")
    bouton4.pack()
    chaine = tk.Label(fenetre, bg="#ffd966")
    chaine.pack()
    chaineChoixBot = tk.Label(fenetre, text="", bg="#ffd966")
    chainePointJoueur = tk.Label(fenetre, text='Vos points :'+ str(pointJ),bg="#ffd966")
    chainePointBot = tk.Label(fenetre, text='Les points du Bot :'+ str(pointB), bg="#ffd966")
    chainePointJoueur.pack(side=tk.BOTTOM)
    chainePointBot.pack(side=tk.BOTTOM)
    chaineChoixBot.pack(side=tk.BOTTOM)
def justePrix():

    window = tk.Tk()
    window.iconbitmap("pygame.ico")
    window.geometry("600x400")
    window.config(bg="#9BC4E2")
    window.resizable(width=True,height=False)
    window.title('Le juste prix')
    TARGET = randint(0, 10000)
    RETRIES = 0
    
    def update_result(text):
        result.configure(text=text)
    
    def new_game():
        guess_button.config(state='normal')
        global TARGET, RETRIES
        TARGET = randint(0, 10)
        RETRIES = 0
        update_result(text="Trouvez le juste prix")
    
    def play_game():
        global RETRIES
    
        choice = int(number_form.get())
        
        if choice != TARGET:
            RETRIES += 1
        
            result = "Non"
            if TARGET < choice:
                hint = "c'est moins"
            else:
                hint = "c'est plus"
            result += "\n\nIndice :\n" + hint
        
        else:
            result = "Tu a trouvez le juste prix en {} essaie".format(RETRIES)
            guess_button.configure(state='disabled')
            result += "\n" + "Cliquez sur Jouer pour démarrer une nouvelle partie"
        
        update_result(result)
    
    title = tk.Label(window,text="Le juste prix",font=("Arial",24),fg="#fffcbd",bg="#9BC4E2")
    result = tk.Label(window, text="Cliquez sur Jouer pour démarrer une nouvelle partie", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#9BC4E2", justify=tk.LEFT)
    play_button = tk.Button(window, text="Jouer", font=("Arial", 14, "bold"), fg = "Black", bg="#ADE55C", command=new_game)
    guess_button = tk.Button(window,text="Valider",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
    exit_button = tk.Button(window,text="Quitter",font=("Arial",14), fg="White", bg="#BE3455", command = window.destroy)
    
    guessed_number = tk.StringVar()
    number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
    
    title.place(x=170, y=50)
    result.place(x=180, y=210)
    exit_button.place(x=300,y=320)
    guess_button.place(x=350, y=147) 
    play_button.place(x=170, y=320)
    number_form.place(x=180, y=150)

fenetre = tk.Tk()
fenetre.iconbitmap("pygame.ico")
fenetre.title("les mini-jeu cool")
fenetre.config(bg="#c90076")
fenetre.geometry('500x100')
bouton1 = tk.Button(fenetre, text='Numbre Mystere', command=GameGuessing, bg="#ce7e00")
bouton2 = tk.Button(fenetre, text='Juste prix', command=justePrix, bg="#8fce00")
bouton3 = tk.Button(fenetre, text='Shifumi', command=ShiFuMi, bg="#2986cc")
button4 = tk.Button(fenetre, text="Quitter", command= fenetre.destroy, bg="#f44336")
bouton1.pack()
bouton2.pack()
bouton3.pack()
button4.pack()
 
fenetre.mainloop()