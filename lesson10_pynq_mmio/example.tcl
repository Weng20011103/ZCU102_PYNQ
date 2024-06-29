create_project project_1 ./project_1 -part xczu9eg-ffvb1156-2-e

set_property board_part xilinx.com:zcu102:part0:3.4 [current_project]
set_property  ip_repo_paths  ./ip_repo/Blink_1.0 [current_project]
update_ip_catalog

create_bd_design "design_1"
update_compile_order -fileset sources_1

startgroup
create_bd_cell -type ip -vlnv xilinx.com:ip:zynq_ultra_ps_e:3.3 zynq_ultra_ps_e_0
endgroup

startgroup
create_bd_cell -type ip -vlnv xilinx.com:user:Blink:1.0 Blink_0
endgroup

apply_bd_automation -rule xilinx.com:bd_rule:axi4 -config { Clk_master {Auto} Clk_slave {Auto} Clk_xbar {Auto} Master {/zynq_ultra_ps_e_0/M_AXI_HPM0_LPD} Slave {/Blink_0/S00_AXI} ddr_seg {Auto} intc_ip {New AXI Interconnect} master_apm {0}}  [get_bd_intf_pins Blink_0/S00_AXI]

startgroup
make_bd_pins_external  [get_bd_pins Blink_0/leds]
endgroup

make_wrapper -files [get_files ./project_1/project_1.srcs/sources_1/bd/design_1/design_1.bd] -top

add_files -norecurse ./project_1/project_1.gen/sources_1/bd/design_1/hdl/design_1_wrapper.v
add_files -fileset constrs_1 -norecurse ./lesson10.xdc

launch_runs impl_1 -to_step write_bitstream -jobs 10