import requests
from lxml import html

from entities import Link, Links


class Searcher:

    def __init__(self, url: str) -> None:
        """Initialization of the link finder object
        Args:
            url (str): url where find links
        """
        self._url = url

    def run(self) -> Links:
        """Start search

        Returns:
            Links: object with found links
        """
        list_links = Links()
        page = requests.get(self._url).content
        page_html = html.fromstring(page)
        result = page_html.xpath('//a[@href]/@href')
        for link in result:
            if 'https' in link or 'http' in link:
                list_links.add(Link(link))
        return list_links
