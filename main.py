import tkinter as tk
import requests
import time


def Previsao(event=None):
    API_KEY = 'sua chave da API OpenWeatherMap'  # Coloque a chave da API aqui
    entrada = textField.get()  # Pega a entrada do usuário
    print(f'Entrada informada: {entrada}')  # Verificação para ver se a função está sendo chamada
    cidade_pais = entrada.split()  # Divide a entrada em cidade e país
    cidade = " ".join(cidade_pais[:-1])  # Junta tudo exceto o último elemento como cidade
    pais = cidade_pais[-1] if len(cidade_pais) > 1 else ''  # O último elemento é o código do país se houver

    # Adiciona a verificação de país para formar o link
    if pais:
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&appid={API_KEY}&lang=pt_br&units=metric'
    else:
        link = f'https://api.openweathermap.org/data/2.5/weather?q={entrada}&appid={API_KEY}&lang=pt_br&units=metric'

    print(f'Link gerado: {link}')  # Verifica se o link da API foi construído corretamente
    
    try:
        requisicao = requests.get(link)
        print(f'Status da requisição: {requisicao.status_code}')  # Verifica o status da resposta
        requisicao_dic = requisicao.json()
        
        # Verifica se a requisição foi bem-sucedida
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
            print('Cidade não encontrada')
            label_error.config(text="Erro: Cidade não encontrada")  # Atualiza o texto do Label de erro


    except Exception as e:
        label1.config(text="Erro ao obter dados.")
        label2.config(text=str(e))
        print(f'Erro: {str(e)}')  # Exibe o erro no terminal para ajudar a depurar


# Configuração da interface gráfica
root = tk.Tk()
root.geometry('600x600')
root.title('Clima de Hoje')

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# Campo de texto para entrada da cidade e país
textField = tk.Entry(root, font=t, justify='center')
textField.pack(pady=30)
textField.focus()
textField.bind('<Return>', Previsao)  # Ao pressionar Enter, chama a função Previsao

# Labels para exibir as informações
label1 = tk.Label(root, font=t)
label1.pack()

label2 = tk.Label(root, font=f)
label2.pack()

# Adiciona um Label para mensagens de erro
label_error = tk.Label(root, font=("poppins", 30), fg="red", wraplength=550)  # Cor vermelha para o erro
label_error.pack(pady=10)  # Adiciona espaçamento

root.mainloop()
