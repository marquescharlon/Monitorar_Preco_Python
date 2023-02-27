# Monitorar Preço usando Python
Verificar a cada período de tempo se o valor do produto baixou conforme desejado e ser notificado via e-mail. Por exemplo, será notificado caso o produto chegue a custar menos que oito mil reais.

#### Produto monitorado:
![image](https://user-images.githubusercontent.com/22162514/221469212-481ab040-051e-4d64-8609-443ca0e986e9.png)

#### Como irá receber o e-mail:
![image](https://user-images.githubusercontent.com/22162514/221457371-25d8a5d9-b793-4de8-8926-84028f479513.png)

![image](https://user-images.githubusercontent.com/22162514/221458278-e90b3de9-415e-4304-b313-0e1bc33c6b3e.png)

## Parâmetros

1. Informar o link ```URL=''``` do produto no arquivo **web_scraping.py**

2. Criar arquivo **security.py**, dentro dele você irá adicionar os parâmetros ```username_email``` e ```password_email```

> Por questões de segurança o Google já não permite mais o envio do e-mail utilizando apenas o usuário e a senha, para poder implementar o envio de e-mail na automatização será preciso utilizar a senha de app. Para isso, siga os seguintes passos:

- Acessar o e-mail
- Ir até ```Manage your Google Account```
- Clicar em ```Security```
- Em **Signing in to Google** você irá encontrar a opção ```App passwords```
- Selecionar ```E-mail```
- Selecionar o dispositivo ```Computador Windows```

> Se a opção ```App passwords``` não estiver aparecendo é porque você precisa ainda ativar à autenticação de dois fatores.

## Bibliotecas utilizadas
```BeautifulSoup```
```requests```
```smtplib```
```email.message```
```datetime```

## Etapas implementadas
- [x] Localizar o produto através do ```requests.get(URL, headers=headers)```
- [x] Extrair o título e o valor utilizando o ```BeautifulSoup```
- [x] Criar função para enviar e-mail ```send_email.py```
- [x] Criar arquivo ```security.py``` e proteger o usuário e a senha do e-mail 
- [x] Criar função ```monitoramento(EnviarEmail: bool)``` que determinar se deseja ser notificado por e-mail
- [x] Chamar a função ```web_scraping.monitoramento(EnviarEmail=True)``` no arquivo principal
- [x] Gerar o executável ```monitorar_preco.exe```
- [x] Adicionar ao gerenciador de tarefas do computador

## Backlog
- [ ] Monitorar mais de um produto
- [ ] Em diferentes lojas

## Gerar executável

Primeiro será necessário instalar a biblioteca PyInstaller que é responsável por gerar esse arquivo .exe: <br>
```
pip install PyInstaller
```
Agora, só acessar a raiz de seu projeto e executar o seguinte comando:
```
pyinstaller --onefile --noconsole monitorar_preco.py
```

Se utiliza alguma biblioteca sua ou de terceiros será necessário usar o seguinte comando **--paths=../** para gerar o executável.

```
pyinstaller --onefile --noconsole --paths=../ monitorar_preco.py
```

> Lembrando que monitorar_preco.py é o nome do arquivo principal, por isso, é informado na hora de gerar o executável.

# Conclusão

Se estou querendo muito um produto tenho à alternativa de deixar o site de uma loja aberta em uma aba no navegador e ir atualizando (F5) na medida que vou lembrando durante o dia, porém, pode ser que em algum momento esqueça e ainda não consiga pegar alguma promoção relâmpago. Neste caso, como o e-mail é uma ferramenta de trabalho, além disso, também sou notificado na tela do celular ao recebê-lo, então, é viável deixar que o Python faça esse monitoramento e envie uma notificação via e-mail quando o produto atingir o valor desejado.
