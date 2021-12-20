# import csv
# from typing import List
# import requests
# from lxml import html

# from entities import Link


# class Searcher:

#     def __init__(self, url: str) -> None:
#         self._url = url

#     def run(self) -> List[Link]:

#         links = list()
#         page = requests.get(self._url).content
#         page_html = html.fromstring(page)
#         result = page_html.xpath('//a[@href]/@href')
#         for link in result:
#             if 'https' in link or 'http' in link:
#                 value = Link(link)
#                 links.append(value)
#         return links

# class Keeper:

#     def __init__(self) -> None:
        
#         self._name_file = ""

#     def save(self, name_file, path_to_save):

        
