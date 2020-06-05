"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factorial(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """

def factorial(x):
    ret = 1
    for i in range(1,x+1):
        ret *= i #왼쪽 변수에 오른쪽 값을 곱하고 그 결과를 왼쪽 변수에 할당한다.
    return ret

print(factorial(5))
