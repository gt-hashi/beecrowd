def get_hms(N):
    h = N // 3600
    N %= 3600
    m = N//60
    s = N%60
    
    print(f"{h}:{m}:{s}")
    

secs = int(input())
get_hms(secs)

