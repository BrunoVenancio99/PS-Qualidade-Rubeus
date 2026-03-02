import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URLS = [
    "https://qualidade.apprbs.com.br",
    "https://qualidade.apprbs.com.br/certificacao"
]

def test_status_http_200():
    for url in URLS:
        r = requests.get(url, timeout=10)
        assert r.status_code == 200

def test_tempo_carregamento():
    for url in URLS:
        r = requests.get(url, timeout=10)
        assert r.elapsed.total_seconds() < 4

def test_title_existe():
    for url in URLS:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        assert soup.title is not None
        assert len(soup.title.get_text().strip()) > 3

def test_meta_description():
    for url in URLS:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        meta = soup.find("meta", attrs={"name": "description"})
        assert meta is not None, f"{url} não possui meta description"
        assert len(meta.get("content", "").strip()) > 10, f"{url} meta description muito curta"