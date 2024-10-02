# WeatherApp

O **WeatherApp** é um aplicativo em Python que fornece informações climáticas em tempo real. Usando a API OpenWeatherMap, o aplicativo permite que os usuários consultem as condições do clima de uma cidade especificando o nome da cidade e, opcionalmente, o código do país. A interface gráfica é construída com a biblioteca Tkinter, proporcionando uma experiência de usuário simples e intuitiva.

## Funcionalidades

- Consulta de clima atual para qualquer cidade.
- Exibição de informações como temperatura, sensação térmica, umidade, pressão atmosférica, velocidade do vento e horários do nascer e pôr do sol.
- Mensagens de erro informativas caso a cidade não seja encontrada.

## Instalação

### Requisitos

- Python 3.5 ou Superior
- Bibliotecas:
  - `requests`
  - `tkinter` (geralmente já incluída na instalação do Python)

### Como instalar

1. Clone este repositório:
    ```bash
    git clone https://github.com/ArturZuza/WeatherApp.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd WeatherApp
    ```

3. Instale a biblioteca `requests`:
    ```bash
    pip install requests
    ```

4. Adicione sua chave da API OpenWeatherMap no código, substituindo o valor em `API_KEY`.

## Uso

1. Execute o script:
    ```bash
    python nome_do_arquivo.py
    ```

2. Digite a cidade e o código do país (se necessário) no campo de texto e pressione `Enter` para obter as informações climáticas.

3. O aplicativo exibirá a descrição do clima, temperatura atual, sensação térmica, umidade, pressão, temperatura mínima e máxima, velocidade do vento e horários do nascer e pôr do sol.

## Exemplo de Uso

- Entrada: `Roma IT`
- Saída: `Céu limpo 20°C 
Sensação Térmica: 22°C
Umidade: 40%
Pressão: 1015 hPa
Temperatura Mínima: 18°C
Temperatura Máxima: 22°C
País: IT
Velocidade do vento: 3 m/s
Nascer do Sol: 06:30:00
Pôr do sol: 18:30:00`

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie um branch com sua nova feature: `git checkout -b minha-nova-feature`.
3. Faça commit das suas mudanças: `git commit -m 'Adicionada nova feature'`.
4. Envie suas mudanças para o branch: `git push origin minha-nova-feature`.
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
