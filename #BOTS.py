
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service


# Especifica la ruta al controlador del navegador web que deseas utilizar
driver_path = 'C:/Users/javie/Downloads/chrome.exe/chromedriver'
service = Service(executable_path=driver_path)

# Crea una instancia del controlador del navegador web
driver = webdriver.Chrome(service=service)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=chrome_options)
# Navega a la primera página web
driver.get('https://www.youtube.com/shorts/WMMzgF8FEd4')

# Espera 5 segundos
time.sleep(7)

# Navega a la segunda página web
driver.get('https://www.pornhub.com/view_video.php?viewkey=63f19019bd162')

# Espera 5 segundos
time.sleep(10)

# Navega a la segunda página web
driver.get('https://www.pornhub.com/view_video.php?viewkey=ph63a614e6ca69c')

# Espera 5 segundos
time.sleep(10)

# Navega a la segunda página web
driver.get('https://www.pornhub.com/view_video.php?viewkey=ph63a770d823aed')

# Espera 5 segundos
time.sleep(10)

# Cierra el navegador web
driver.quit()

