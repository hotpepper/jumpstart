import os

def get_or_creat_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pics'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new folder {}'.format(folder))
        os.makedirs(full_path)

    return full_path

def main():
    # print header
    print_header()
    # get or creat folder
    folder = get_or_creat_output_folder()
    # download cats
    # display cats
    pass

def print_header():
    print('--------------------------')
    print('       Cat factory ')
    print('--------------------------')

if __name__ == '__main__':
    main()