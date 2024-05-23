import os
import requests
from bs4 import BeautifulSoup

def download_images(fruit, num_images):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    url = f"https://www.google.com/search?q={fruit}&tbm=isch"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")

    if not os.path.exists(fruit):
        os.makedirs(fruit)

    downloaded = 0
    for i, img in enumerate(images):
        img_url = img.get("src")
        if img_url and img_url.startswith("http"):
            img_data = requests.get(img_url).content
            with open(f"{fruit}/{fruit}_{downloaded}.jpg", "wb") as handler:
                handler.write(img_data)
            downloaded += 1
            if downloaded >= num_images:
                break

download_images("mango", 20)
download_images("kiwi", 20)
download_images("orange", 20)
