from tkinter import *
from random import randint
 
def GameGuessing():
    window = Tk()
 
    # Set the dimensions of the created window
    window.geometry("600x400")
    
    # Set the background color of the window
    window.config(bg="#065569")
    
    window.resizable(width=False,height=False)
    
    # Set Window Title
    window.title('Number Guessing Game')
    
    # The code for the buttons and text and other 
    # interactive UI elements go here 
    
    TARGET = randint(0, 10)
    RETRIES = 0
    
    
    def update_result(text):
        result.configure(text=text)
    
    # Create a new game
    def new_game():
        guess_button.config(state='normal')
        global TARGET, RETRIES
        TARGET = randint(0, 10)
        RETRIES = 0
        update_result(text="Guess a number between\n 1 and 10")
    
    # Continue the ongoing game or end it
    def play_game():
        global RETRIES
    
        choice = int(number_form.get())
        
        if choice != TARGET:
            RETRIES += 1
        
            result = "Wrong Guess!! Try Again"
            if TARGET < choice:
                hint = "The required number lies between 0 and {}".format(result)
            else:
                hint = "The required number lies between {} and 100".format(choice)
            result += "\n\nHINT :\n" + hint
        
        else:
            result = "You guessed the correct number after {} retries".format(RETRIES)
            guess_button.configure(state='disabled')
            result += "\n" + "Click on Play to start a new game"
        
        update_result(result)
    
    # Heading of our game
    title = Label(window,text="Guessing Game",font=("Arial",24),fg="#fffcbd",bg="#065569")
    
    # Result and hints of our game
    result = Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=LEFT)
    
    # Play Button
    play_button = Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=new_game)

    # Guess Button
    guess_button = Button(window,text="Guess",font=("Arial",13), state='disabled', fg="#13d675",bg="Black", command=play_game)
    
    # Exit Button
    exit_button = Button(window,text="Exit Game",font=("Arial",14), fg="White", bg="#b82741", command=exit)
    
    
    # Entry Fields
    guessed_number = StringVar()
    number_form = Entry(window,font=("Arial",11),textvariable=guessed_number)
    
    
    # Place the labels
    
    title.place(x=170, y=50)
    result.place(x=180, y=210)
    
    # Place the buttons
    exit_button.place(x=300,y=320)
    guess_button.place(x=350, y=147) 
    play_button.place(x=170, y=320)
    
    # Place the entry field
    number_form.place(x=180, y=150)
def PrixJuste():
    toplevel = Tk()
    toplevel.geometry('200x100')
    label = Label(toplevel, text='Voici le jeu du juste prix')
    label.pack()
def ShiFuMi():
    
    pointJ = 0
    pointB = 0
 
    values = { 0: 'Papier', 1: 'Pierre', 2: 'Ciseaux' }
 
#definiton des fonctions
 
    def choisir(choixJoueur) :
        global pointJ, pointB, values
        choixBot = randint(0,2)
    
        chaineChoixBot.configure(text = "Choix du bot : %s" % values[choixBot])
    
        if choixJoueur == choixBot:
            # Égalité
            chaine.configure(text = "Égalité")
        elif (choixJoueur+1) % 3 == choixBot:
            # Le joueur a gagné
            pointJ += 1
            chaine.configure(text = "Vous avez gagné :-)")
        else:
            # Le bot a gagné
            pointB += 1
            chaine.configure(text = "Vous avez perdu :'(")
    
        chainePointJoueur.configure(text = "Vos points : %d" % pointJ)
        chainePointBot.configure(text = "Les point du Bot : %d" % pointB)
 
    # programe IG affichage
 
    fenetre = Tk()
    fenetre.title('ShiFuMi')
    texte1 = Label(fenetre, text='Feuille, cailloux, ciseau, 1 2 3 !')
    texte1.pack()
    bouton1 = Button(fenetre, text="Papier", command = (lambda: choisir(0)))
    bouton1.pack()
    bouton2 = Button(fenetre, text="Pierre", command = (lambda: choisir(1)))
    bouton2.pack()
    bouton3 = Button(fenetre, text="Ciseaux", command = (lambda: choisir(2)))
    bouton3.pack()
    bouton4 = Button(fenetre, text="Quitter", command = fenetre.destroy)
    bouton4.pack()
    chaine = Label(fenetre)
    chaine.pack()
    chaineChoixBot = Label(fenetre, text="")
    chainePointJoueur = Label(fenetre, text='Vos points :'+ str(pointJ))
    chainePointBot = Label(fenetre, text='Les points du Bot :'+ str(pointB))
    chainePointJoueur.pack(side=BOTTOM)
    chainePointBot.pack(side=BOTTOM)
    chaineChoixBot.pack(side=BOTTOM)
 
 
fenetre = Tk() ##
fenetre.geometry('200x100')
 
bouton1 = Button(fenetre, text='Guessing Game', command=GameGuessing)
bouton2 = Button(fenetre, text='Juste prix', command=PrixJuste)
bouton3 = Button(fenetre, text='Shifumi', command=ShiFuMi)
bouton1.pack()
bouton2.pack()
bouton3.pack()
 
fenetre.mainloop()