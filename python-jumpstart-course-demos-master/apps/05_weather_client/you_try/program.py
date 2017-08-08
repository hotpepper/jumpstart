import requests


def main():
    # print the header
    print_header()
    # get zipcode from user
    zipcode = input('What zipcode do you want the weather for (11372)?\n')
    # get html from web
    html = get_html_fom_web(zipcode)
    # parse html
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


if __name__ == '__main__':
    main()
