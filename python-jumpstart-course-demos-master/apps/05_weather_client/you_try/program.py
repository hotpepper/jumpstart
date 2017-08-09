import requests
import bs4


def main():
    # print the header
    print_header()
    # get zipcode from user
    zipcode = input('What zipcode do you want the weather for (11372)?\n')
    # get html from web
    html = get_html_fom_web(zipcode)
    # parse html
    get_weather_from_html(html)
    # display the forcast


def print_header():
    print('------------------------------------')
    print('          WEATHER APP')
    print('------------------------------------')


def get_html_fom_web(zipcode):
    url = 'https://www.wunderground.com/us/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_weather_from_html(html):
    cityCss = 'div#location h1'
    weatherConditionCss = 'div#curCond span.wx-value'
    weatherTempCss = 'div#curtemp span.wx-data span.wx-value'
    weatherScaleCs = 'div#curtemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html5lib')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    print(condition, temp, scale)

if __name__ == '__main__':
    main()
