import random
import time
import platform
import psutil
from tqdm import tqdm

# 获取 CPU 基本信息
def get_cpu_info():
    return platform.processor(), platform.system(), platform.release()

# 输入计算的位数
decimal_places = int(input("请输入计算圆周率的位数："))

# 开始计算圆周率的时间
start_time = time.time()

# 找点的次数
total = 100000  
count = 0  # 只需要一个计数器

# 使用 tqdm 显示进度条
for i in tqdm(range(total), desc="计算中"):
    Xrandresult = random.uniform(0, 1)
    Yrandresult = random.uniform(0, 1)
    if (Xrandresult**2 + Yrandresult**2)**0.5 <= 1:
        count += 1

# 计算圆周率pi
average_pi = 4 * (count / total)

# 计算结束时间
end_time = time.time()
elapsed_time = end_time - start_time

# 不显示计算结果
# print(f"计算的圆周率 (保留{decimal_places}位数): {round(average_pi, decimal_places)}")

# 显示 CPU 信息
cpu_model, os_name, os_version = get_cpu_info()
cpu_usage = psutil.cpu_percent()

# 显示运算信息
print(f"运算时间: {elapsed_time:.4f} 秒")
print(f"运算速度: {total / elapsed_time:.2f} 点/秒")
