import requests

if __name__ == '__main__':

    try:
        resp = requests.get('http://www.google.frss')
        print(resp.status_code)
        # raise Exception('Exception !!!')
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError: {e}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        print('Aucune erreur')
    finally:
        print('Toujours lancé')

