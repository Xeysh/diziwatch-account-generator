from colorama import Fore
import json
import sys
from Solution_Captcha import Solve


def captcha():
    print(Fore.YELLOW + "Captcha'yı siz çözüceksiniz.")

    captcha_data = Solve.ReCaptcha("6LeE7LAZAAAAAF0FSYKo4JGYLmdkH4jhjUg_9cXH",
                                   "https://diziwatch.net/sign-up/")["data"].strip("'")

    captcha_token = json.loads(captcha_data)["Solution"]

    with open("captcha.txt", "a") as f:
        f.write(captcha_token + "\n")
        sys.exit(0)


if __name__ == "__main__":
    captcha()
