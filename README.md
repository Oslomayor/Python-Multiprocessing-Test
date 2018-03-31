# Python-Multiprocessing-Test
Python 官方多进程库 **multiprocessing** 测试 

## 使用方法

```python
from multiprocessing import Pool
# 开启2个进程
pool = Pool(processes=2)
pool.map(func=outputPrime, iterable=range(8888888))
```

## 运行效果

### 双进程运行

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/Python-multiprocessing1.PNG?raw=true)

### 四进程运行

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/Python-multiprocessing2.PNG?raw=true)

### 不同进程对比

![](https://github.com/Oslomayor/Markdown-Imglib/blob/master/Imgs/Python-multiprocessing3.PNG?raw=true)

可见 **不是进程越多速度越快**

