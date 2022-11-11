
import requests

if __name__ == '__main__':

    resp = requests.post('https://apply.caplena.com/api-guru')
    print(resp.__dict__)
    # To unlock the secret job-application key, decode this message and POST it to this endpoint:
    # VGhlIEludGVybmV0PyAgV2UgYXJlIG5vdCBpbnRlcmVzdGVkIGluIGl0Lg==

    # https://dencode.com/
    test = 'The Internet?  We are not interested in it.'
    resp2 = requests.post('https://apply.caplena.com/api-guru', data=test)
    # That's correct! The secret response key has been transmitted to you.

    print(resp2.__dict__)
    # super-secret-key-for-job-application': 'dum-di-dumm'