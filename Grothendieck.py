import numpy as np
import itertools

# m*n行列Aの設定
# 行数m
m = 10
# 列数n
n = 10

#行列にランダムな実数を代入
A = np.random.normal(0,np.sqrt(30),(m,n)) #正規分布(平均,標準偏差,(m,n))

def generate_XY(rep):
    T =itertools.product([1,-1],repeat=rep) #要素が1か-1であるようなすべての順列を列挙
    
    return T
#仮定のX,Yを全ての場合で生成する
X = generate_XY(m)
Y = generate_XY(n)

l_X =[]
l_Y =[]
for x in X:
    l_X.append(x)
l_X=np.array(l_X)

l_Y=[]
for y in Y:
    l_Y.append(y)
l_Y = np.array(l_Y)

sum = 0
sum_list=[]
#各X,Yに対して和を計算し、リスト化する。
for k in range(0,m):
    for l in range(0,n):
        
        for i in range(0,m):
            for j in range(0,n):
                sum += A[i][j] * l_X[k][i]*l_Y[l][j]
    
        sum_list.append(abs(sum))
        sum = 0

M = max(sum_list)
#Aを正規化して仮定の不等式を満たすようにする
A_normarize = A/M 

#証明の正誤判定の初期化
result = True

#試行回数Nの設定
N=100

for t in range(0,N):
    #W,Zベクトルの生成(任意なので分布は何でもよい)
    W = np.random.normal(-20,100,m)
    Z = np.random.normal(100,1000,n)

    #WとZの絶対値に関する最大値を取得
    W_max = max(np.abs(W))
    Z_max = max(np.abs(Z))
    #上の積を取得
    right_hand_bound = W_max*Z_max

    for i in range(0,m):
        for j in range(0,n):
            sum += A_normarize[i][j]*W[i]*Z[j]
#Falseの場合は左辺と右辺を出力する
    if np.abs(sum) > right_hand_bound:
        result = False
        print("Wは" , W)
        print("Zは" , Z)
        print("Aは" , A_normarize)
        print("左辺は" , np.abs(sum) ," ", "右辺は" , right_hand_bound)

print(result)