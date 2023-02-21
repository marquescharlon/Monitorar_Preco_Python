import smtplib
import email.message
import security
from datetime import datetime


def send_email(destinatario: str = '', assunto: str = '', mensagem: str = ''):
    """
    destinatario='Quem irá receber o e-mail' \n
    assunto='Texto fixo ou usar variável'
    mensagem='Texto fixo ou usar variável'
    """

    atual = datetime.now()
    s2 = atual.strftime("%d/%m/%Y, %H:%M:%S")

    email_content = f"""
    {s2} | {mensagem} \n
    """

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = destinatario
    msg['To'] = destinatario
    password = security.password_email

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print("E-mail enviado com sucesso!")


if __name__ == '__main__':

    title = 'Apple iPhone 14 Pro Max 128GB Preto-espacial - 6,7” 48MP iOS 5G'
    URL = 'https://www.magazinevoce.com.br/magazineqro/apple-iphone-14-pro-max-128gb-preto-espacial-67-48mp-ios-5g/p/235924800/TE/14PM/'
    price = float(8009.99)

    mensagem = URL
    mensagem += ' | '
    mensagem += title
    mensagem += ' | '
    mensagem += str(price)

    send_email(destinatario=security.username_email,
               assunto=title, mensagem=mensagem)
