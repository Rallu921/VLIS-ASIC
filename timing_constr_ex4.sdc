# create clock clk 
create_clock -period 8 -name clk -waveform {0 5} [get_ports clk]	       	  	     			
# set clock latency
set_clock_latency 0.4 [get_clocks clk]					
# set clock uncertainty
set_clock_uncertainty 0.05 [get_clocks clk] 
					
# clock transition time
set_clock_transition 0.1 [get_clocks clk]	
# set max output delay
set_output_delay -clock clk -max 1 -network_latency_included [all_outputs]
	
# set min output delay
set_output_delay -clock clk -min 0.4 -network_latency_included [all_outputs]    			       			
# set max load
set_load -max 0.5 [all_outputs]	 						
# set min load
set_load -min 0.01 [all_outputs]	
# set max input delay
set_input_delay -clock clk -max 1 -network_latency_included [all_inputs]	
# set min inout delay
set_input_delay -clock clk -min 0.4 -network_latency_included [all_inputs]	      			
# set max driving cell as BUFX2
set_driving_cell -lib_cell BUFX2 -max [all_inputs]
# set min driving cell as BUFX16
set_driving_cell -lib_cell BUFX16 -min [all_inputs]				




