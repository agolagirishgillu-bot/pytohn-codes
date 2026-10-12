from abc import ABC ,abstractmethod

class device(ABC):
    def show_detail(self,name):
        print('device(s) name is',name)

    @abstractmethod
    def dev(self):
        pass

class fan(device):
    def dev(self):
        print('the fan is ON.')

class light(device):
    def dev(self):
        print('the is light is ON.')

class speaker(device):
    def dev(self):
        print('the speaker is ON.')

f=fan()
l=light()
s=speaker()

f.dev()
f.show_detail('fan')

l.dev()
l.show_detail('light')

s.dev()
s.show_detail('speaker')
class door():
    def func(self):
        print('door can open/close.')

class lock():
    def func(self):
        print('lock can lock door')

obj1=door()
obj2=lock()

for i in (obj1,obj2):
    i.func()