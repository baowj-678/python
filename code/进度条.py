import time
scale=100
print("begin".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
        a='*'*i
        b='.'*(scale-i)
        c=(i/scale)*100
        time.sleep(0.1)
        dur=time.perf_counter()-start
        print("\r\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
print("\n"+"over".center(scale//2,'-'))