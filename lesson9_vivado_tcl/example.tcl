# Weng20011103 - June - 14 - 2024 - Created !

# This is the tcl script which build our example system.

# Created Project
create_project project_1 F:/EE/20240621/project_1 -part xczu9eg-ffvb1156-2-e
set_property board_part xilinx.com:zcu102:part0:3.4 [current_project]

# create block design
create_bd_design "design_1"
update_compile_order -fileset sources_1

# add the Zynq UltraScale+ MPSoC to the block design
startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:zynq_ultra_ps_e:3.3 zynq_ultra_ps_e_0
endgroup

# add the AXI GPIO to the block design
startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:axi_gpio:2.0 axi_gpio_0
endgroup

# change the axi_gpio_0 IP configuration
set_property -dict [list CONFIG.C_GPIO_WIDTH {8} CONFIG.C_ALL_OUTPUTS {1}] [get_bd_cells axi_gpio_0]

# add the led.v module
add_files -norecurse C:/Users/user/Downloads/led.v
update_compile_order -fileset sources_1

# add the led.v module to the block design
create_bd_cell -type module -reference led led_0

# connect axi_gpio_0/gpio_io_o to led_0/LED_in
connect_bd_net [get_bd_pins axi_gpio_0/gpio_io_o] [get_bd_pins led_0/LED_in]

# make external pins and change external ports name
startgroup
make_bd_pins_external  [get_bd_pins led_0/LED_out]
endgroup

set_property name LED_out [get_bd_ports LED_out_0]

# run connection automation
apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/zynq_ultra_ps_e_0/M_AXI_HPM0_LPD} Slave {/axi_gpio_0/S_AXI} ddr_seg {Auto} intc_ip {New AXI Interconnect} master_apm {0}}  [get_bd_intf_pins axi_gpio_0/S_AXI]

# create HDL wrapper
make_wrapper -files [get_files F:/EE/20240621/project_1/project_1.srcs/sources_1/bd/design_1/design_1.bd] -top
add_files -norecurse f:/EE/20240621/project_1/project_1.gen/sources_1/bd/design_1/hdl/design_1_wrapper.v
update_compile_order -fileset sources_1
update_compile_order -fileset sources_1

# add the led.xdc file
add_files -fileset constrs_1 -norecurse C:/Users/user/Downloads/led.xdc

# generate bitstream
launch_runs impl_1 -to_step write_bitstream -jobs 10