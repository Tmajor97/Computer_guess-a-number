def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'C':
        if low != high:
            guess = (low + high) // 2
        else:
            guess = low  # could also be high because low = high
        feedback = input(f'Is {guess} too (H), too low (L), or correct (C)? ')
        
        if feedback.lower() == 'h':
            high = guess - 1
        elif feedback.lower() == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(1000)
