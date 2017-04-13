import datetime


def print_header():
    print('-' * 50)
    print('          Birthday app')
    print('-' * 50)
    print()


def get_birthday_from_user():
    print('When were you born:\n')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_btwn_two_dates(org_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, org_date.month, org_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_info(days):
    if days < 0:
        print('Your birthday is in {} days'.format(-days))
    elif days > 0:
        print('You had your birthday already this year {} days ago'.format(days))
    else:
        print('Happy birthday')



def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_btwn_two_dates(bday, now)
    print_birthday_info(number_of_days)


main()
