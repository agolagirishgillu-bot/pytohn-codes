try:
    n1,n2=eval(input('enteer 2 no wiht comma between them'))
    r=n1/n2
    print('the result is',r)

except ZeroDivisionError as ex:
    print('the error',ex)

except SyntaxError as e:
    print('u forgot any syntax')

except:
    print('wrong input')

finally:
    print('print')