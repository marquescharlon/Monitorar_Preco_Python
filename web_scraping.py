from bs4 import BeautifulSoup
import requests
import send_email as email
import security


def monitoramento(EnviarEmail: bool):

    URL = 'https://www.magazinevoce.com.br/magazineqro/apple-iphone-14-pro-max-128gb-preto-espacial-67-48mp-ios-5g/p/235924800/TE/14PM/'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    title = soup.find('h3', class_='hide-mobile').get_text().strip()
    title = title[0:63]
    price = soup.find('div', class_='p-price').get_text().strip()

    # Se eu quiser converter o valor em float
    num_price = price[3:11]
    num_price = num_price.replace('.', '')
    num_price = num_price.replace(',', '.')
    num_price = float(num_price)

    mensagem = title
    mensagem += ' | '
    mensagem += 'R$ ' + str(num_price).replace('.', ',')
    mensagem += ' | '
    mensagem += URL

    if EnviarEmail == True:
        if (num_price < 9000):
            email.send_email(destinatario=security.username_email,
                             assunto=title, mensagem=mensagem)
    else:
        print("Não foi permitido enviar o e-mail.")


if __name__ == '__main__':
    monitoramento(EnviarEmail=False)
