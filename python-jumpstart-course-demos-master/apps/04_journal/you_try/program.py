def main():
    print_header()
    run_event_loop()


def print_header():
    print('-' * 50)
    print('          Journal app')
    print('-' * 50)
    print()


def run_event_loop():
    print('what do you want to do with your journal?\n')
    cmd = None
    journal_data = list()

    while cmd != 'X':
        cmd = input('[L]ist entries, [A]dd entries, E[x]it?\n').upper().strip()

        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entries(journal_data)
        elif cmd != 'X':
            print("Sorry we don't understand '{}'.\n".format(cmd))
    print('Done, good bye')


def list_entries(data):
    print('your journal entries\n')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx + 1, entry))


def add_entries(data):
    text = input('Type your entry, ,enter> to exit\n')
    data.append(text)


main()
