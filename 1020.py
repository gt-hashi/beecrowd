def days_converter(N):
    year = N // 365
    N %= 365
    month = N // 30
    days = N % 30

    print(f'{year} ano(s)')
    print(f"{month} mes(es)")
    print(f'{days} dia(s)')

days = int(input())

days_converter(days)

