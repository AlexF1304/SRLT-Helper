from webdriver_interface import WebdriverInterface

import sys


def main():
    wi = WebdriverInterface()
    wi.auth()

    try:
        wi.run_tcc()
    except KeyboardInterrupt:
        wi.close_and_quit()
        sys.exit(130)


if __name__ == "__main__":
    main()
