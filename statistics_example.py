# simple statistics program 

import statistics 


data = [2020, 2030,2040, 2050 , 2060, 2020]

mean = statistics.mean(data)

median = statistics.median(data)

mode = statistics.mode(data)


print("\033[96m SIMPLE STATISTICS PROGRAM.\033[00m".center(50))


print("\033[96m=\033[00m"*50)

print(f"\033[92m The Data:    {data}\033[00m")

print(f"The mean of the data is \033[92m{mean:.2f}\033[00m")

print (f"The median the data is \033[92m{median:.0f}\033[00m")
print (f"The mode of the the data is \033[92m{mode}\033[00m")


print("\033[96m=\033[00m"*50)		