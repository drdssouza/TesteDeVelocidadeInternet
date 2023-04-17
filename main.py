from tkinter import *
import speedtest

# Janela
janela = Tk()
janela.title("Speedtest")
janela.geometry("390x600")
janela.resizable(False, False)
janela.configure(bg="#162C39")

# Definições
def Check():
    teste = speedtest.Speedtest()

    velocidade_up = round(teste.upload()/(1024*1024), 2)
    camada_upload.config(text=velocidade_up)

    velocidade_down = round(teste.download()/(1024*1024), 2)
    camada_download.config(text=velocidade_down)
    camada_downloadprincipal.config(text=velocidade_down)

    servernames = []
    teste.get_servers(servernames)
    camada_ping.config(text=teste.results.ping)

# Configuracao do app
icone = PhotoImage(file='imgs/atalho.png')
janela.iconphoto(False, icone)

button = PhotoImage(file='imgs/botao2.png')
Button = Button(janela, image=button, bg="#162C39", bd=0,activebackground="#1a212d", cursor="hand2",command=Check)
Button.pack(pady=30)
bg = PhotoImage(file='imgs/ms.png')
Label(janela, image=bg, bg='#162C39').pack()

# Velocidade nas camadas
camada_ping = Label(janela, text="0", font="Airelon 15", bg="#162C39", fg="white")
camada_ping.place(x=60, y=200, anchor="center")

camada_download = Label(janela, text="0", font="Airelon 15", bg="#162C39", fg="white")
camada_download.place(x=180, y=200, anchor="center")

camada_upload = Label(janela, text="0", font="Airelon 15", bg="#162C39", fg="white")
camada_upload.place(x=310, y=200, anchor="center")

camada_downloadprincipal = Label(janela, text="00", font="Airelon 60", bg="#162C39", fg="white")
camada_downloadprincipal.place(x=195, y=390, anchor="center")

# Loop da janela
janela.mainloop()