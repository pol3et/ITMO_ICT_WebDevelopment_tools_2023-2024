import aiohttp
from bs4 import BeautifulSoup
from time import time
from schemas import Article

async def parse_and_save(url, db_session):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.find('h1', class_='tm-title').get_text(strip=True)
            text = soup.find('div', class_='tm-article-body').get_text(strip=True)
            
            article = Article(title=title, url=url, text=text)
            db_session.add(article)
            db_session.commit()