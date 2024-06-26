# 第三課: 由 PYNQ 載入 bit 檔點亮 GPIO LED    
示範如何使用`PYNQ`來載入`.bit`檔後操控`GPIO LED`的方法。  
  
## 確認連接埠  
在`Windows 11`的圖標上右鍵選擇`裝置管理員`。  
![1.png](pictures/1.png "1.png")  
  
找到連接埠選項展開尋找`Silicon Labs Quad CP2108 USB to UART Bridge: Interface 0`，以下圖為例為`COM8`。  
![2.png](pictures/2.png "2.png")  
  
## Putty 設定  
開啟`Putty`應用程式。  
![3.png](pictures/3.png "3.png")  
  
選擇`Serial`選項，`Serial line`填`COM8`且`Speed`填`115200`後按`Open`。  
![4.png](pictures/4.png "4.png")  
  
此時`Putty`界面如下。  
![5.png](pictures/5.png "5.png")  
  
此時`ZCU102`開發版電源未開啟如下圖。  
![b1.png](pictures/b1.png "b1.png")  
  
把`ZCU102`開發版電源往上方開啟如下圖。  
![b2.png](pictures/b2.png "b2.png")  
  
此時`Putty`頁面會開始打印訊息。 **註: 我把`Hash value`去掉了**  
![6.png](pictures/6.png "6.png")  
  
等待一段時間後`Putty`頁面會顯示
```text
xilinx@pynq:~$
```
此時板子即啟動完成。  
![7.png](pictures/7.png "7.png")  
  
## 檔案總管訪問 PYNQ  
在同一個局域網中可以訪問`ZCU102`的資料夾，進入`jupyter_notebooks`資料夾。  
![8.png](pictures/8.png "8.png")  
  
創建`led_kirakira`資料夾。  
![9.png](pictures/9.png "9.png")  
  
把`lesson 1`和`lesson 2`的`.bit`檔和`.hwh`檔放入`led_kirakira`資料夾。  
![10.png](pictures/10.png "10.png")  
  
## 瀏覽器訪問 Jupyter Notebook  
在瀏覽器搜尋窗口輸入`pynq:9090`後按`Enter`鍵。  
![11.png](pictures/11.png "11.png")  
  
第一次登入或無痕模式會需要輸入密碼，密碼為`xilinx`。  
![12.png](pictures/12.png "12.png")  
  
登入後選擇剛剛創建的`led_kirakira`資料夾。  
![13.png](pictures/13.png "13.png")  
  
## 創建 ipynb 檔案  
在`led_kirakira`資料夾點擊`New`選`Python 3`。  
![14.png](pictures/14.png "14.png")  
  
此時頁面如下。  
![15.png](pictures/15.png "15.png")  
  
輸入下方程式碼後利用`alt + enter`組合鍵執行程式。 **`ctrl + enter`組合鍵也能執行但不會加入下面一列的程式格**  
```python
from pynq import Overlay
```
![16.png](pictures/16.png "16.png")  
  
在程式格中加入驚嘆號`!`可以執行`Linux`的指令如`ls`，範例: `!ls`。  
![17.png](pictures/17.png "17.png")  
  
輸入下方程式碼載入`lesson 1`的`LED_kirakira1.bit`檔案。  
```python
overlay = Overlay('LED_kirakira1.bit')
```
![18.png](pictures/18.png "18.png")  
  
執行`overlay?`可以看到`LED_kirakira1.bit`中的一些`IP`核，不需要時可以按`x`關閉小視窗。  
![19.png](pictures/19.png "19.png")  
  
輸入下方程式碼來操作`axi_gpio_0`。  
```python
led = overlay.axi_gpio_0
```
![20.png](pictures/20.png "20.png")  
  
輸入下方程式碼來讀取`axi_gpio_0`的值，結果為`0`。  
```python
led.read(0)
```
![21.png](pictures/21.png "21.png")  
  
輸入下方程式碼來寫入`axi_gpio_0`的值，結果為十進制的`121`即二進制的`01111001`。  
```python
led.write(0, 121)
```
![22.png](pictures/22.png "22.png")  
  
此時板子的`PL LEDs`如下圖，跟寫入的二進制`01111001`一致。  
![b3.png](pictures/b3.png "b3.png")  
  
也可以利用下方程式碼來直接寫入二進制的`10100011`。  
```python
led.write(0, 0b10100011)
```
![23.png](pictures/23.png "23.png")  
  
此時板子的`PL LEDs`如下圖，跟寫入的二進制`10100011`一致。  
![b4.png](pictures/b4.png "b4.png")  
  
## Shutdown Kernel from ipynb  
不使用此`ipynb`檔案後點擊`Kernel`選`Shutdown`。  
![24.png](pictures/24.png "24.png")  
  
`Shutdown kernel?`提示訊息中選`Shutdown`確認操作。  
![25.png](pictures/25.png "25.png")  
  
此時右上方會顯示`No kernel`。  
![26.png](pictures/26.png "26.png")  
  
點左上角`Jupyter`圖標切換至主頁面後選`Running`可以看到沒有`Notebook`執行中。  
![27.png](pictures/27.png "27.png")  
  
## Shutdown Kernel from ipynb  
載入`lesson 2`的`LED_kirakira2.bit`。  
![28.png](pictures/28.png "28.png")  
  
寫入二進制`11110000`後`LED`執行結果如下圖正確。  
![b5.png](pictures/b5.png "b5.png")  
  
點左上角`Jupyter`圖標切換至主頁面後選`Running`可以看到有`Notebook`執行中，點擊`Shutdown`來關閉。  
![29.png](pictures/29.png "29.png")  
  
稍等一陣子後關閉完成。  
![30.png](pictures/30.png "30.png")  
  
回到被結束的`ipynb`檔頁面會看到提示訊息，點`Don't Restart`。  
![31.png](pictures/31.png "31.png")  
  
此時右上方會顯示`No kernel`。  
![32.png](pictures/32.png "32.png")  
  
## 下一堂課連結:  
[第四課: 由 PYNQ 寫入 GPIO 控制 DAC 輸出電壓](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson4_dac_control_by_pynq#%E7%AC%AC%E5%9B%9B%E8%AA%B2-%E7%94%B1-pynq-%E5%AF%AB%E5%85%A5-gpio-%E6%8E%A7%E5%88%B6-dac-%E8%BC%B8%E5%87%BA%E9%9B%BB%E5%A3%93)  

## 參考連結  
[Notebooks are not just for Python](https://pynq.readthedocs.io/en/latest/getting_started/jupyter_notebooks_advanced_features.html#Notebooks-are-not-just-for-Python)  
[AxiGPIO](https://pynq.readthedocs.io/en/latest/pynq_libraries/axigpio.html#axigpio)  