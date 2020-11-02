선형회귀 경사 하강법 구현
==================

### 선형 회귀
- 데이터들이 있을 때 데이터들에 가장 잘 맞는 최적선을 찾아내는 것이 목표
- 최적선을 사용하면 새로운 입력 변수에 대한 목표 변수를 예측할 수 있다.

### 경사 하강법
- 손실 함수의 output을 최소화하기 위한 전략
- 손실 함수의 극소점을 찾는 것
- θ값을 늘리거나 줄이면서 극소점을 찾으면 된다.
- 경사의 방향과 크기를 이용해서 조금씩 극소점을 찾는 것이므로 경사 하강법이라 한다.

### 경사 하강법에서 <img width="18" alt="스크린샷 2020-11-02 오후 8 53 38" src="https://user-images.githubusercontent.com/38938145/97865409-7f475280-1d4d-11eb-96a9-081a9d523b38.png">와 <img width="18" alt="스크린샷 2020-11-02 오후 8 54 16" src="https://user-images.githubusercontent.com/38938145/97865465-97b76d00-1d4d-11eb-866e-b67c279ef154.png">을 업데이트 하는 방법
> <img width="223" alt="스크린샷 2020-11-02 오후 8 55 01" src="https://user-images.githubusercontent.com/38938145/97865538-b6b5ff00-1d4d-11eb-9b2d-b9010e4e590c.png">

> <img width="250" alt="스크린샷 2020-11-02 오후 8 55 10" src="https://user-images.githubusercontent.com/38938145/97865564-c3d2ee00-1d4d-11eb-920e-815c4ed03b68.png">

* * *
__본 실습은 경사 하강법을 사용해 <img width="18" alt="스크린샷 2020-11-02 오후 8 53 38" src="https://user-images.githubusercontent.com/38938145/97865409-7f475280-1d4d-11eb-96a9-081a9d523b38.png">와 <img width="18" alt="스크린샷 2020-11-02 오후 8 54 16" src="https://user-images.githubusercontent.com/38938145/97865465-97b76d00-1d4d-11eb-866e-b67c279ef154.png">의 값을 업데이트하는 코드이다.__
