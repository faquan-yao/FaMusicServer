from unittest import TestCase
import requests


class Test(TestCase):
    def test_reg(self):
        payload = dict(phone_number="18219142019", nick_name="faquan.yao", password="123456")
        files = dict(head_photo=open("photo.png", "rb"))
        r = requests.post("http://127.0.0.1:8000/FaMusic/register", data=payload, files=files)
        print(r.status_code)
        print(r.text)

    def test_login(self):
        payload = dict(account="1000014", password="123456")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)

    def test_unregister(self):
        payload = dict(nick_name="123456", password="123456")
        r = requests.post("http://127.0.0.1:8000/FaMusic/unregister", data=payload)
        print(r.status_code)
        print(r.text)
