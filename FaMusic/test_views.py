from unittest import TestCase
import requests


class Test(TestCase):
    #urlbase = "http://120.79.203.124:8090/FaMusic"
    urlbase = "http://127.0.0.1:8000/FaMusic"

    def test_reg(self):
        payload = dict(username="faquan.yao", password="123456", phone_number="12345678910",
                       email="yaofaquan123@sina.com", intro="this is me")
        files = dict(avatar=open("photo.png", "rb"))
        r = requests.post(f"{self.urlbase}/register", data=payload, files=files)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

    def test_login(self):
        payload = dict(username="faquan.yao", password="00000")
        r = requests.post(f"{self.urlbase}/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        payload = dict(username="faquan.yao", password="000011")
        r = requests.post(f"{self.urlbase}/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        payload = dict(username="faquan.yao", password="123456")
        r = requests.post(f"{self.urlbase}/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')
        self.cookies = r.cookies

    def test_logout(self):
        r = requests.post(f"{self.urlbase}/logout")
        print(r.status_code)
        print(r.text)

    def test_queryMusic(self):
        payload = dict(username="faquan.yao", password="123456")
        r = requests.post(f"{self.urlbase}/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        r = requests.post(f"{self.urlbase}/queryMusic", cookies=r.cookies)
        print(r.status_code)
        print(r.text)

        r = requests.get(f"{self.urlbase}/medias/avatar/faquan.yao/avatar_tVSUo9N.png", stream=True)
        file = open("photo_relocal.png", "wb")
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
        file.close()


    def test_upload_music(self):
        payload = dict(username="faquan.yao", password="123456")
        r = requests.post(f"{self.urlbase}/login", data=payload)
        print(r.status_code)
        print(r.text)
        for item in r.cookies:
            print(f'key = {item.name}, value = {item.value}')

        files = dict(data=open("Jam - ?????????.mp3", 'rb'),
                     album_pic=open("photo.png", "rb"))
        payload = dict(title="?????????", author="Jam", album="Jam", album_inf="Jam's music",
                       time="1234")
        r = requests.post(f"{self.urlbase}/uploadMusic", data=payload, files=files, cookies=r.cookies)
        print(r.status_code)
        print(r.text)
