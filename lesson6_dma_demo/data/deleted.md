## DMA (Direct Memory Access) 簡介  
`DMA`允許從記憶體（在此情況下為`PS DRAM`）串流資料到`AXI stream`介面，稱為`DMA`的`READ channel`。`DMA`也可以從`AXI stream`接收資料並將其寫回`PS DRAM`，稱為`DMA`的`WRITE channel`。  
  
`DMA`具有用於`READ channel`的`AXI Master port`，以及另一個用於`WRITE channel`的`AXI Master port`，也被稱為`memory-mapped ports` - 它們可以訪問`PS`記憶體。這些端口被標記為`MM2S (Memory-Mapped to Stream)`和`S2MM (Stream to Memory-Mapped)`。目前可以將這些視為讀取或寫入`DRAM`的`ports`。  
  
Control port:  
`DMA`有一個`AXI lite control port`，用於寫入指令來配置、啟動和停止`DMA`，並讀取狀態（原文: `readback status`）。  
  
AXI Masters:  
有兩個`AXI Master ports`連接到`DRAM`。`M_AXI_MM2S (READ channel)`和`M_AXI_S2MM (WRITE channel)`。`AXI masters`可以讀取和寫入記憶體。在此教學中，將連接到`Zynq HP (High Performance) AXI Slave ports`。  
`HP ports`的寬度`width`可以在`Vivado`中更改，但是當`PYNQ`啟動開發板時，這些`ports`會被配置（原文: `These ports are configured when PYNQ boots the board.`）。需要確保`Vivado`設計中的`ports`寬度與`PYNQ`啟動設定相符。在所有官方的 `PYNQ`的`image`中，`HP ports`的寬度`width`為`64-bit`。  
  
如果設計中錯誤地將`HP ports`設定為`32-bit`，可能會看到每`64-bits`只有`32-bits`被正確傳輸。  
  
`DMA`有兩個`AXI stream ports`，一個是`AXI master Stream (M_AXIS_MM2S)`，對應於`READ channel`。資料將通過`M_AXI_MM2S port`從記憶體讀取，並發送到`M_AXIS_MM2S port`（並傳送到連接到此`port`的`IP`）。  
另一個`AXI stream port`是`AXI Slave (S_AXIS_S2MM)`，連接到`IP`。`DMA`從`IP`接收`AXI stream`資料，並通過`M_AXI_S2MM port`將其寫回記憶體。  
  
如果`IP`尚未準備好從`M_AXIS port`接收資料，則此`port`將停滯（原文: `This port will stall.`）。也可以使用`AXI Stream FIFOs`。  
如果`IP`嘗試寫回資料，但`DMA`寫入尚未開始，則`S_AXIS channel`將使`IP`停滯。如果需要可以使用`FIFOs`。  
`DMA`內建了一些緩衝`built in buffering`，所以如果正在試圖除錯，可能會看到一些（或全部）資料從記憶體讀取，但它可能並未必然被發送到你的`IP`，並可能在內部或`HP port FIFOs`中排隊。  
  
Scatter gather support:  
`PYNQ`不支援`DMA`的`scatter gather`功能。這是可以從碎片化或不連續的記憶體位置傳輸資料的功能（原文: `Data can be transferred from fragmented or disjointed memory locations.`）。`PYNQ`僅支援從`contiguous memory buffers`的`DMA`。  
可以在`DMA`上啟用`Scatter-Gather`，以允許多次傳輸最多`8,388,608 bytes`（來自`contiguous memory buffers`）。如果這樣做，需要使用`SG M_AXI ports`而不是`M_AXI ports`。對於大型傳輸，`SG`的替代方案是在軟體中將你的記憶體傳輸分段成`67,108,863`或更少的片段，並運行多個`DMA`傳輸。  
  
## 參考連結  
[PYNQ DMA tutorial (Part 1: Hardware design)](https://discuss.pynq.io/t/tutorial-pynq-dma-part-1-hardware-design/3133)  
[DMA](https://pynq.readthedocs.io/en/latest/pynq_libraries/dma.html)  