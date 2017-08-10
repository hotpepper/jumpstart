import os
import platform
import subprocess
import cat_service

def get_or_creat_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pics'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new folder {}'.format(folder))
        os.makedirs(full_path)

    return full_path


def download_cats(folder):
    print ('Downloading cats...')
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print ('downloading cat {}'.format(name))
        cat_service.get_cat(folder, name)


def display_cats(folder):
    print('Displaying cats in window {}'.format(folder))
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder], shell=True   )
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])


def main():
    # print header
    print_header()
    # get or create folder
    folder = get_or_creat_output_folder()
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print('--------------------------')
    print('       Cat factory ')
    print('--------------------------')

if __name__ == '__main__':
    main()