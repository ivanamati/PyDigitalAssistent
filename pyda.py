import wolframalpha
import wikipedia

#library za sintezu govora
import pyttsx3

# Import customtkinter module
import customtkinter as ctk

 
# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System")       
 
# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("green")   
 
# Create App class
class My_Py_Asisstant_App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My Py Digital Asisstant ")   
        self.geometry("500x150")   
 
        # Name Label
        self.greetinglabenl = ctk.CTkLabel(self,
                                      text="How can IPy help you?")
        self.greetinglabenl.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.korisnikovo_pitanje = ctk.CTkEntry(self,
                         placeholder_text="your input here", width=300)
        self.korisnikovo_pitanje.grid(row=0, column=1,
                            columnspan=3, padx=10,
                            pady=20, sticky="ew")
        
        # korisnikov_upit = self.korisnikovo_pitanje.get()

        # OK Button
        self.gumb_za_rezutat = ctk.CTkButton(self,
                                         text="OK", 
                                         #command=lambda: self.popup_prozor(upit=self.korisnikovo_pitanje.get()),
                                         command=self.popup_prozor,
                                         #self.dohvacanje_unosa, 
                                         width=10)
        self.gumb_za_rezutat.grid(row=1, column=1,                                   
                                        padx=10, pady=10,
                                        sticky="ew")
        self.gumb_cancel = ctk.CTkButton(self, text="Cancel", command=self.izlaz_iz_app,width=10)
        self.gumb_cancel.grid(row=1, column=2, sticky="ew", pady=20)

        # try:
        # #     wiki_res = wikipedia.summary(self.korisnikovo_pitanje.get(), sentences=2)
        #     wolfram_res = next(client.query(self.korisnikovo_pitanje.get()).results).text
        #     return wolfram_res
        # except:
        #     return Exception


    def popup_prozor(self):
        popup_window = ctk.CTkToplevel()
        popup_window.grab_set() 
        popup_window.title("Message")
        popup_window.geometry("600x250")

        odgovor = self.ispis_odgovora_na_korisnikov_input()

        popup_label = ctk.CTkLabel(popup_window, text="the answer is:")
        popup_label.pack(pady=10)
        popup_answer = ctk.CTkLabel(popup_window, text=odgovor, wraplength=500)
        popup_answer.pack(pady=20)

        popup_button = ctk.CTkButton(popup_window, text="GO BACK",
                                     command=popup_window.destroy)
        popup_button.place(anchor="center",relx=0.5, rely=0.8)


    def ispis_odgovora_na_korisnikov_input(self):
        client = wolframalpha.Client("ATVE7L-94QT4PX37R")
        #client=wolframalpha.Client("lilpumpsaysnopeeking")

        # voice engine for digital asisstent
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id) # ili "voices[0].id" ovisno o željenom glasu

        # user input
        upit = self.korisnikovo_pitanje.get()

        try:
            wiki_rezultat = wikipedia.summary(upit, sentences=2)
            # engine.say(wiki_rezultat)
            # engine.runAndWait()
            return wiki_rezultat
            #sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)

        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(upit).results).text
            engine.say(wolfram_res)
            engine.runAndWait()
            return wolfram_res

        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(upit).results).text
            engine.say(wolfram_res)
            engine.runAndWait()
            return wolfram_res

        except:
            engine.say("Im sorry, I can't find the answer to your question")
            engine.runAndWait()
            return "An exception has occurred!"
                  

    def dohvacanje_unosa(self):
        vas_unos = self.korisnikovo_pitanje.get()
        print("Upisali ste:", vas_unos)

    def izlaz_iz_app(self):
        self.destroy()
        
        
if __name__ == "__main__":
    app = My_Py_Asisstant_App()
    # Runs the app
    app.mainloop()


# def ispis_odgovora_na_korisnikov_input():
#         # #return(self.korisnikovo_pitanje.get())
#         # return "hej"
#         #print(upit)
#         #return upit
#         upit = "3+3"
#         try:
#             #wiki_res = wikipedia.summary(upit, sentences=2)
#             wolfram_res = next(client.query(input="where is zagreb").results).text
#             #return wolfram_res
#             print (wolfram_res)
#             #engine.say(wolfram_res)
#             #sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
#         except wikipedia.exceptions.DisambiguationError:
#             wolfram_res = next(client.query(upit).results).text
#             #return wolfram_res
#             print (wolfram_res)
#             #engine.say(wolfram_res)
#             #sg.PopupNonBlocking(wolfram_res)
#         except wikipedia.exceptions.PageError:
#             wolfram_res = next(client.query(upit).results).text
#             #return wolfram_res
#             print (wolfram_res)
#             #engine.say(wolfram_res)
#             #sg.PopupNonBlocking(wolfram_res)
#         except:
#             print("An exception has occurred!")
        

# # client = wolframalpha.Client("3KJ4AR-A9JEVLY5Y9")
# # res = client.query('temperature in Washington, DC on October 3, 2012')
# # print(res)

# #ispis_odgovora_na_korisnikov_input()