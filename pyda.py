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
ctk.set_default_color_theme("blue")   
 
# Create App class
class My_Py_Asisstant_App:

    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("My Py Digital Asisstant ")   
        self.window.geometry("500x150")   
 
        # Label
        self.greetinglabenl = ctk.CTkLabel(self.window,
                                      text="How can IPy help you?")
        self.greetinglabenl.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Question entry
        self.korisnikovo_pitanje = ctk.CTkEntry(self.window,
                         placeholder_text="your input here", width=300)
        self.korisnikovo_pitanje.grid(row=0, column=1,
                            columnspan=3, padx=10,
                            pady=20, sticky="ew")
    
        # OK Button
        self.gumb_za_rezutat = ctk.CTkButton(self.window,
                                         text="OK", 
                                         command=self.popup_prozor_za_odgovor,
                                         width=10)
        
        # CANCEL button
        self.gumb_za_rezutat.grid(row=2, column=1,                                   
                                        padx=10, pady=10,
                                        sticky="ew")
        self.gumb_cancel = ctk.CTkButton(self.window, text="Cancel", command=self.izlaz_iz_app,width=10)
        self.gumb_cancel.grid(row=2, column=2, sticky="ew", pady=20)

        # combobox za odabir jezika pitanja i odgovora
        combobox_var = ctk.StringVar(value="choose the language")  # set initial value
        self.odabir_jezika_asistenta = ctk.CTkComboBox(master=self.window,
                                     values=["en", "de", "hr"],
                                     variable=combobox_var)
        self.odabir_jezika_asistenta.grid(row=1,column=1,padx=10,
                                        sticky="ew")


    def popup_prozor_za_odgovor(self):
        popup_window = ctk.CTkToplevel()
        popup_window.grab_set() 
        popup_window.title("Message")
        popup_window.geometry("600x400")     
        
        # ODGOVOR:
        odgovor = self.odgovor_na_korisnikov_input()
        popup_label = ctk.CTkLabel(popup_window, text="the answer is:")
        popup_label.pack(pady=10)
        # ovdje se ispsuje odgovor:
        popup_answer = ctk.CTkLabel(popup_window, text=odgovor, wraplength=550)
        popup_answer.pack(pady=20)


        # promjena jezika s obzirom na odabir korisnika
        engine = pyttsx3.init()
        odabrani_jezik = self.odabir_jezika_asistenta.get()
        print("vas odabrani jezik je: ", odabrani_jezik)

        if odabrani_jezik == "en":
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) # ili "voices[0].id" ovisno o željenom glasu
                    # this code helps that sound comes 1 second after the tekst
            self.window.after(1000, lambda: engine.say(odgovor))
            self.window.after(1000, engine.runAndWait)

        if odabrani_jezik == "de":
            german_voice_id = "com.apple.speech.synthesis.voice.anna"
            engine.setProperty('voice', german_voice_id)
                    # this code helps that sound comes 1 second after the tekst
            self.window.after(1000, lambda: engine.say(odgovor))
            self.window.after(1000, engine.runAndWait)

        elif odabrani_jezik == "hr":
            engine.stop()

        # GO BACK button
        popup_button = ctk.CTkButton(popup_window, text="GO BACK",
                                     command=popup_window.destroy)
        popup_button.place(anchor="center",relx=0.5, rely=0.8)


    def odgovor_na_korisnikov_input(self):

        client = wolframalpha.Client("ATVE7L-94QT4PX37R")

        # user input
        upit = self.korisnikovo_pitanje.get()
        odabrani_jezik = self.odabir_jezika_asistenta.get()
        print("sad cu govoriti na: ", odabrani_jezik, "jeziku.")

        try:
            wikipedia.set_lang(odabrani_jezik)
            wiki_rezultat = wikipedia.summary(upit, sentences=2)
            return wiki_rezultat

        except wikipedia.exceptions.DisambiguationError:
            wolfram_res = next(client.query(upit).results).text
            print("tražio sam na wolframu")
            return wolfram_res

        except wikipedia.exceptions.PageError:
            wolfram_res = next(client.query(upit).results).text
            print("i sada sam tražio na wolframu")
            return wolfram_res
        
        except:
            # voice engine for digital asisstent
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("I'm sorry, I can't find the answer to your question")
            engine.runAndWait()
            return "An exception has occurred!"
        

    def timeout_handler(signum):
    # Ova funkcija će se pozvati nakon isteka određenog vremena tijekom izvršavanja
    # upita i prekinuti izvršavanje programa
        return Exception("Vrijeme za izvršavanje upita je isteklo.")
                  

    # def dohvacanje_unosa(self):
    #     vas_unos = self.korisnikovo_pitanje.get()
    #     print("Upisali ste:", vas_unos)

    def izlaz_iz_app(self):
        self.window.destroy()
        
        
if __name__ == "__main__":
    app = My_Py_Asisstant_App()
    # Runs the app
    app.window.mainloop()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', 'de')
# engine.say("Dobar dan")
# engine.runAndWait()

# engine = pyttsx3.init()
# german_voice_id = "com.apple.speech.synthesis.voice.anna"
# engine.setProperty('voice', german_voice_id)

# čitanje teksta s njemačkim glasom
# engine.say("Guten Tag! Wie geht's Ihnen heute?")
# engine.runAndWait()


# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id) 
# engine.say("hello, i'm mary")
# engine.runAndWait()

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

#print(wikipedia.languages())