import unittest
import HtmlTestRunner
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
class CrearProductoTest(unittest.TestCase):
    def setUp(self):
        driver_options=Options()
        #driver_options.add_argument("--headless")
        driver_options.add_argument("start-maximize")
        #driver_options.add_argument("window-size=800*600")
        driver_path=r"C:\taller3\taller3\browser\chrome\chromedriver-win64\129.0.6668.58\chromedriver.exe"
        binary_path=r"C:\taller3\taller3\browser\chrome\chromedriver-win64\129.0.6668.58\chrome.exe"
        service=Service(driver_path)
        self.driver=webdriver.Chrome(service=service,options=driver_options)
        self.driver.implicitly_wait(4)
        self.wait=WebDriverWait(self.driver,3)

    def test_crear_producto(self):
        driver=self.driver
        wait=self.wait
        driver.get("http://localhost:9000/admin/cliente/cliente/add/")
    
        user='admin'
        password=12345678
        apellidos='Tester_'+ str(random.randint(10, 20))
        nombres='Juan'
        correo='test@pruebas.com'
        direccion='LIMA'


        user_input=driver.find_element(By.NAME,"username")
        user_input.send_keys(user)
        password_input=driver.find_element(By.NAME,"password")
        password_input.send_keys(password)
        driver.save_screenshot("login_credenciales.png")
        btn_login=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-form"]/div[3]/input')))
        btn_login.click()
        driver.save_screenshot("pagina_principal.png")
        apellidos_input=driver.find_element(By.NAME,"apellidos")
        apellidos_input.send_keys(apellidos)
        nombres_input=driver.find_element(By.NAME,"nombres")
        nombres_input.send_keys(nombres)
        correo_input=driver.find_element(By.NAME,"correoelectronico")
        correo_input.send_keys(correo)
        direccion_input=driver.find_element(By.NAME,"direccion")
        direccion_input.send_keys(direccion)
        driver.save_screenshot("llenar_formulario.png")
        time.sleep(2)
        btn_save=wait.until(EC.element_to_be_clickable((By.NAME,'_save')))
        btn_save.click()
        time.sleep(2)
        driver.save_screenshot("cliente_creados.png")

        editar=wait.until(EC.element_to_be_clickable((By.XPATH,f"//a[text()='{apellidos} {nombres}']")))
        editar.click()
        time.sleep(5)

        new_name='Camilo_'+ str(random.randint(10, 20))
        nombres_input=driver.find_element(By.NAME,"nombres")
        nombres_input.clear()
        nombres_input.send_keys(new_name)
        btn_save=wait.until(EC.element_to_be_clickable((By.NAME,'_save')))
        btn_save.click()
        time.sleep(2)
        driver.save_screenshot("cliente_actualizado.png")



    def tearDown(self) :
        if self.driver:
         self.driver.quit()
         return super().tearDown()

def suite():
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(CrearProductoTest))

    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
        output="reportes",
        report_name="crear_producto",
        report_title="Crear nuevo producto usando selenium",
        combine_reports=True,
        add_timestamp=True
    )
    runner.run(suite())
