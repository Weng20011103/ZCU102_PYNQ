# ZCU102 PYNQ  
使用的版本為`Vivado 2020.2`和`PYNQ v2.7`。  
  
## 課程目錄  
[第一課: 由GPIO設定點亮GPIO LED](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson1_LED_kirakira_gpio#%E7%AC%AC%E4%B8%80%E8%AA%B2-%E7%94%B1-gpio-%E8%A8%AD%E5%AE%9A%E9%BB%9E%E4%BA%AE-gpio-led)  
[第二課: 由XDC綁定腳位點亮GPIO LED](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson2_LED_kirakira_xdc#%E7%AC%AC%E4%BA%8C%E8%AA%B2-%E7%94%B1-xdc-%E7%B6%81%E5%AE%9A%E8%85%B3%E4%BD%8D%E9%BB%9E%E4%BA%AE-gpio-led)  
[第三課: 由PYNQ載入bit檔點亮GPIO LED](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson3_pynq_led#%E7%AC%AC%E4%B8%89%E8%AA%B2-%E7%94%B1-pynq-%E8%BC%89%E5%85%A5-bit-%E6%AA%94%E9%BB%9E%E4%BA%AE-gpio-led)  
[第四課: 由PYNQ寫入GPIO控制DAC輸出電壓](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson4_dac_control_by_pynq#%E7%AC%AC%E5%9B%9B%E8%AA%B2-%E7%94%B1-pynq-%E5%AF%AB%E5%85%A5-gpio-%E6%8E%A7%E5%88%B6-dac-%E8%BC%B8%E5%87%BA%E9%9B%BB%E5%A3%93)  
[第五課: 由Clocking Wizard創造時鐘訊號及PYNQ檔案限制](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson5_clocking_wizard_and_ps#%E7%AC%AC%E4%BA%94%E8%AA%B2-%E7%94%B1-clocking-wizard-%E5%89%B5%E9%80%A0%E6%99%82%E9%90%98%E8%A8%8A%E8%99%9F%E5%8F%8A-pynq-%E6%AA%94%E6%A1%88%E9%99%90%E5%88%B6)  
[第六課: PYNQ DMA範例](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson6_dma_demo#%E7%AC%AC%E5%85%AD%E8%AA%B2-pynq-dma-%E7%AF%84%E4%BE%8B)  
[第七課: PYNQ HLS IP範例](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson7_hls_demo#%E7%AC%AC%E4%B8%83%E8%AA%B2-pynq-hls-ip-%E7%AF%84%E4%BE%8B)  
[第八課: 新增一個AXI4-Lite的自定義IP](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson8_axi_lite_custom_ip#%E7%AC%AC%E5%85%AB%E8%AA%B2-%E6%96%B0%E5%A2%9E%E4%B8%80%E5%80%8Baxi4-lite%E7%9A%84%E8%87%AA%E5%AE%9A%E7%BE%A9ip)  
[第九課: 在Vivado中使用TCL腳本](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson9_vivado_tcl#%E7%AC%AC%E4%B9%9D%E8%AA%B2-%E5%9C%A8vivado%E4%B8%AD%E4%BD%BF%E7%94%A8tcl%E8%85%B3%E6%9C%AC)  
[第十課: PYNQ MMIO示範](https://github.com/Weng20011103/ZCU102_PYNQ/tree/main/lesson10_pynq_mmio#%E7%AC%AC%E5%8D%81%E8%AA%B2-pynq-mmio%E7%A4%BA%E7%AF%84)  
  
## ZCU102 參考連接  
[Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)  
[Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit - Known Issues and Release Notes Master Answer Record](https://support.xilinx.com/s/article/66752?language=en_US)  
[ZCU102 Evaluation Board User Guide (UG1182)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)  
  
## Intellectual Property 參考連接  
[AXI General Purpose IO](https://www.xilinx.com/products/intellectual-property/axi_gpio.html)  
[AXI DMA Controller](https://www.xilinx.com/products/intellectual-property/axi_dma.html#overview)  
[AXI4-Stream Data FIFO](https://docs.amd.com/r/en-US/pg085-axi4stream-infrastructure/AXI4-Stream-Data-FIFO?tocId=gyNUSa81sSudIrD3MNZ6aw)  
[Clocking Wizard](https://www.xilinx.com/products/intellectual-property/clocking_wizard.html)  
  
## PYNQ 參考連接  
[PYNQ官網](https://www.pynq.io/)  
[PYNQ介紹網站](https://pynq.readthedocs.io/en/latest/)  
[PYNQ GitHub](https://github.com/Xilinx/PYNQ)  
[PYNQ Workshop for v2.6](https://github.com/Xilinx/PYNQ_Workshop)  
  
## Zynq UltraScale+  
1. [Zynq UltraScale+ MPSoC Data Sheet: Overview (DS891)](https://docs.amd.com/v/u/en-US/ds891-zynq-ultrascale-plus-overview)  
2. [Zynq UltraScale+ MPSoC Technical Reference Manual (UG1085)](https://docs.amd.com/r/en-US/ug1085-zynq-ultrascale-trm/Zynq-UltraScale-Device-Technical-Reference-Manual)  
3. [UltraScale Architecture FPGAs Memory Interface Solutions LogiCORE IP Product Guide (PG150)](https://docs.amd.com/v/u/en-US/pg150-ultrascale-memory-ip)  
4. [UltraScale Architecture SelectIO Resources User Guide (UG571)](https://docs.amd.com/r/en-US/ug571-ultrascale-selectio/UltraScale-Architecture-SelectIO-Resources-User-Guide)  
5. [Silicon Labs CP210x USB-to-UART Installation Guide (UG1033)](https://docs.amd.com/v/u/en-US/ug1033-cp210x-usb-uart-install)  
6. [Vivado Design Suite User Guide: Using Constraints User Guide (UG903)](https://docs.amd.com/r/en-US/ug903-vivado-using-constraints/Introduction)  
7. [UltraScale Architecture System Monitor User Guide (UG580)](https://docs.amd.com/v/u/en-US/ug580-ultrascale-sysmon)  