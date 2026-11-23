"""
Interface Gráfica do Aplicativo Pomodoro usando python/tkinter
Programação Orientada a Objetos (POO)
Gerado por: Wesin Ribeiro
"""
from tkinter import *
from pathlib import Path
from math import floor

#########################################
BEIGE = "#FEF3E2"
GOLD = "#F4AE52"
ORANGE = "#D4621A"
BLACK = "#2A1A0E"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
########################################

class Pomodoro:
    def __init__(self):
        self.window = None 
        self.session = None
        self.status = None
        self.can = None
        self.img = None
        self.timer = None
        self.timer_text = None
        self.reps = 0
        self.session_number = 0
        self.create_gui()

    ############## TIMER RESET ##############
    def reset_timer(self):
        pass

    ############# TIMER START ###############
    def start_timer(self):
        self.reps += 1

        if self.reps % 8 == 0:
            self.countdown(LONG_BREAK_MIN)
            self.status.config(text="Long Break")
        elif self.reps % 2 == 0:
            self.countdown(SHORT_BREAK_MIN)
            self.status.config(text="Break")
        else:
            self.countdown(WORK_MIN)
            self.session_number += 1
            self.status.config(text="Work")
            self.session.config(text=f"Sessão: {self.session_number}")
            if self.session_number % 4 == 0:
                self.session.config(text=f"Sessão: {self.session_number} \n ✅ Bom trabalho!")
                self.reset_timer()

    ############ MECANISMO DE CONTAGEM #####
    def countdown(self, count):

        minutes = floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"

        self.can.itemconfig(self.timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            self.timer = self.window.after(1000, self.countdown, count-1)
        else:
            self.start_timer()

    ########### CRIAR INTERFACE GRÁFICA ####
    def create_gui(self):

        ########## Janela Principal #############
        self.window = Tk()
        self.window.geometry("300x370")
        self.window.config(padx=5, pady=5, bg=BEIGE)
        self.window.title("Pomodoro")

        self.status = Label(
            text="Timer",
            fg=ORANGE,
            bg=BEIGE,

            font=("Arial",20,"normal")
        )
        self.status.pack()

        self._create_canvas()
        self._create_buttons()

        ######### Sessões ##################
        self.session = Label(
            text="",
            fg=BLACK,
            bg=BEIGE,

            font=("Arial",14,"normal")
        )
        self.session.pack()
        #return self.window

    def _create_canvas(self):
        ######### Canva Tomate ##################
        path = Path(__file__).parent
        self.img = PhotoImage(file=path / "tomato.png")
        self.can = Canvas(self.window, bg=BEIGE, highlightthickness=0)
        self.can.pack()
        w = self.img.width() + 18
        h = self.img.height()
        self.can.config(width=w, height=h)
        self.can.create_image(w//2, h//2, image=self.img)
        self.timer_text = self.can.create_text(w//2, h//2, text="00:00", font=("Arial", 20, "bold"), fill=BLACK)

    def _create_buttons(self):
        ######### Botões ########################
        buttons = Frame(bg=BEIGE)
        buttons.pack()

        start = Button(buttons, text="Start", fg=ORANGE, font=("Arial", 14, "normal"), bd=0)
        start.config(command=self.start_timer)
        start.pack(side=LEFT, padx=5, pady=5)

        reset = Button(buttons, text="Reset", fg=ORANGE, font=("Arial", 14, "normal"), bd=0)
        reset.config(command=self.reset_timer)
        reset.pack(side=RIGHT, padx=5, pady=5)


if __name__ == "__main__":
    app = Pomodoro()
    app.window.mainloop()
