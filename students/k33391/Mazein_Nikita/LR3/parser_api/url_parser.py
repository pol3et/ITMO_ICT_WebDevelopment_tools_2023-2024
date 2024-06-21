import requests
from bs4 import BeautifulSoup
from models import Article
from celery_main import celery_app

@celery_app.task
def parse_and_save(url, db_session):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find('h1', class_='tm-title').get_text(strip=True)
        text = soup.find('div', class_='tm-article-body').get_text(strip=True)
        
        article = Article(title=title, url=url, text=text)
        db_session.add(article)
        db_session.commit()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")