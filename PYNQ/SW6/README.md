# ZCU102 啟動選項  
參考[ZCU102 Evaluation Board User Guide (UG1182)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)的第 19 頁。  
  
## Switch SW6 (Figure 2-2, Callout 26)  
`Switch SW6`為圖一的紅圈部分，此時為`SD`配置。  
![圖一](pictures/1.png "1.png")  
  
有三種模式如下:  
***註: 朝 ON 是 0，反之為 1***  
|Boot Mode|Mode Pins [3:0]|Mode SW6 [4:1]|
|:--:|:--:|:--:|
|JTAG|0000|on, on, on, on|
|QSPI32|0010|on, on, off, on|
|SD|1110|off, off, off, on|
  
## PYNQ  
`PYNQ`啟動必須要使用`SD`模式。  
![圖二](pictures/2.png "2.png")  
  
## 參考連結  
[Zynq UltraScale+ MPSoC Technical Reference Manual (UG1085)](https://docs.amd.com/r/en-US/ug1085-zynq-ultrascale-trm/Zynq-UltraScale-Device-Technical-Reference-Manual)  
[ZCU102 Evaluation Board User Guide (UG1182)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)  