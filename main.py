import speedtest
import tkinter as tk

janela = tk.Tk()
janela.title("SpeedTest")

def resultados():

    teste = speedtest.Speedtest()

    vd = teste.download()

    vp = teste.upload()

    ping = teste.results.ping

    resultadod = tk.Label(text=f'Velocidade download: {vd / 10**6:.2f}', width=30, height=1)
    resultadod.grid(row=1, column=1)

    resultadou = tk.Label(text=f' Velocidade upload: {vp / 10**6:.2f}', width=30, height=1)
    resultadou.grid(row=1, column=2)

    resultadop = tk.Label(text=f'Ping: {ping:.2f}', width=30, height=1)
    resultadop.grid(row=1, column=3)
    return resultadod, resultadou, resultadop

resultados()



janela.mainloop()