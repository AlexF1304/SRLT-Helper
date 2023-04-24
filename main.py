from webdriver_interface import WebdriverInterface

import os
import sys


def run(wd_i):
    while True:
        rma_number = input('Type RMA Number')
        wd_i.make_tcc_confirm(rma_number)


def main():
    wi = WebdriverInterface(os.getenv('WD_PATH', 'wd_path not defined'))
    wi.auth()

    try:
        run(wi)
    except KeyboardInterrupt:
        wi.close_and_quit()
        sys.exit(130)


if __name__ == "__main__":
    main()
