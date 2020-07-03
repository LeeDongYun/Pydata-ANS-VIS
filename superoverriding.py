class Singer:
    def __init__(self, name, debut):
        self.name = name
        self.debut = debut

    def introduce(self):
        print('안녕하세요! 가수 %s입니다' % self.name)

    def age(self):
        print('데뷔한지 %d년이 됬어요' % (2020 - self.debut +1))

class KPopGroup(Singer):
    def __init__(self, name, debut, cnt):
        super().__init__(name, debut)
            

        self.cnt = cnt

    def introduce(self):
        super().introduce()
        print('우린 KPop 그룹으로 %d명입니다' % self.cnt)

bts = KPopGroup('BTS',2013,7)
bts.introduce()
bts.age()