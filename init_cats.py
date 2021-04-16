class Cat:
    def __init__(self, name, color="흰색"):    #여기에 쓴 건 초기화 값. 이걸 지정해주면서 새로운 인스턴스를 만들어낸다
        self.name = name
        self.color = color

    def meow(self, name):
        print('내 이름은 {}, 색깔은 {}이야, 애옹~'.format(self.name, self.color))
        print('나이는', name,'살 이다냥!')    #여기서 쓰이는 name은 self.name과 다른 인자로 분류됨

nabi = Cat("나비")
nabi.meow(1)

nero = Cat("네로", "검은색")
nero.meow(4)

mimi = Cat("미미", "노란색")
mimi.meow(2)