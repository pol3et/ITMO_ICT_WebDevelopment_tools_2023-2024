```python
import threading
import requests
from bs4 import BeautifulSoup
from time import time
from db import get_session, Article
from urls import URLS

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

def thread_parse(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=parse_and_save, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time()
    thread_parse(urls)
    end_time = time()
    print(f"Threading finished in {end_time - start_time:.4f} seconds")
```