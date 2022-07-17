import sys
sys.stdin = open('호텔.txt')

# 허용량(이상 가능), 도시 갯수
Capacity, City = map(int, input().split())
# Cost는 비용, Customer는 Cost당 Customer
Costs_Customers = [list(map(int, input().split())) for _ in range(City)]
# 최솟값을 구하는 거니까 최대치로 생성(DP)
# index는 index명만큼을 부르는 데 필요한 최소한의 비용
Total = [float('inf')]*(Capacity+200)
# 돈 없으면 아무도 못 가져오니까 0으로 만듦
Total[0] = 0
# Cost순으로 정렬
Costs_Customers = sorted(Costs_Customers)

for Cost, Customer in Costs_Customers:
    # 가장 적은 Cost로 부를 수 있는 Customer부터 대략적으로 원하는 숫자 + 200명까지 세보기
    for index in range(Customer, Capacity+200):
        # Total[index]에 저장되는 숫자는 Total[index-Customer](즉, n명 모집 전까지 들어간 돈)보다 더 들어가는게 싼지, 아닌지 결정
        # 근데 그걸 모든 Cost를 계산해보는 것임.
        # ex) 1명을 2번 부르는게 싼지, 2명을 1번 부르는게 싼지를 for를 통해 계산하는 것
        Total[index] = min(Total[index-Customer] + Cost, Total[index])
# Capacity를 딱 정하는 게 아니라 그 이후에도 Cost가 싼 게 있을 수도 있으므로 :를 이용함.
print(min(Total[Capacity:]))
