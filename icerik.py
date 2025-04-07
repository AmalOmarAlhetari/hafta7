
import requests
from bs4 import BeautifulSoup

def content(url, filename="icerik.txt"):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tarih_tag = soup.find("time") 
    tarih = tarih_tag.getText().strip() if tarih_tag else "Tarih bulunamadı"

    title_tag = soup.find("h1")
    baslik = title_tag.getText().strip() if title_tag else "No Title Found"

    content_tag = soup.find("div", attrs={"class": "haber-metin"})
    icerik = content_tag.getText().strip() if content_tag else "No Content Found"

 
    with open(filename, "w", encoding="utf-8") as file:
        file.write("URL: {}\n".format(url))
        file.write("Tarih: {}\n".format(tarih))
        file.write("Başlık: {}\n".format(baslik))
        file.write("İçerik: {}\n".format(icerik))
        file.write("-" * 50 + "\n")

    print("kayıt edildi {}".format(filename))

    return baslik, icerik  

content('https://www.milligazete.com.tr')
