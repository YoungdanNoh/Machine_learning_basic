import numpy as np
import matplotlib.pyplot as plt

def prediction(theta_0, theta_1, x):
    """주어진 학습 데이터 벡터 x에 대해서 모든 예측 값을 벡터로 리턴하는 함수"""
    # 지난 과제 코드를 갖고 오세요
    return theta_0 + theta_1*x
    
    
def prediction_difference(theta_0, theta_1, x, y):
    """모든 예측 값들과 목표 변수들의 오차를 벡터로 리턴해주는 함수"""
    # 지난 과제 코드를 갖고 오세요
    return prediction(theta_0, theta_1, x) - y
    
def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    """주어진 theta_0, theta_1 변수들을 경사 하강를 하면서 업데이트 해주는 함수"""
    m = len(x) # 총 데이터 개수
    cost_list = [] # 경사하강을 한 번 할 때마다 그 시점의 손실을 저장하는 함수
    for i in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 실제 값들의 오차를 계산
        cost = (error@error) / (2*m) # 모든 오차를 재곱하고 더한 후 2m으로 나눈다.
        cost_list.append(cost)
        
        theta_0 = theta_0 - alpha*error.mean()
        theta_1 = theta_1 - alpha*(error*x).mean()
        
        # 실제 가설함수가 개선되는 것을 시각적으로 그려보기
        if i % 10 == 0: # 그래프를 200번 그리지 않고 10번에 한번씩만 그리기
            plt.scatter(house_size, house_price)
            plt.scatter(house_size, prediction(theta_0, theta_1, x), color='red')
            plt.show()
        
    return theta_0, theta_1, cost_list
    
    
# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1, cost_list = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

print(theta_0, theta_1)

# 손실 리스트를 그래프에 그려보기
plt.plot(cost_list)
plt.show() # 경사하강을 반복할수록 손실이 줄어드는 것을 볼 수 있다.
