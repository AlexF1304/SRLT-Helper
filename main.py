from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

rma_number = input('Type RMA Number')
url = "https://srlt.msi.com/"
driver_service = Service(executable_path="E:\\Python\\Projects\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

try:

    def auth():
        driver.get(url=url)
        time.sleep(5)
        login_input = driver.find_element(By.ID, 'username')
        login_input.clear()
        login_input.send_keys("")
        login_input = driver.find_element(By.ID, 'password')
        login_input.clear()
        login_input.send_keys("")
        time.sleep(3)
        driver.find_element(By.ID, 'submit').click()  # submit_button


    driver.get('https://srlt.msi.com///Login/BrickHome?pid=901&sid=90108&')  # brick_home_button
    time.sleep(3)
    driver.get('https://srlt.msi.com/iFramePage/ASP_First_Page')  # asp_repair_v3_button
    time.sleep(3)
    driver.find_element(By.ID, 's2id_rcSiteName').click()  # pop-up_window
    time.sleep(3)


    def asp_selection():

        match rma_number[:3].upper():

            case "RAU":
                rma_service_type = 0
            case "RBV4":
                rma_service_type = 1
            case "RP4":
                rma_service_type = 2
            case "RPW":
                rma_service_type = 3
            case "DBV4":
                rma_service_type = 1
            case "DP4":
                rma_service_type = 2
            case "DPW":
                rma_service_type = 3
            case _:
                raise Exception('Wrong RMA Number')
        driver.find_elements(By.CLASS_NAME, 'select2-result-label')[rma_service_type].click()  # asp_choose


    time.sleep(8)
    driver.find_element(By.ID, 'rmano').click()
    driver.find_element(By.ID, 'rmano').send_keys(rma_number)  # rma_number_fill_field
    time.sleep(3)
    driver.find_element(By.ID, 'btnContinue').click()  # next_button
    time.sleep(10)
    driver.switch_to.frame(driver.find_element(By.ID, "IFRAME1"))
    time.sleep(3)
    driver.find_element(By.ID, 'txtErrorC')  # error_code
    driver.find_element(By.ID, 'txtErrorC').send_keys("NXSEV")
    driver.find_element(By.ID, 'txtRMAC')
    driver.find_element(By.ID, 'txtRMAC').send_keys("NXN00")
    driver.find_element(By.ID, 'txtRRemark')
    driver.find_element(By.ID, 'txtRRemark').send_keys("TCC CONFIRMED")
    time.sleep(3)
    driver.find_element(By.ID, 'Button4').click()
    time.sleep(10)
    driver.find_element(By.ID, 'Button5').click()
    time.sleep(3)
    driver.switch_to.alert.accept()

    time.sleep(60)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
