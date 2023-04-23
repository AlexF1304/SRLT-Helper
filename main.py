from webdriver_interface import WebdriverInterface

import os


def run():
    wd_path = os.getenv('WD_PATH', 'wd_path not defined')
    wi = WebdriverInterface(wd_path)
    wi.auth()
    while True:
        rma_number = input('Type RMA Number')
        wi.make_tcc_confirm(rma_number)


if __name__ == "__main__":
    run()
