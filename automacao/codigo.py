#Passo a passo do projeto 
#1 Entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#2 Pip install pyautogui, biblioteca para automatizaçao
import pyautogui
import time

pyautogui.PAUSE = 2
# apertar tecla do windows (command + barra de espaço)
pyautogui.press("win")
# digita nome do programa (chrorme)
pyautogui.write("chrome")
# apertar enter 
pyautogui.press("enter")
# digitar link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"    
pyautogui.write(link)
# apertar enter 
pyautogui.press("enter")
#espere 5 segundos pois o site pode demorar abrir, importar biblioteca time
time.sleep(3)

#3 Fazer login
pyautogui.click(x=444, y=371)
#digitar o email
pyautogui.write("contatoglibrelon@gmail.com")
#passar para o campo de senha 
pyautogui.press("tab")
#digitar senha
pyautogui.write("minhasenha123")
#logar
pyautogui.click(x=669, y=537)
time.sleep(2)

#5 importar base de dados
#abrir cmd no VS pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #4 Cadastrar produtos 

    pyautogui.click(x=568, y=258)
    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write (tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # ou "1"
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    #rolar para começar adicionar novo produto
    pyautogui.scroll(4000)
    #colocar todas as informaçoes de produtos dentro do for selecionando todos os produtos e dando um tab



    #5 Repetir ate acabar dados