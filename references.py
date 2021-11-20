PATH = 'logs.txt'


@get_log(FILE_PATH)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://github.com/')