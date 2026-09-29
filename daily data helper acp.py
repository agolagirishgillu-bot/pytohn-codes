class upper_case:
        def __init__(self):
               self.str1=''

        def get_ans(self):
              self.str1=input('enter todays messeage')

        def print_ans(self):
              print(self.str1.upper())

hi=upper_case()

hi.get_ans()
hi.print_ans()

class con_des:
       def __init__(self):
            print('messeage created...')
       def __del__(self):
            print('messeage destroyed....')

def create():
    obj=con_des()
    print('creating....')
    return obj

print('calling create() function..')
create_obj=create()
print('program iis still running..')


class pairfinder:
      def find_pair(self,num,target):
            lookup={}

            for index,number in enumerate(num):
                  needed_num=target-number

                  if needed_num in lookup:
                        return (lookup[needed_num],index)
                  lookup[num]=index

            return None

number1=(10,20,30,40,50,60,70)

target_value=int(input('enter the target:'))

result=pairfinder().find_pair(number1,target_value)

if result is not None:
      print('index1=%d,index2=%d'%result)
else:
      print('macth not found')

del create_obj