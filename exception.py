try:
    n=int(input('enter a no'))
    print('the no is',n)

except ValueError as ex:
    print(' error',ex)