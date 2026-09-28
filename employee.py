class employee():
    def __init__(self):
        print('employee created')
    def __del__(self):
        print('employee destroyed')

def create_obj():
    obj=employee()
    print('making...')
    return obj

print('created create_obj()...')
obj=create_obj()
print('end.....')

