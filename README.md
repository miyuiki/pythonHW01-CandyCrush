# 簡易版Candy Crush

### 程式截圖
![](https://github.com/miyuiki/pythonHW01-CandyCrush/blob/master/Capture/capture%2004102249.jpg?raw=true)

座標為一般的xy二維平面座標，起始1終止10
盤面為10*10

![](https://goo.gl/BaMV99)
![](https://goo.gl/o0LWGb)

在天降過程中可以找到連線並消去以及計算過程中累加的分數
```
while checkTable(table):
	searchConnected(table)
    score_count(table)
    drop(table, signal, num)
    print (table)
    print("分數:" + str(score))

```
使用wile迴圈檢查是否還可以再連線消除

![](https://goo.gl/X43GW8)
最終無法再連現實的盤面

### 其他功能

![](https://goo.gl/LZUnq8)
一些防呆措施