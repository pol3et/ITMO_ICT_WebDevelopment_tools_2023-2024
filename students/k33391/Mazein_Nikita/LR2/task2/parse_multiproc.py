import multiprocessing as mp
from time import time
from db import get_session, Article
from urls import URLS
import requests
from bs4 import BeautifulSoup

urls = URLS

def parse_and_save(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='tm-title').get_text(strip=True)
    text = soup.find('div', class_='tm-article-body').get_text(strip=True)

    with next(get_session()) as session:
        article = Article(title=title, url=url, text=text)
        session.add(article)
        session.commit()
    print(f"Saved: {title}")

def mp_parse(urls):
    processes = []
    for url in urls:
        process = mp.Process(target=parse_and_save, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    start_time = time()
    mp_parse(urls)
    end_time = time()
    print(f"Multiprocessing finished in {end_time - start_time:.4f} seconds")