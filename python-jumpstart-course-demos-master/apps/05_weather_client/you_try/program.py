import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    # print the header
    print_header()
    # get zipcode from user
    zipcode = input('What zipcode do you want the weather for (11372)?\n')
    # get html from web
    html = get_html_fom_web(zipcode)
    # parse html
    report = get_weather_from_html(html)
    # display the forcast
    print ('The temp in {} is {}{} and {}'.format(
        report.loc, report.temp, report.scale, report.cond
    ))


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


def clean_up_text(text : str): # (param : type) => type hints to give vaiable meaning
    if not text:
        return text
    text = text.strip()
    return text


def find_city_state_from_loc(loc : str):
    return loc.split('\n')[0].strip()


def get_weather_from_html(html):
    cityCss = 'div#location h1'
    weatherConditionCss = 'div#curCond span.wx-value'
    weatherTempCss = 'div#curtemp span.wx-data span.wx-value'
    weatherScaleCs = 'div#curtemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    
    loc = clean_up_text(loc)
    loc = find_city_state_from_loc(loc)
    condition = clean_up_text(condition)
    temp = clean_up_text(temp)
    scale = clean_up_text(scale)

    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

if __name__ == '__main__':
    main()
