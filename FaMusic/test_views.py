from unittest import TestCase
import requests


class Test(TestCase):
    cookies = None

    def test_reg(self):
        payload = dict(username="faquan.yao", password="000000", phone_number="18219142019",
                       email="yaofaquan123@sina.com", intro="this is me")
        files = dict(avatar=open("photo.png", "rb"))
        r = requests.post("http://127.0.0.1:8000/FaMusic/register", data=payload, files=files)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

    def test_login(self):
        payload = dict(username="faquan.yao", password="123456")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        payload = dict(username="faquan.yao", password="000011")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        payload = dict(username="faquan.yao", password="000000")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')
        self.cookies = r.cookies

    def test_logout(self):
        r = requests.post("http://127.0.0.1:8000/FaMusic/logout")
        print(r.status_code)
        print(r.text)

    def test_queryMusic(self):
        payload = dict(username="faquan.yao", password="000000")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        r = requests.post("http://127.0.0.1:8000/FaMusic/queryMusic", cookies=r.cookies)
        print(r.status_code)
        print(r.text)

    def test_upload_music(self):
        payload = dict(username="faquan.yao", password="000000")
        r = requests.post("http://127.0.0.1:8000/FaMusic/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        files = dict(data=open("Jam - 七月上.mp3", 'rb'),
                     album_pic=open("photo.png", "rb"))
        payload = dict(title="七月上", author="Jam", album="Jam", album_inf="Jam's music",
                       time="1234")
        r = requests.post("http://127.0.0.1:8000/FaMusic/uploadMusic", data=payload, files=files, cookies=r.cookies)
        print(r.status_code)
        print(r.text)
