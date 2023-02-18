# The computer has to find a number between 1 and 100

min_number = 1
max_number = 100
feedback = ''

# Until the computer found the right number
while feedback != '=':
    # The computer guess a number
    guess = (max_number - min_number) // 2

    # If correct => Win
    # Else => receive a feedback on the direction (< oder >)
   