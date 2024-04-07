import requests
from faker import Faker
from mailtm import MailTmApi
from colorama import Fore
import random
import sys
import psutil


class DiziWatch:
    def __init__(self) -> None:
        proxy = random.choice(open("proxy.txt", "r").readlines()).strip()
        if not proxy:
            raise Exception("'proxy.txt' is empty.")
        self.session = requests.Session()
        self.session.proxies = {'http': 'http://' + proxy.strip()}

    def generator(self) -> str:
        try:
            with open("captcha.txt", "r") as f:
                captcha = f.read()
                if not captcha:
                    raise ValueError(Fore.RED + "Captcha token boş, lütfen captcha.py'ı çalıştırın.")

        except FileNotFoundError:
            raise Exception(Fore.RED + "Captcha file is missing.")

        email = MailTmApi().get_random_mail(MailTmApi().get_random_avaible_domain())

        info = {
                       'action': 'register_action',
                       'username': Faker().word().lower() + "12347",
                       'mail_id': email["email"],
                       'passwrd': "whysoserius1",
                       'passwrd2': "whysoserius1",
                       'captcha': captcha
                       }

        r = self.session.post("https://diziwatch.net/wp-admin/admin-ajax.php",
                              headers={'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                              data=info)

        if r.status_code != 200:
            raise Exception(Fore.RED + f"Kayıt olunurken bir sorun oluştu. - {r.status_code}\n{r.text}")

        elif r.status_code == 400:
            raise Exception(Fore.RED + f"Captcha tokeninin süresi dolmuş, lütfen captcha.py'ı çalıştırın.")

        return (Fore.GREEN + f"Başarıyla kayıt olundu. - {r.status_code}\n"
                             f"İsim: {info['username']}\n"
                             f"Parola: {info['passwrd']}\n"
                             f"Mail: {info['mail_id']}\n"
                             f"Mail Token: {email['token']}")

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
    try:
        print(DiziWatch().generator())
        DiziWatch().killer()
    except Exception as e:
        print(Fore.RED + f"Bir hata oluştu: {e}")
        sys.exit(1)
