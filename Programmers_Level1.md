## 없는 숫자 더하기
### 문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 수 ≤ 9
numbers의 모든 수는 서로 다릅니다.

### 입출력 예
numbers	result
[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	6

### 입출력 예 설명
입출력 예 #1

5, 9가 numbers에 없으므로, 5 + 9 = 14를 return 해야 합니다.
입출력 예 #2

1, 2, 3이 numbers에 없으므로, 1 + 2 + 3 = 6을 return 해야 합니다.

```python
# 나의 풀이
def solution(numbers):
    # numbers를 집합으로 바꾼다
    numbers = set(numbers)
    # 0~9까지 들어있는 집합 ex 선언
    ex = set(range(10))
    # ex 와 numbers에 차집합을 결과값에 넣기
    result = ex - numbers
    # 차집합의 원소 합을 정답에 넣기
    answer = sum(result)
    return answer
```


## 로또의 최고 순위와 최저 순위
### 문제 설명
로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 

### 순위 당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외

로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.

알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.

당첨 번호	31	10	45	1	6	19	결과
최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등

순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

### 제한사항
lottos는 길이 6인 정수 배열입니다.
lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
0은 알아볼 수 없는 숫자를 의미합니다.
0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
win_nums은 길이 6인 정수 배열입니다.
win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
입출력 예
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]

---
### 입출력 예 설명
입출력 예 #1
문제 예시와 같습니다.

입출력 예 #2
알아볼 수 없는 번호들이 아래와 같았다면, 1등과 6등에 당첨될 수 있습니다.

당첨 번호	38	19	20	40	15	25	결과
최고 순위 번호	0→38	0→19	0→20	0→40	0→15	0→25	6개 번호 일치, 1등
최저 순위 번호	0→21	0→22	0→23	0→24	0→26	0→27	0개 번호 일치, 6등
입출력 예 #3
민우가 구매한 로또의 번호와 당첨 번호가 모두 일치하므로, 최고 순위와 최저 순위는 모두 1등입니다.

실제로 사용되는 로또 순위의 결정 방식과는 약간 다르지만, 이 문제에서는 지문에 명시된 대로 로또 순위를 결정하도록 합니다.  ↩


```python
# 일치한 번호 개수를 키로 가지고 값을 순위로 가지는 사전형 자료 선언
win = { 0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}

def solution(lottos, win_nums):
    # 가장 많이 맞은 경우의 수와 가장 적게 맞은 경우에 수 담을 변수 선언
    r1 = 0
    r2 = 0
    # 로또 산 번호 원소들을 순차적으로 방문
    for i in lottos:
        # win_num안에 있는지 조회
        if i in win_nums:
            # 있으면 1씩 증가시키기
            r1 += 1
            r2 += 1
            # 만약 i 가 0이라면 r2(가장 많이 맞은 경우의 수)에 1씩 더해주기
        elif i == 0:
            r2 += 1
    
    # win에서 value 결과 출력
    result = [win[r2], win[r1]]
    return result
```

## 최소직사각형
문제 설명
명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.

명함 번호	가로 길이	세로 길이
1	60	50
2	30	70
3	60	30
4	80	40
가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 이때의 지갑 크기는 4000(=80 x 50)입니다.

모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

