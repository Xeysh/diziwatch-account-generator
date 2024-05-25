import string
import requests
from faker import Faker
import random


class DiziWatch:
    def __init__(self) -> None:
        self.session = requests.Session()

    def generator(self) -> str:

        info = {
                       'action': 'register_action',
                       'username': Faker().word().lower() + "12347" + "".join(random.choices(string.digits, k=3)),
                       'mail_id': Faker().free_email(),
                       'passwrd': "whysoserius1",
                       'passwrd2': "whysoserius1",
                       'captcha': "03AFcWeA5M_4H4iaRIte9tyPg8P9G6He7r2SbtCMD1KIfZSS70JxpOuxjTpbIDzHPqg0p-4ofOwYOOqBY0S2QVIgV9T6GKXj8w5rAUGwWUZFFid0dZT6iwbkGRn2y5O8DI-24G5onc6mUxaDeIrlB7OJYYoz242ScF9JB3rbZBanKazuGd7VtNP1k5KPu9uOu84B-rgBui8enEWpKYcxy61FylFmtE2gBGWep2AjUYKhVDmJ6r9ia9o4vG_kSngp9DeMOaEzohKMjjOmqiEM6-585Bh35kQFFRXg27MP01BF6dHX64GU6hTCQRGihTdt4XvuDPvp1uiUTXEIx3jPJkv785lnX3t3Xe0jlMUafiqBRm_6XrWD7YXjBtqJPyUn536epc0soVPOBDxlFz1s8FVFNBnmZpIDf7rx9a8xGi0dedRDrKqN6B591pJcxtUiR97cvlXhKFBUocSp_Qku8vkqYQjGiRP9nhzU4PmQ9Fi2eV1FVUyCqgYw-RNd-BbSSklo0X4bkpwmBZ_4gZav1LGOsQyHWt6EE0tOz5hVHQ5DDzueuNmcMSndHjGMciHced396EgcAiusy0pE8lGAe0Hi9Ty2V-3rU1MLZ1iD1mXvQMlDo6GIXLhV0Oe3nO5z4RRrDIMTFfxzmP_ADsb1S7UvMaRSyQB1Mat9RL23BDEqk1UCkYDEmevn8"
                       }

        r = self.session.post("https://diziwatch.net/wp-admin/admin-ajax.php",
                              data=info)

        if r.status_code != 200:
            raise Exception
        
        return f"Kayıt olundu." + "\n"


if __name__ == "__main__":
    while True:
        try:
            print(DiziWatch().generator())
        except requests.exceptions.ConnectionError:
            continue
