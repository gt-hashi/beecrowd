def banknotes(N):
    print(N)
    banknotes = [100, 50, 20, 10, 5, 2, 1]
    labels = ["nota(s) de R$ 100,00",
              "nota(s) de R$ 50,00",
              "nota(s) de R$ 20,00",
              "nota(s) de R$ 10,00",
              "nota(s) de R$ 5,00",
              "nota(s) de R$ 2,00",
              "nota(s) de R$ 1,00"]
    
    for i in range(len(banknotes)):
        count = N // banknotes[i]
        print(f"{count} {labels[i]}")
        N %= banknotes[i]


N = int(input())
if 0 < N < 1000000:
    banknotes(N)