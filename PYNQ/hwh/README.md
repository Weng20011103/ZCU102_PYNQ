# Overlay HWH 檔案  
`HWH`（hardware handoff）檔案是由 Vivado IP Integrator block design 自動生成的，並由 PYNQ 用來自動識別 Zynq 系統配置、IP（包括版本）、中斷（interrupts）、重設（resets）和其他控制信號。  
  
基於這些資訊，系統配置（system configuration）的某些部分可以由 PYNQ 自動修改，驅動程式可以自動分配，功能可以啟用或禁用，並且信號可以連接到相應的 Python methods。  
  
進行 Generating Bitstream 時，`HWH`檔案會由 Vivado 自動生成。  
  
`HWH`檔案必須作為`Overlay`的一部分與`.bit`檔案一起提供。PYNQ PL class 將自動解析（parse）`HWH`檔案。  
  
`HWH`檔案在以下目錄中:  
```text
<prj>.gen/sources_1/bd/<bd_name>/hw_handoff/<bd_name>.hwh
```
  
`HWH`檔案名稱應該與`.bit`檔案名稱相符。  
  
當`Overlay`實例化（instantiated）並下載時，將解析`HWH`檔案。  
```python
from pynq import Overlay
ol = Overlay("base.bit") # hwh is parsed here
```
  
如果在嘗試下載`overlay`時`HWH`不可用，或者`HWH`檔案名稱與`.bit`檔案名稱不符，則會顯示錯誤。  
  
## 參考連結  
[Overlay HWH file](https://pynq.readthedocs.io/en/latest/overlay_design_methodology/overlay_design.html#overlay-hwh-file)  