제한사항
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.
입출력 예
sizes	result
[[60, 50], [30, 70], [60, 30], [80, 40]]	4000
[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133
입출력 예 설명
입출력 예 #1
문제 예시와 같습니다.

입출력 예 #2
명함들을 적절히 회전시켜 겹쳤을 때, 3번째 명함(가로: 8, 세로: 15)이 다른 모든 명함보다 크기가 큽니다. 따라서 지갑의 크기는 3번째 명함의 크기와 같으며, 120(=8 x 15)을 return 합니다.

입출력 예 #3
명함들을 적절히 회전시켜 겹쳤을 때, 모든 명함을 포함하는 가장 작은 지갑의 크기는 133(=19 x 7)입니다.

```python
# 나의 풀이
def solution(sizes):
    # 빈 배열 선언
    answer = []
    # 넓이, 높이 변수 선언
    w = 0
    h = 0
    # sizes 순회
    for size in sizes:
        # 만약 size의 0번째 인덱스가 size의 1번째 인덱스보다 크다면 서로 바꿔주기
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
        # 배열에 넣어준다
        answer.append(size)
    # answer 순회    
    for i in answer:
        # 0번째 인덱스의 최댓값 찾기
        if i[0] > w:
            w = i[0]
        # 1번째 인덱스의 최댓값 찾기
        if i[1] > h:
            h = i[1]
            
    # 넓이 높이 최댓값을 리턴하기
    return h * w
```


## 나머지가 1이 되는 수 찾기
문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000
입출력 예
n	result
10	3
12	11
입출력 예 설명
입출력 예 #1

10을 3으로 나눈 나머지가 1이고, 3보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 3을 return 해야 합니다.
입출력 예 #2

12를 11로 나눈 나머지가 1이고, 11보다 작은 자연수 중에서 문제의 조건을 만족하는 수가 없으므로, 11을 return 해야 합니다.

```python
# 나의 풀이
def solution(n):
    # 빈 배열 선언
    answer = []
    # i 는 1 ~ n까지 순회
    for i in range(1, n + 1):
        # 만약 나머지가 1이 되는 i 는 배열에 넣어주기
        if n % i == 1:
            answer.append(i)
    # 배열에서 가장 작은 값을 리턴
    return min(answer)
```

## 부족한 금액 계산하기
문제 설명
새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

제한사항
놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
입출력 예
price	money	count	result
3	20	4	10
입출력 예 설명
입출력 예 #1
이용금액이 3인 놀이기구를 4번 타고 싶은 고객이 현재 가진 금액이 20이라면, 총 필요한 놀이기구의 이용 금액은 30 (= 3+6+9+12) 이 되어 10만큼 부족하므로 10을 return 합니다.

참고 사항
미션 언어는 Java, JavaScript, Python3, C++ 만 해당 됩니다.
같은 코드를 제출한 사람이 여럿이라면 코드를 가장 먼저 제출한 분께 상품을 드립니다.
좋아요 수가 동일할 경우 코드를 가장 먼저 제출한 분께 상품을 드립니다.
solution.py
1
def solution(price, money, count):
2
    pay = 0
3
    for i in range(1, count + 1):
4
        pay += price * i
5
        
6
    result = money - pay
7
    if result > 0:
8
        return 0
9
    else:
10
        return abs(result)
실행 결과
실행 결과가 여기에 표시됩니다.

```python
# 나의 풀이
def solution(price, money, count):
    # pay 변수 선언
    pay = 0
    # 1부터 count까지 반복하면서 지불할 금액 더해주기
    for i in range(1, count + 1):
        pay += price * i
    # 결과는 가진 돈과 지불할 돈을 뺀 값    
    result = money - pay
    # 만약 결과가 0보다 크다면 0을 리턴해준다
    if result > 0:
        return 0
    # 그렇지 않다면 절댓값을 리턴해준다
    else:
        return abs(result)
```

## 나누어 떨어지는 숫자 배열
문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
입출력 예
arr	divisor	return
[5, 9, 7, 10]	5	[5, 10]
[2, 36, 1, 3]	1	[1, 2, 3, 36]
[3,2,6]	10	[-1]
입출력 예 설명
입출력 예#1
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

```python
# 나의 풀이
def solution(arr, divisor):
    # 빈배열 선언해주기
    answer = []
    # 나누어 떨어지는 갯수 세는 count 변수 선언
    count = 0
    # arr 순회
    for i in arr:
        # 만약 divisor 로 나누어 떨어진다면
        if i % divisor == 0:
            # answer에 넣고 count + 1
            answer.append(i)
            count += 1
            
    # 배열 정렬
    answer.sort()
    # 만약 나누어떨어지는 수가 없다면 return [-1]
    if count == 0:
        return [-1]
    return answer
```

## 두 정수 사이의 합
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
입출력 예
a	b	return
3	5	12
3	3	3
5	3	12

```python
# 나의 풀이
def solution(a, b):
    # 만약 a < b 라면 answer = a, b 사이의 수의 합
    if a < b:
        answer = sum(range(a, b + 1))
    # 그렇지 않다면 answer = b, a 사이의 수의 합
    else:
        answer = sum(range(b, a + 1))
    return answer
```

## 문자열 내 p와 y의 개수
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.
입출력 예
s	answer
"pPoooyY"	true
"Pyy"	false
입출력 예 설명
입출력 예 #1
'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

입출력 예 #2
'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.


```python
# 나의 풀이
def solution(a, b):
    # 만약 a < b 라면 answer = a, b 사이의 수의 합
    if a < b:
        answer = sum(range(a, b + 1))
    # 그렇지 않다면 answer = b, a 사이의 수의 합
    else:
        answer = sum(range(b, a + 1))
    return answer
```

## 문자열을 정수로 바꾸기
문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.
입출력 예
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

```python
def solution(s):
    return int(s)
```

## 약수의 합
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
입출력 예
n	return
12	28
5	6
입출력 예 설명
입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

```python
# 나의 풀이
def solution(n):
    # 약수의 합을 담을 정수 변수 선언
    answer = 0
    # i는 1부터 n까지 순회
    for i in range(1, n + 1):
        # 만약 i 가 n 의 약수라면 answer에 더하기
        if n % i == 0:
            answer += i
    # answer 리턴하기
    return answer
```

## 자릿수 더하기
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수
입출력 예
N	answer
123	6
987	24
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.

```python
# 나의 풀이
def solution(n):
    # 정수형 answer 선언 
    answer = 0
    # 문자열 n을 순차적으로 순회
    for i in str(n):
        # answer에 정수 i를 더해주기
        answer += int(i)

    return answer
```

## 자연수 뒤집어 배열로 만들기
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]

```python
# 나의 풀이
def solution(n):
    # 빈 배열 선언
    answer = []
    # 문자열로 바꿔준 숫자를 뒤집어서 순회하기
    for i in reversed(str(n)):
        # answer에 int로 바꿔서 넣어주기
        answer.append(int(i))
        
    return answer
```

## 정수 내림차순으로 배치가
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211

```python
# 나의 풀이
def solution(n):
    # 빈 배열 선언
    list = []
    # 빈 문자열 선언
    answer = ''
    # 문자열 순회
    for i in str(n):
        # 리스트에 추가해주기
        list.append(i)
    # 리스트 큰 순서대로 정렬
    list.sort(reverse=True)
    # 리스트를 순회해서 문자열로 바꿔서 차례대로 answer에 넣어주기
    for i in list:
        answer += str(i)
    # int형으로 바꿔서 리턴하기    
    return int(answer)
```

## 정수 제곱근 판별
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.
입출력 예
n	return
121	144
3	-1
입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.

```python
# 나의 풀이
def solution(n):
    # 만약 n 의 제곱근이 정수인 n 제곱근과 같으면
    if n ** (1/2) == int(n ** (1/2)):
        # 제곱근 + 1의 제곱을 리턴하기
        return ((n ** (1/2)) + 1) * ((n ** (1/2)) + 1)
    # 그렇지 않다면 -1 리턴하기
    else:
        return -1
```