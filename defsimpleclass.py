class person():
    pass

def hello(p):
    print('%s이 인사합니다' % p.name)

person.hello = hello

he = person()
he.name='홍길동'
he.age=20
print(he.name,he.age)
he.hello()
print(isinstance(he, person))


she = person()
she.name = '신입생'
she.age = 19
print(she.name, she.age)
she.hello()
print(isinstance(she, person))
