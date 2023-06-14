import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("http://www.buscacep.correios.com.br/sistemas/buscacep/")
time.sleep(2)

#Inserindo CEP
end_element = driver.find_element(by=By.ID, value="endereco")
end_element.click()
end_element.send_keys("69005-040")
# Tirar screenshot da tela e salvar como "busca_cep.png"
driver.save_screenshot("busca_cep.png")
print("Screenshot da busca por CEP tirada!")
time.sleep(5)
#Click button
click_element = driver.find_element(by=By.ID, value="btn_pesquisar")
click_element.click()
time.sleep(5)
# Tirar screenshot da tela e salvar como "busca_cep.png"
driver.save_screenshot("busca_cep1.png")
print("Screenshot da busca por CEP tirada!")
time.sleep(3)

#Retornar pagina
click_element = driver.find_element(by=By.ID, value="btn_nbusca")
click_element.click()

#Novo Endereco
end_element = driver.find_element(by=By.ID, value="endereco")
end_element.click()
end_element.send_keys("Lojas Bemol")
# Tirar screenshot da tela e salvar como "busca_lojas_bemol.png"
driver.save_screenshot("busca_lojas_bemol.png")
print("Screenshot da busca por Lojas Bemol tirada!")
time.sleep(5)
#Click button
click_element = driver.find_element(by=By.ID, value="btn_pesquisar")
click_element.click()
time.sleep(5)
# Tirar screenshot da tela e salvar como "busca_lojas_bemol.png"
driver.save_screenshot("busca_lojas_bemol1.png")
print("Screenshot da busca por Lojas Bemol tirada!")
time.sleep(3)

#Retornar pagina
click_element = driver.find_element(by=By.ID, value="btn_nbusca")
click_element.click()

driver.quit()