from decimal import Decimal
def banknotes_converter(N):
    list_of_bills = [Decimal("100.00"), Decimal("50.00"), Decimal("20.00"), Decimal("10.00"), Decimal("5.00"), Decimal("2.00")]

    print("NOTAS:")
    for i in range(len(list_of_bills)):
        number_of_bills = N // list_of_bills[i]
        N = N % list_of_bills[i] 
        print(f"{number_of_bills:.0f} nota(s) de R$ {list_of_bills[i]:.2f}")
    
    return N

def coin_banknotes(N):
    list_of_coins = [Decimal("1.00"), Decimal("0.50"), Decimal("0.25"), Decimal("0.10"), Decimal("0.05"), Decimal("0.01")]
    print("MOEDAS:")
    for i in range(len(list_of_coins)):
        number_of_coins = N // list_of_coins[i]
        N = N % list_of_coins[i] 
        print(f"{number_of_coins:.0f} moeda(s) de R$ {list_of_coins[i]:.2f}")
    



def main():
    user_val = Decimal(input())
    remainder=banknotes_converter(user_val)
    coin_banknotes(remainder)


if __name__ =="__main__":
    main()

""" 
Python の float は 2進数で表現されるため、10進数の小数を正確に扱えない ことがあります。
特に、0.01 のような数値は 2進数で正確に表現できない ため、計算途中で誤差が生じます。

例えば、次のような計算を考えてみてください：

python
Copy
Edit
print(0.1 + 0.2)  # 期待: 0.3 だが、実際は 0.30000000000000004
このように、float の計算では 微小な誤差が発生する ため、
N %= list_of_coins[i] の計算が期待通りに動かないことがあります。

弟子丸ファンクションを使うことも可能。より正確性の高い計算結果になります。。

"""