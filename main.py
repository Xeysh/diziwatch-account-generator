import requests
from faker import Faker
from Solution_Captcha import Solve
import json
from mailtm import MailTmApi
from colorama import Fore
import random
import sys
import psutil

print(Fore.YELLOW + "Captcha'yı siz çözüceksiniz.")

class DiziWatch:

    def __init__(self) -> None:
        proxy = random.choice(open("proxy.txt", "r").readlines()).strip()
        if proxy == []:
            raise Exception("'proxy.txt' is empty.")
        self.session = requests.Session()
        self.session.proxies = {'http': 'http://' + proxy.strip()}

    def generator(self) -> str:
        captcha = Solve.ReCaptcha("6LeE7LAZAAAAAF0FSYKo4JGYLmdkH4jhjUg_9cXH",
                "https://diziwatch.net/sign-up/")["data"].strip("'")

        captcha_token = json.loads(captcha)["Solution"]

        email = MailTmApi().get_random_mail(MailTmApi().get_random_avaible_domain())["email"]

        info = {
                       'action': 'register_action',
                       'username': Faker().word().lower() + "12347",
                       'mail_id': email,
                       'passwrd': "whysoserius1",
                       'passwrd2': "whysoserius1",
                       'captcha': captcha_token
                       }

        r = self.session.post("https://diziwatch.net/wp-admin/admin-ajax.php",
                 headers={'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                 data=info
        )

        if r.status_code != 200:
            raise Exception(Fore.RED + f"Kayıt olunurken bir sorun oluştu. - {r.status_code}\n{r.text}")

        return Fore.GREEN + f"Başarıyla kayıt olundu. - {r.status_code}\nİsim: {info['username']}\nParola: {info['passwrd']}\nMail: {info['mail_id']}"

    @staticmethod
    def killer() -> None:
        """
        **Arkadaki Google Chrome'ları kapatır ve CPU'ya çok fazla yüklenmeyi durdurur.**

        **Bu fonksiyonu devre dışı bırakırsanız bilgisayarınızda donma, mavi ekran yaşayabilirsiniz.**
        :return:
        """
        for proc in psutil.process_iter(['pid', 'name']):
            if 'chrome.exe' in proc.info['name']:
                proc.kill()

if __name__ == "__main__":
    try:
        print(DiziWatch().generator())
        DiziWatch().killer()
    except Exception as e:
        print(Fore.RED + f"Bir hata oluştu: {e}")
        sys.exit(1)
