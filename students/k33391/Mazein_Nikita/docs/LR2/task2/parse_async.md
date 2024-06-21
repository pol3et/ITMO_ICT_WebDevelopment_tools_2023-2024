```python
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from time import time
from db import get_session, Article
from urls import URLS

urls = URLS

async def parse_and_save(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.find('h1', class_='tm-title').get_text(strip=True)
            text = soup.find('div', class_='tm-article-body').get_text(strip=True)
            
            with next(get_session()) as db_session:
                article = Article(title=title, url=url, text=text)
                db_session.add(article)
                db_session.commit()
            print(f"Saved: {title}")

async def async_parse(urls):
    tasks = [parse_and_save(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time()
    asyncio.run(async_parse(urls))
    end_time = time()
    print(f"Async/Await finished in {end_time - start_time:.4f} seconds")
```