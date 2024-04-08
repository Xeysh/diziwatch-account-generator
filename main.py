import string
import requests
from faker import Faker
from mailtm import MailTmApi
from colorama import Fore
import random
import sys
import time


class DiziWatch:
    def __init__(self) -> None:
        proxy = random.choice(open("proxy.txt", "r").readlines()).strip()
        if not proxy:
            raise Exception("'proxy.txt' is empty.")
        self.session = requests.Session()
        self.session.proxies = {'http': 'http://' + proxy.strip()}

    def generator(self) -> str:
        try:
            captcha = random.choice(open("captcha.txt", "r").readlines()).strip()
            if not captcha:
                raise ValueError(Fore.RED + "Captcha token boş, lütfen captcha.py'ı çalıştırın.")
        except FileNotFoundError:
            raise Exception(Fore.RED + "Captcha file is missing.")

        email = MailTmApi().get_random_mail(MailTmApi().get_random_avaible_domain())

        info = {
                       'action': 'register_action',
                       'username': Faker().word().lower() + "12347" + "".join(random.choices(string.digits, k=3)),
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
            with open("captcha.txt") as f:
                f.truncate(0)
            raise Exception(Fore.RED + f"Captcha tokeninin süresi dolmuş, lütfen captcha.py'ı çalıştırın.")

        return (Fore.GREEN + f"Başarıyla kayıt olundu. - {r.status_code}\n"
                             f"İsim: {info['username']}\n"
                             f"Parola: {info['passwrd']}\n"
                             f"Mail: {info['mail_id']}\n"
                             f"Mail Token: {email['token']}"
                )


if __name__ == "__main__":
    while True:
        time.sleep(2)
        try:
            print(DiziWatch().generator())
        except requests.exceptions.ConnectionError:
            print(Fore.RED + "Proxy'e bağlanırken sorun oluştu.")
            sys.exit(0)
        except Exception as e:
            print(Fore.RED + f"Bir hata oluştu: {e}")
            sys.exit(1)
