import json
from bs4 import BeautifulSoup
class HtmlToJson:
    def __init__(self)-> None:
        self.__capitals=[]
    def parse(self, f)->json:
        self.__get_capitals(f)
        return self.__json_output()
    def __get_capitals(self, f)->None:
        for item in BeautifulSoup(f.read(), 'html.parser').find_all('li'):
            cap = item.strong.text.strip()
            stt = item.span.text.strip()
            self.__capitals.append({'capital':cap,'state':stt})
    def __json_output(self)->json:
        json_op={
            'capitals':self.__capitals,
            'summary':{
                'numberOfCapitals':len(self.__capitals)
            }
        }
        return json.dumps(json_op,indent=2)