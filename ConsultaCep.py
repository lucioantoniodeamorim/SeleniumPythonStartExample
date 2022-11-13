from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#Seta a localização do chromedriver e cria uma instância do driver
driver = webdriver.Chrome("D:/driver/chromedriver.exe")

#Maximiza a tela
driver.maximize_window()

#Visita a url
driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php?t")

#Digita no camo de busca o cep 89209674
driver.find_element(By.ID, "endereco").send_keys("89209674")

#Clica no botão de pesquisa
driver.find_element(By.ID, "btn_pesquisar").click()

#Tempo de espera para ver o resultado - O teste não deve ter sleep, foi inserido neste código apenas por didática, a maneira correta é usar um Explicit wait
time.sleep(5)

#Pega o texto do campo de resposta da pesquis
resultado = driver.find_element(By.XPATH, "//*[@id='resultado-DNEC']/tbody/tr/td[1]").text

#Printa o conteúdo do campo - Aqui deveria estar a validação de que o conteúdo exibido é o conteúdo esperado, para isso usaríamos um framework de testes como TestNG ou Junit
print(resultado)

driver.close()
