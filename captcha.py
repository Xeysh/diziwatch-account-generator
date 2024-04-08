from colorama import Fore
import json
import sys
from Solution_Captcha import Solve
import psutil


class Captcha:
    @staticmethod
    def captcha() -> None:
        print(Fore.YELLOW + "Captcha'yı siz çözüceksiniz.")

        captcha_data = Solve.ReCaptcha("6LeE7LAZAAAAAF0FSYKo4JGYLmdkH4jhjUg_9cXH",
                                       "https://diziwatch.net/sign-up/")["data"].strip("'")

        captcha_token = json.loads(captcha_data)["Solution"]

        with open("captcha.txt", "a") as f:
            f.write(captcha_token + "\n")
            sys.exit(0)

    @staticmethod
    def killer() -> None:
        """
        **Arkadaki Google Chrome'ları kapatır ve CPU'ya çok fazla yüklenmeyi durdurur.**

        **Bu fonksiyonu devre dışı bırakırsanız bilgisayarınızda donma, mavi ekran yaşayabilirsiniz.**
        :return:
        """
        for chrome in psutil.process_iter(['pid', 'name']):
            if 'chrome.exe' in chrome.name():
                chrome.kill()


if __name__ == "__main__":
    Captcha.captcha()
    Captcha.killer()
