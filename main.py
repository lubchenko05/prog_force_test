"""
Python v3.6+ required because I'm using f strings.
"""


def parse_data(file):
    """
    Parse data from logs
    :param file: path to file
    :return: parsed data in format list(From, Message)
    """
    with open(file, 'r') as f:
        data = f.read()
        f.close()
    return [value for value in [(i.split('\n')[0], i.split("Subject: ")[1].split('X-Content-Type-Outer-Envelope:')[0])
                                if len(i.split('\n')[0]) > 0 and not i.split('\n')[0].startswith('-')
                                and not i.split('\n')[0].startswith('\n')
                                else None for i in data.split('\n\n\n\n')] if value]


def repr_message(data):
    """
    Represent data in format: From data: Subject
    :param data: parsed data in format list(From, Message)
    :return: None
    """
    for j in [f'{i[0]}: {i[1]}' for i in data]:
        print(j, end='')


def repr_count_of_message(data):
    """
    Counting how many messages was sent by email
    :param data: parsed data in format list(From, Message)
    :return: None
    """
    result = {}
    for i in data:
        email = i[0].split()[1]
        if email in result:
            result[email] += 1
        else:
            result[email] = 0

    for k, v in result.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    data = parse_data('mbox.txt')
    repr_message(data)
    print('\n-----------------------------------------------------------------------\n')
    repr_count_of_message(data)
