################################################################################
#
# Init setup file
# Created by Genus(TM) Synthesis Solution on 11/28/2022 21:55:02
#
################################################################################

      if { ![is_common_ui_mode] } {
        error "This script must be loaded into an 'innovus -stylus' session."
      }
    


read_mmmc genus_invs_des/genus.mmmc.tcl

read_physical -lef {}

read_netlist genus_invs_des/genus.v

init_design
