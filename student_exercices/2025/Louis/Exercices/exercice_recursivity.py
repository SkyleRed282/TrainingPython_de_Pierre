from string import ascii_lowercase as alphabet

alphabet_court = alphabet[:5]
#
# while len(alphabet_court) != 0:
#     alphabet_court = alphabet_court[:-1]
#     print(alphabet_court)



def coupe_string(some_text:str):

    if not some_text:
        return

    print(some_text)
    coupe_string(some_text[:-1])

coupe_string(alphabet_court)