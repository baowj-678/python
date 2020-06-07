二、1
{2, 10, 5}

二、2
(1). T(n) = T(n/2) + 1
(2). log(n)

二、3
nlog(n)

二、4
(1). 动态规划(DP)
(2). {a1、a2、a3、...、an}, 大小2^n
(3). 3, xi取值为{0，1}表示对各个值得选择与否

三、2
(1)、贪心算法，O(n)
(2)、
LeastStations(D)
distance <- 0
station <- 0
stations <- {}
for i = 1 -> k
    do if D[i] <= distance + n
        do station <- i
       else
        do stations.add(station)
           distance <- distance + D[station]
return stations
           
