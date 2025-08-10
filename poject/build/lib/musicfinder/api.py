from ddgs import DDGS, exceptions as ddgsexceptions
from requests import get, exceptions 


from typing import Literal, Union, Any
from bs4 import BeautifulSoup

class Finder:
    def __init__(self, search_type:Literal['music', 'video'], proxy:str = None):
        self.ddgs = DDGS(proxy)
        self.search_type = search_type.lower()

        if search_type == 'video':
            self.__end = '.mp4' or '.mkv'
        
        if search_type == 'music':
            self.__end = '.mp3'
    
    def search(self, prompt:str) -> Union[list[dict, Any], str]:
        # SEARCH IN WEB
        try:
            results:list = self.ddgs.text(
                query=prompt,
                max_results=10
            )
        
        except ddgsexceptions.TimeoutException:
            return 'Timeout Erorr, check internet or proxy'

        
        # ADD DOWNLOAD LINK
        for i in range(10):
            page_url = results[i]['href']
            try:
                response = get(page_url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    # To avoid errors
                    href = a.get('href', 'Not_found')
                    if href.endswith(self.__end):
                        results[i]['download_url'] = href
                        break
            
            except exceptions.ConnectionError:
                continue

            except exceptions.InvalidURL:
                continue
                
        return results