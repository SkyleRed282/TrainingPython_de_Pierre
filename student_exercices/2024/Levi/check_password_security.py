from string import punctuation
# {} () []

# create an empty list of insecure reasons


password_unsafe = True
while password_unsafe:

    unsafe = []

    # ask the user for a password
    password = input('Passwort: ')

    # We will check the security of the password in many steps
    # 1) check if the length of it is at least 10
    if len(password) < 10:
        unsafe.append('Passwort zu kurz min 10 ')

    # 2) check if it contains at least a number. Hint: isdigit()
    for symbol in password:
        if symbol.isdigit():
            break
    else:
        unsafe.append('Passwort braucht min. 1 Nummer')

    # 3) check if it contains at least a letter. Hint: isalpha()
    for symbol in password:
        if symbol.isalpha():
            break
    else:
        unsafe.append('Passwort braucht min. 1 Punkt')

    # 4) check if contains a special character like "$@#.-"
    for symbol in password:
        if symbol in punctuation:
            break
    else:
        unsafe.append('Passwort braucht min. 1 special character')

    # if every condition is correct, print "Your password <password> is secured
    if not unsafe:
        print(f'Your password "{password}" is secure')
        password_unsafe = False
    # else print "You password <password> is insecure, <reasons>
    else:
        print(f'Your password "{password}" is insecure : {unsafe}')