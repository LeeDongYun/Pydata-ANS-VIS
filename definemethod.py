class Singer:
    '''가수를 표현하는 클라스'''
    def __init__(self, name, debut):
        self.name = name
        self.debut = debut


    def introduce(self):
        print('안녕하세요! 가수 %s입니다.' % self.name)
    def age(self):
        print('데뷔한지 %d년이 됬네요.' % (2020 - self.debut +1))


iyou = Singer('아이유', 2008)
iyou.introduce()
iyou.age()