###############################################################
#  Generated by:      Cadence Innovus 19.11-s128_1
#  OS:                Linux x86_64(Host ID cn98.it.auth.gr)
#  Generated on:      Fri Feb 10 23:22:25 2023
#  Design:            picorv32
#  Command:           create_ccopt_clock_tree_spec -file clock_tree.spec
###############################################################
#-------------------------------------------------------------------------------
# Clock tree setup script - dialect: Innovus
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

if { [get_ccopt_clock_trees] != {} } {
  error {Cannot run clock tree spec: clock trees are already defined.}
}

namespace eval ::ccopt {}
namespace eval ::ccopt::ilm {}
set ::ccopt::ilm::ccoptSpecRestoreData {}
# Start by checking for unflattened ILMs.
# Will flatten if so and then check the db sync.
if { [catch {ccopt_check_and_flatten_ilms_no_restore}] } {
  return -code error
}
# cache the value of the restore command output by the ILM flattening code
set ::ccopt::ilm::ccoptSpecRestoreData $::ccopt::ilm::ccoptRestoreILMState

# Clocks present at pin clk
#   clk (period 10.000ns) in timing_config default_emulate_constraint_mode([genus_invs_des/genus.default_emulate_constraint_mode.sdc])
create_ccopt_clock_tree -name clk -source clk -no_skew_group
set_ccopt_property target_max_trans_sdc -delay_corner default_emulate_delay_corner -early -clock_tree clk 0.100

set_ccopt_property target_max_trans_sdc -delay_corner default_emulate_delay_corner -late -clock_tree clk 0.100
set_ccopt_property source_driver -clock_tree clk {BUFX2/A BUFX2/Y}
# Clock period setting for source pin of clk
set_ccopt_property clock_period -pin clk 10

# Skew group to balance non generated clock:clk in timing_config:default_emulate_constraint_mode (sdc genus_invs_des/genus.default_emulate_constraint_mode.sdc)
create_ccopt_skew_group -name clk/default_emulate_constraint_mode -sources clk -auto_sinks
set_ccopt_property include_source_latency -skew_group clk/default_emulate_constraint_mode true
set_ccopt_property extracted_from_clock_name -skew_group clk/default_emulate_constraint_mode clk
set_ccopt_property extracted_from_constraint_mode_name -skew_group clk/default_emulate_constraint_mode default_emulate_constraint_mode
set_ccopt_property extracted_from_delay_corners -skew_group clk/default_emulate_constraint_mode {default_emulate_delay_corner default_emulate_delay_corner}


check_ccopt_clock_tree_convergence
# Restore the ILM status if possible
if { [get_ccopt_property auto_design_state_for_ilms] == 0 } {
  if {$::ccopt::ilm::ccoptSpecRestoreData != {} } {
    eval $::ccopt::ilm::ccoptSpecRestoreData
  }
}
