from customtkinter import *
import customtkinter
customtkinter.set_default_color_theme("green")
import random
from PIL import Image

class Pierre_papier_ciseaux():
    def __init__(self):
        self.score_Joueur=0
        self.score_Ordinateur=0
        self.nombre_de_jeu=20
        self.valeurs=["pierre", "papier","ciseaux"]

        # interface graphique(fenêtre principale)
        self.app = CTk()
        self.score_label=CTkLabel(self.app,fg_color="green",
                        text=f"""Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous""")
        self.score_label.pack(side="top", pady=(50,100),ipadx=10)
        # cadre du stade
        self.stade_frame=CTkFrame(self.app,width=500,height=400,fg_color="white")

        self.pc_frame=CTkFrame(self.stade_frame, fg_color="transparent",
                               width=250,border_width=1)
        self.pc_frame.pack(side="left", padx=10,pady=10)

        # label ordinateur
        self.ordinateurLabelImage = CTkLabel(self.pc_frame, text="", 
                                image=self.loard_image("images/ordi.jpg",200,150))
        self.ordinateurLabelImage.pack(side ="left", pady=20,padx=(10,0))
        # label ordinateur
        self.pc_label = CTkLabel(self.pc_frame, text="Ordinateur")
        self.pc_label.pack(side="left",padx=20)

        # cadre qui contient les boutons pierre-papier-ciseaux
        self.frameImages = CTkFrame(self.stade_frame,fg_color="transparent",
                                    width=250,border_width=1)
        # label joueur
        self.player_label = CTkLabel(self.frameImages, text="Vous")
        self.player_label.pack(side ="left", padx=(20,100))
        self.frameImages.pack(side="right",padx=10,pady=50)

        self.stade_frame.pack(padx=20,pady=20)
        self.ciseaux_button = CTkButton(self.frameImages,fg_color="transparent",hover_color="white",
                                border_width=1, 
                                text="", image=self.loard_image("images/ciseaux.jpg",50,30),
                                width=1,command=self.f_ciseaux)
        self.ciseaux_button.pack(padx=20,pady=(20,0))
        self.pierre_Button = CTkButton(self.frameImages,fg_color="transparent",hover_color="white",
                                border_width=1,  
                                image=self.loard_image("images/pierre.jpg",50,30),text='', 
                                width=5, corner_radius=5, command=self.f_pierre)
        self.pierre_Button.pack(pady=20)

        self.papier_Button = CTkButton(self.frameImages,fg_color="transparent",hover_color="white",
                                border_width=1,text="", 
                            image=self.loard_image("images/papier.jpg",50,30),
                            width=5, corner_radius=5, command=self.f_papier)
        self.papier_Button.pack(padx=20,pady=(0,20))

        self.replay_button = CTkButton(self.stade_frame,fg_color="green",hover_color="green",
                                border_width=1,text="Rejouer", 
                            width=5, corner_radius=5, command=self.replay)
        self.app.mainloop()

    def replay(self):
        self.score_Joueur=0
        self.score_Ordinateur=0
        self.nombre_de_jeu=20
        self.replay_button.place(x=330,y=1000)
        self.ciseaux_button.configure(state="normal")
        self.pierre_Button.configure(state="normal")
        self.papier_Button.configure(state="normal")
        self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
        self.pc_label.configure(text="Ordinateur",image=self.loard_image("",3,4))
        self.player_label.configure(text="Vous",image=self.loard_image("",3,4))
        
    def loard_image(self,image_file,x,y):
        try:
            image=CTkImage(light_image=Image.open(image_file),
                            dark_image=Image.open(image_file),
                            size=(x,y))
            return image 
        except:
            pass

    def decision(self,j1,j2):
        self.nombre_de_jeu -=1
        if self.nombre_de_jeu>=1:

            if str(j1) == str(j2):
                self.score_Joueur +=1
                self.score_Ordinateur +=1
                self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
                
            elif str(j1)=="papier" and str(j2) == "ciseaux":
                self.score_Ordinateur+=3
                self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
                
            elif str(j1)=="pierre" and str(j2) == "papier":
                self.score_Ordinateur+=3
                self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
                
            elif str(j1)=="ciseaux" and str(j2) == "pierre":
                self.score_Ordinateur+=3
                self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
            else:
                self.score_Joueur +=3
                self.score_label.configure(
                    text=f"Ordinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
        else:
            self.replay_button.place(x=340,y=130)
            self.score_label.configure(
                text=f"Fin du match Score final\nOrdinateur {self.score_Ordinateur}   :   {self.score_Joueur} Vous")
            self.ciseaux_button.configure(state="disabled")
            self.pierre_Button.configure(state="disabled")
            self.papier_Button.configure(state="disabled")

            if self.score_Joueur==self.score_Ordinateur:
                self.pc_label.configure(text="Match nul", image=self.loard_image("",4,3))
                self.player_label.configure(text="Match nul",image=self.loard_image("",4,3))
            elif self.score_Joueur>self.score_Ordinateur:
                self.pc_label.configure(text="",
                        image=self.loard_image("images/perdant.png",100,80))
                self.player_label.configure(text="",
                        image=self.loard_image("images/gagnant.png",100,80))
            else:
                self.pc_label.configure(text="",
                        image=self.loard_image("images/gagnant.png",100,80))
                self.player_label.configure(text="",
                        image=self.loard_image("images/perdant.png",100,80))
    
    def ordinateur_joue(self):
        self.ordinateurJouer = random.choice(self.valeurs).lower()
        if self.ordinateurJouer == "pierre":
            self.pc_label.configure(text="", 
                image=self.loard_image("images/pierre.jpg",50,30))
        elif self.ordinateurJouer == "ciseaux":
            self.pc_label.configure(text="", 
                image=self.loard_image("images/ciseaux.jpg",50,30))
        else: 
            self.pc_label.configure(text="", 
                image=self.loard_image("images/papier.jpg",50,30))

    # les actions du bouton pierre
    def f_pierre(self):
        self.ordinateur_joue()
        self.joueur = "pierre".lower()
        self.player_label.configure(text="", 
            image=self.loard_image("images/pierre.jpg",50,30))
        self.decision(self.joueur,self.ordinateurJouer)
             
    # les actions du boutons papier
    def f_papier(self):
        self.ordinateur_joue()
        self.joueur = "papier".lower()
        self.player_label.configure(text="", 
            image=self.loard_image("images/papier.jpg",50,30))
        self.decision(self.joueur,self.ordinateurJouer)
        
    def f_ciseaux(self):
        self.ordinateur_joue()
        self.joueur = "ciseaux".lower()
        self.player_label.configure(text="", 
            image=self.loard_image("images/ciseaux.jpg",50,30))
        self.decision(self.joueur,self.ordinateurJouer)
        
Pierre_papier_ciseaux()
