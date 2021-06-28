from html.parser import HTMLParser
from urllib.request import urlopen, Request


def get_html(url):
    """获取页面响应
    :return http响应
    """
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=25) as f:
        data = f.read()
        print(f'Status: {f.status} {f.reason}')
    return data.decode("utf-8")


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__attr = ''

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__attr = 'Meeting'
        if tag == 'time':
            self.__attr = 'Time'
        if ('class', 'say-no-more') in attrs:
            self.__attr = 'Year'
        if ('class', 'event-location') in attrs:
            self.__attr = 'Location'

    def handle_endtag(self, tag):
        self.__attr = ''

    def handle_data(self, data):
        if self.__attr == 'Meeting':
            print(f'{self.__attr}:{data}')
        if self.__attr == 'Time':
            print(f'{self.__attr}:{data}')
        if self.__attr == 'Year':
            if data.isdecimal():
                print(f'{self.__attr}:{data}')
        if self.__attr == 'Location':
            print(f'{self.__attr}:{data}')
            print()


if __name__ == '__main__':
    result = get_html('https://www.python.org/events/python-events/')
    parser = MyHTMLParser()
    parser.feed(result)


'''
执行结果：
Status: 200 OK
Meeting:PyHEP 2021
Time:05 July – 09 July 
Location:Online

Meeting:SciPy 2021
Time:12 July – 18 July 
Location:Austin, TX, US

Meeting:EuroPython 2021
Time:26 July – 01 Aug. 
Location:Online

Meeting:PyOhio 2021
Time:31 July
Location:Online

Meeting:PyConline AU 2021
Time:10 Sept. – 12 Sept. 
Location:Online, Australia

Meeting:Kiwi PyCon
Time:17 Sept. – 19 Sept. 
Location:Ōtautahi/Christchurch, Aotearoa/New Zealand

Meeting:PyCon Namibia 2021
Time:18 June – 19 June 
Location:Windhoek, Namibia

Meeting:PyFest
Time:16 June – 18 June 
Location:Online 

'''