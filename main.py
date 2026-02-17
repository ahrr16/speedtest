# Importa as bibliotecas responsáveis pela medição da velocidade e pela janela
import speedtest
import tkinter as tk

# Cria a janela da aplicação
janela = tk.Tk()
janela.title("SpeedTest")

# Função para medir a velocidade da internet e mostrar os resultados na janela
def resultados():
    # Objeto prara realizar as medições
    teste = speedtest.Speedtest()

    # Mede a velocidade do download (em bits/s)
    v_download = teste.download()

    # Mede a velocidade do upload (em bits/s)
    v_upload = teste.upload()

    # mede o ping
    ping = teste.results.ping

    # Exibe os resultados na janela convertendo para megabits/s
    resultado_download = tk.Label(text=f'Velocidade download: {v_download / 10**6:.2f}', width=30, height=1)
    resultado_download.grid(row=1, column=1)

    resultado_upload = tk.Label(text=f' Velocidade upload: {v_upload / 10**6:.2f}', width=30, height=1)
    resultado_upload.grid(row=1, column=2)

    resultado_ping = tk.Label(text=f'Ping: {ping:.2f}', width=30, height=1)
    resultado_ping.grid(row=1, column=3)
    return resultado_download, resultado_upload, resultado_ping

resultados()



janela.mainloop()
