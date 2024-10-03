import tkinter as tk
from tkinter import PhotoImage
import requests
import time
import os

def previsao(event=None):
    API_KEY = 'sua chave da API OpenWeatherMap'  # Coloque a chave da API aqui
    entrada = textField.get()  # pega a entrada do usuário
    print(f'Entrada informada: {entrada}')  # verificação para ver se a função está sendo chamada
    cidade_pais = entrada.split()  # divide a entrada em cidade e país
    cidade = " ".join(cidade_pais[:-1])  # junta tudo menos o ultimo elemento como cidade
    pais = cidade_pais[-1] if len(cidade_pais) > 1 else ''  # o ultimo elemento eh o codigo do pais (se tiver)

    # tira a mensagem de erro toda vez que inicia a funcao (toda vez que o usuario apertar enter)
    label_error.config(text="")  # de fato tira a mensagem do erro

    # adiciona a verificação de país pra gerar o link
    if pais:
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&appid={API_KEY}&lang=pt_br&units=metric'
    else:
        link = f'https://api.openweathermap.org/data/2.5/weather?q={entrada}&appid={API_KEY}&lang=pt_br&units=metric'

    print(f'Link gerado: {link}')  # verifica se o link da API foi gerado direito
    
    try:
        requisicao = requests.get(link) # pega as informacoes da api
        print(f'Status da requisição: {requisicao.status_code}')  # verifica o status da resposta (200, 404 essas coisas)
        requisicao_dic = requisicao.json() # transforma em json para manipular
        
        # verifica se a requisição deu certo (200)
        if requisicao.status_code == 200:
            descricao = requisicao_dic['weather'][0]['description']
            sensacao = requisicao_dic['main']['feels_like']
            tempmax = requisicao_dic['main']['temp_max']
            tempmin = requisicao_dic['main']['temp_min']
            pressao = requisicao_dic['main']['pressure']
            velvento = requisicao_dic['wind']['speed']
            pais = requisicao_dic['sys']['country']
            nascerdosol = time.strftime('%I:%M:%S', time.gmtime(requisicao_dic['sys']['sunrise'] - 10800))
            pordosol = time.strftime('%I:%M:%S', time.gmtime(requisicao_dic['sys']['sunset'] - 10800))
            temperatura = requisicao_dic['main']['temp']
            umidade = requisicao_dic['main']['humidity']
            final_info = f'{descricao.title()}\n{temperatura}°C'
            final_data = (f'Sensação Térmica: {sensacao}°C\nUmidade: {umidade}%\nPressão: {pressao} hPa\n'
                          f'Temperatura Mínima: {tempmin}°C\nTemperatura Máxima: {tempmax}°C\n'
                          f'País: {pais}\nVelocidade do vento: {velvento} m/s\n'
                          f'Nascer do Sol: {nascerdosol}\nPôr do sol: {pordosol}')
            
            label1.config(text=final_info)
            label2.config(text=final_data)
        else:
            label1.config(text="")
            label2.config(text="")
            print('Cidade não encontrada') # (so pra mim isso)
            label_error.config(text="Erro: Cidade não encontrada")  # atualiza o texto do Label de erro

    # aqui é pra saber os erros detalahadamente e seta a mensagem que vai aparecer pro usuario quando der erro
    except Exception as e:
        label1.config(text="Erro ao obter dados.")
        label2.config(text=str(e)) # pega erro detalhado
        print(f'Erro: {str(e)}')  # mostra erro detalhado no terminal (so pra mim isso)


# configuracoes basicas da interface 
app = tk.Tk() # cria a interface do tkinter
app.geometry('600x500') # deixa o tamanho do aplicativo com 600px largura e 500px de altura
app.title('Clima de Hoje') # titulo do aplicativo (na janela)
description = ("poppins", 15, "bold") # fonte para a descricao (Menor)
heading = ("poppins", 35, "bold") # fonte para o heading (Maior)

# isso aqui garante que o icone vai ser achado quando converter pro executavel (pyinstaller)
caminho_icone = os.path.join(os.path.dirname(__file__), 'WeatherAppIcon.png')
icon = PhotoImage(file=caminho_icone)
app.iconphoto(False, icon)


# configuracao da entrada da cidade na interface
textField = tk.Entry(app, font=heading, justify='center')
textField.pack(pady=30)
textField.focus()
textField.bind('<Return>', previsao)  # quando der entra chama a funcao previsao

# labels para exibir as informações
label1 = tk.Label(app, font=heading)
label1.pack()

label2 = tk.Label(app, font=description)
label2.pack()

# de fato adiciona o label da mensagem de erro
label_error = tk.Label(app, font=heading, fg="red", wraplength=550)  # cor vermelha para o erro e maximo de pixels para nao passar do tamanho da tela
label_error.pack(pady=10)

app.mainloop()
