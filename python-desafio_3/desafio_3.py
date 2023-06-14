import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

#Dimensões da tela: 1920 x 1080

# Inicializar o WebDriver do Chrome
driver = webdriver.Edge()

# Acessar o site do Trivago
driver.get("http://www.trivago.com.br")
time.sleep(10)

search_form = driver.find_element(By.XPATH, "//span[@data-testid='search-form-destination-value']")
search_form.click()
time.sleep(5)

# Digitar "Manaus" no campo de busca
search_input = driver.find_element(by=By.ID, value="input-auto-complete")
search_input.click()
search_input.click()
search_input.send_keys("Manaus")
time.sleep(5)
#Clicar enter
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(5)

#Confirmar data
#Dia 05
datee_button = driver.find_element(by=By.XPATH, value="//*[@id='overlay-root']/div/section/main/div/div/div/div[2]/div[1]/div/button[9]/time")
datee_button.click()
#Dia 06
datee_button = driver.find_element(by=By.XPATH, value="//*[@id='overlay-root']/div/section/main/div/div/div/div[2]/div[1]/div/button[10]/time")
datee_button.click()
time.sleep(5)

#Aplicar Data
apply_button = driver.find_element(by=By.XPATH, value="//*[@id='overlay-root']/div/section/footer/div/div/div/button[2]")
apply_button.click()
time.sleep(5)

#Confirmar reserva
reserva_button = driver.find_element(by=By.XPATH, value="//*[@id='overlay-root']/div/section/footer/div/div/div/button[2]")
reserva_button.click()
time.sleep(5)

#Clicar em pesquisar
pesquisa_button = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div[1]/div[1]/section/div[2]/div[2]/div/button")
pesquisa_button.click()
time.sleep(5)

#Screenshot da tela de requisição
driver.save_screenshot("tela_de_requisicao.png")
print("Screenshot da tela de requisicao!")
time.sleep(3)

#Tempo de espera da requisicao do site
time.sleep(50)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(50)

# Dimensões da tela
largura, altura = pyautogui.size()
print(f"Dimensões da tela: {largura} x {altura}")

# Obtém a posição atual do cursor
posicao_atual = pyautogui.position()
print(f"Posição atual do cursor: {posicao_atual.x}, {posicao_atual.y}")

# Coordenadas do botão de pesquisa
x = 897
y = 239

# Movre o mouse para as coordenadas do botão de pesquisa e clica
pyautogui.moveTo(x, y)
pyautogui.click()

#filtrar por avaliacao
avaliacao_filtro = driver.find_element(by=By.XPATH, value="//*[@id='sorting-selector']/option[2]")
avaliacao_filtro.click()
time.sleep(5)
pyautogui.press('enter')

#clicar fora para sumir a tela de filtro
x = 447
y = 393
pyautogui.moveTo(x, y)
pyautogui.click()

time.sleep(10)
time.sleep(10)

#Screenshot da tela de avaliação
driver.save_screenshot("avaliacao.png")
print("Screenshot do primeiro resultado!")
time.sleep(3)

driver.quit()





