import requests

try:
    resp = requests.get('https://levicode2024.github.io/to-do/')
    resp.raise_for_status()

    # raise Exception('Exception !!!')

except ZeroDivisionError as e:
    print(f'ZeroDivisionError: {e}')
except Exception as e:
    print(f'Other exception: {e} of type {type(e).__name__}')
else:
    print('Else: No error')
finally:
    print('Finally: Always called')
