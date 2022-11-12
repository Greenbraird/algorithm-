dwarf = [int(input()) for _ in range(9)] #9개의 숫자를 list로 받는다.
dwarf_sum = sum(dwarf) #dwarf list를 다  더한다.

dwarf.sort() #올름차순으로 정렬해준다.

def ran(dwarf, dwarf_sum): #함수로 정의해 준다. 그 이유는 이중 for문에서 정답을 찾았을때 return으로 함수를 종료를 위해
  for i in range(8): 
    a = dwarf[i] #첫번째 수를 a로 정의
    for j in range(i+1, 9):
      b = dwarf[j] #두번째 수를 b로 정의
      if dwarf_sum - a - b == 100: # a와 b를 dwarf_sum에서 빼서 100이되면 dwarf list에서 a값과 b값을 뺀 list가 정답
        dwarf.remove(a) #dwarf list에서 a를 빼준다.
        dwarf.remove(b) #dwarf list에서 b를 빼준다.
        return '\n'.join(map(str,dwarf)) #dwarf list를 한줄씩 띄어서 return

print(ran(dwarf, dwarf_sum))

"""
---------------------------------------
첫번째 실패는 다음과 같다.
이중 for문의 break 거는 방법을 알지 못했다.
그래서 def을 통해 함수로 정의 해서 풀었다.
---------------------------------------
함수로 하지 않고 이중 for문으로 하기 위해서는 다음과 같다.
수 없는 연구 끝에 터득
★Break_first_for = True
for i in range(len(dwarf)-1):
  for j in range(i+1, len(dwarf)):
    dwarf_miner = dwarf_sum
    dwarf_miner -= (dwarf[i] + dwarf[j])
    if dwarf_miner == 100:
      dwarf.pop(i)
      dwarf.pop(j-1)
    ★Break_first_for = False
      print('\n'.join(map(str,dwarf)))  
      break
★if Break_first_for == False:
    break


4가지 생각의 전개
1. 문제 이해하기
:9개의 숫자를 입력받고 7의 합이 100되는 숫자들을 오름차순으로 출력하는구나

2. 재정의와 추상화
: 완전 탐색으로 해결하면 되겠네

3. 계획 세우기
dwarf라는 list를 정의해서
for문을 통해 9개의 수를 dwarf에 append 시킨다.

dwarf.sum()해서 9개의 수를 더하고
dwarf.sort()한다.-----------
이중 for를 통해 dwarf_sum에서 2수를 뺀다.
그러면 7개의 수가 더한게 된다.
dwarf_sum의 수가 100이 될 때까지 빼준다.
100 되면 i와 j를 pop시킨다.


4. 검증하기
여기는 아직 
여기서는 시간복잡도와 공간복잡도를 생각한다.
"""
