# 第一課: 由 GPIO 設定點亮 GPIO LED  
示範如何使用`GPIO`來操控`GPIO LED`的方法。  
  
## Vivado 工程創建  
開啟`Vivado 2020.2`應用程式。  
![1.png](pictures/1.png "1.png")  
  
點擊`Create Project`創建新的工程。  
![2.png](pictures/2.png "2.png")  
  
點擊`Next`。  
![3.png](pictures/3.png "3.png")  
  
自訂`Project name`和`Project location`後選`Next`。  
![4.png](pictures/4.png "4.png")  
  
選擇`RTL Project`並勾選`Do not specify sources at this time`後選`Next`。  
![5.png](pictures/5.png "5.png")  
  
選擇`Boards`選項後選擇`Zynq UltraScale+ ZCU102 Evaluation Board`後選`Next`。  
![6.png](pictures/6.png "6.png")  
  
點擊`Finish`。  
![7.png](pictures/7.png "7.png")  
  
## Block Design 設計  
點擊`IP INTEGRATOR`中的`Create Block Design`。  
![8.png](pictures/8.png "8.png")  
  
自訂`Design name`後選`OK`。  
![9.png](pictures/9.png "9.png")  
  
在`Diagram`中`右鍵`後選擇`Add IP...`。  
![10.png](pictures/10.png "10.png")  
  
左鍵雙擊選擇`Zynq UltraScale+ MPSoC`。  
![11.png](pictures/11.png "11.png")  
  
再次右鍵選擇`Add IP...`左鍵雙擊新增`AXI GPIO`。  
![12.png](pictures/12.png "12.png")  
  
此時`Diagram`圖如下。  
![13.png](pictures/13.png "13.png")  
  
左鍵雙擊`axi_gpio_0`後在`Re-customize IP`把`GPIO`設置成`led 8bits`後選`OK`。    
![14.png](pictures/14.png "14.png")  
  
點擊`Run Connection Automation`。  
![15.png](pictures/15.png "15.png")  
  
勾選`All Automation`左側的格子後按`OK`。  
![16.png](pictures/16.png "16.png")  
  
此時`Diagram`內容如下。  
![17.png](pictures/17.png "17.png")  
  
展開`Sources`中的`Design Sources`右鍵`LED_kirakira.bd`後選`Create HDL Wrapper...`。 ***`.bd`檔名是自己取的***  
![18.png](pictures/18.png "18.png")  
  
選擇`Let Vivado manage wrapper and auto-update`後按`OK`。  
![19.png](pictures/19.png "19.png")  
  
等待`LED_kirakira.bd`變成`LED_kirakira_wrapper.v`檔後點擊`Generate Bitstream`。  
![20.png](pictures/20.png "20.png")  
  
`Generate Bitstream`的時間跟工程量有關，`.bit`檔完成後會出現`Bitstream Generation Completed`訊息，按`OK`繼續。  
![21.png](pictures/21.png "21.png")  
  
在`Design Timing Summary`會顯示出設計的時間參數，沒問題就可關閉`Vivado`軟件。  
![22.png](pictures/22.png "22.png")  
  
## .bit 檔和 .hwh 檔  
開啟你的`Vivado`工程檔案資料夾，`.bit`檔位於`.runs`資料夾中，`.hwh`檔位於`.gen`資料夾中。  
![23.png](pictures/23.png "23.png")  
  
`.bit`檔的位置`F:\EE\20240416\LED_kirakira1\LED_kirakira1.runs\impl_1`中。  
![24.png](pictures/24.png "24.png")  
  
`.hwh`檔的位置`F:\EE\20240416\LED_kirakira1\LED_kirakira1.gen\sources_1\bd\LED_kirakira\hw_handoff`中。  
![25.png](pictures/25.png "25.png")  
  
把`.bit`檔和`.hwh`檔改成同一檔名以便後續使用。  
![26.png](pictures/26.png "26.png")  

## 下一堂課連結:  
[第二課: 由 XDC 綁定腳位點亮 GPIO LED](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson2_LED_kirakira_xdc#%E7%AC%AC%E4%BA%8C%E8%AA%B2-%E7%94%B1-xdc-%E7%B6%81%E5%AE%9A%E8%85%B3%E4%BD%8D%E9%BB%9E%E4%BA%AE-gpio-led)  