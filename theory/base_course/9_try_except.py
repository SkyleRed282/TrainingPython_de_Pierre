import requests

if __name__ == '__main__':

    try:
       # resp = requests.get('http://www.google.fr')
        # print(resp.status_code)
        # raise Exception('Exception !!!')
        1 / 0
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError: {e}')
    except Exception as e:
        print(f'Other exception: {e}')
    else:
        print('Else: No error')
    finally:
        print('Finally: Always called')
