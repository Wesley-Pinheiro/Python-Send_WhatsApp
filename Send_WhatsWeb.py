#pinheirocfc@gmail.com
#https://github.com/Wesley-Pinheiro
#instrucoes em: https://youtu.be/78NoGpfiPpk

#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = ['PALMEIRAS FUT','CONDOMINIO AREZZO','FAMILIA 02','FUTEBOL 2020','CLIENTES 02']

#Mensagem - Mensagem que sera enviada
mensagem = 'Bom dia grupo '
mensagem2 = ' ,que o dia de voces seja iluminado'

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
midia = "/home/pinheirocfc/Imagens/bom-dia.jpg"

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem,mensagem2):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(str(mensagem) + str(contato) + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)

#Funcao que envia midia como mensagem
def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
    send.click()    

#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem,mensagem2)       
    enviar_midia(midia) 
    time.sleep(1)
