import random

name = ['권성주', '김동민', '김소희','김승현', '김예원', '김채운', ' 문지현','박나영', '서수범', '서희선', '유아람', '우희윤', '이예원', '이유림', '이정민', ' 이지행', '정수연', '조하늘', '채효정', '한아리영', '김시준']
while True:

    a = int(input("0:진행 | 1:멈춤\n"))
    if  a == 0:
            print(name.pop(random.randrange(0,len(name))))
    else:
        break


 