# Sirage El-Jawhari
# ID: 018359144

def main():

    import math

    def rng():

        ran_num = []

        N = 10000
        A = 4857
        M = 8601

        S = 0

        for i in range(100):
            S = (M*S+A)%N
            r = S/N
            ran_num.append(r)
            print(format(r,'.4f'))
        return ran_num
    
    def Coin(c):
        for j in c[0:25]: # 0:24 returned 24 possibilities so I added one more to make it 25 flips 
            coin = math.floor(2*j)
            if coin == 0:
                print('Tail')
            else:
                print('Head')
    def Die(d):
        for k in d[0:25]: # 0:24 returned 24 possibilities so I added one more to make it 25 dice rolls 
            die = math.ceil(6*k)
            print(die)
    
    rn = rng()
    Coin(rn)
    Die(rn)

main()