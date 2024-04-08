import random
import random_strings
import requests


class MailTmApi:
    def __init__(self) -> None:
        self.session = requests.session()
        self.session.headers = {
            'authority': 'api.mail.gw',
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9',
            'cache-control': 'no-cache',
            'origin': 'https://mail.tm',
            'pragma': 'no-cache',
            'referer': 'https://mail.tm/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

    def get_random_avaible_domain(self) -> str:
        """
        **Random olarak bir domain alır.**
        """
        response = self.session.get('https://api.mail.gw/domains')
        random_mail_domain = random.choice(response.json()["hydra:member"])["domain"]
        return random_mail_domain

    def get_random_mail(self, domain: str) -> dict[str, str]:
        """
        **Random olarak bir mail alır ve şifresini, tokenini alır.**
        """
        nickname = random_strings.random_hex(10)
        password = random_strings.random_hex(8)

        json_data = {
            'address': f'{nickname}@{domain}',
            'password': password,
        }

        response = self.session.post('https://api.mail.gw/accounts', json=json_data)

        dondurulen_json = response.json()
        dondurulen_json.update({'password': password})

        response = self.session.post('https://api.mail.gw/token', json=json_data)
        return {"email": f'{nickname}@{domain}', "password": password, "token": response.json()["token"]}

    def get_emails(self, mail_token) -> list[str]:
        """
        **Random olarak alınan mail'in mail kutusuna bakar.**
        """
        self.session.headers['authorization'] = f'Bearer {mail_token}'
        response = self.session.get('https://api.mail.gw/messages')
        return response.json()["hydra:member"]

# if __name__ == '__main__':
#     mail = MailTmApi()
#     domain = mail.get_random_avaible_domain()
#     random_mail = mail.get_random_mail(domain)["token"]
#     get_emails = mail.get_emails(random_mail)
#     print(get_emails)
