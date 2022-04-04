import tkinter as tk
import requests
import time
 

def Previsao(root):
    cidade = textField.get()
    API_KEY = '495532554bb4f8e0be118b424a1354c2'
    # variaveis tutorial link = f'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API_KEY}&lang=pt_br&units=metric'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric'
    
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
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

    final_info = descricao + '\n' + str(temperatura) + '°C' 
    final_data = f'Sensação Térmica: {sensacao}°C\nUmidade: {umidade}\nPressão: {pressao}\nTemperatura Mínima: {tempmin}\nTemperatura Máxima: {tempmax}\nPaís: {pais}\nVelocidade do vento: {velvento}\nNascer do Sol: {nascerdosol}\nPôr do sol: {pordosol}'
    label1.config(text = final_info)
    label2.config(text = final_data)


root = tk.Tk()
root.geometry('600x500')
root.title('Clima de Hoje')
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(root, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', Previsao)

label1 = tk.Label(root, font=t)
label1.pack()
label2 = tk.Label(root, font=f)
label2.pack()
root.mainloop()