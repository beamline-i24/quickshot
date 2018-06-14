#!/usr/bin/python
import os, sys
###############
# 28 Feb 2017 #
###############
def __show__(name):
    """Checks available variables given a string, uses first two letters"""
    for things in globals():
	    if name[:2].lower() in things.lower():
	        print 'Available:', things
    print

def __which__():
    """Return script directory, used for finding which pv.py you are running"""
    pathname, scriptname = os.path.split(sys.argv[0])
    print("Script dir: "+ os.path.abspath(pathname))

#PILATUS 
pilat_filepath      = 'BL02I-EA-PILAT-01:cam1:FilePath'
pilat_filename      = 'BL02I-EA-PILAT-01:cam1:FileName'
pilat_filetemplate  = 'BL02I-EA-PILAT-01:cam1:FileTemplate'
pilat_numimages     = 'BL02I-EA-PILAT-01:cam1:NumImages'
pilat_filenumber    = 'BL02I-EA-PILAT-01:cam1:FileNumber'
pilat_acquire       = 'BL02I-EA-PILAT-01:cam1:Acquire'
pilat_acquiretime   = 'BL02I-EA-PILAT-01:cam1:AcquireTime'
pilat_acquireperiod = 'BL02I-EA-PILAT-01:cam1:AcquirePeriod'
pilat_imagemode     = 'BL02I-EA-PILAT-01:cam1:ImageMode'
pilat_triggermode   = 'BL02I-EA-PILAT-01:cam1:TriggerMode'
pilat_delaytime     = 'BL02I-EA-PILAT-01:cam1:DelayTime'
pilat_wavelength    = 'BL02I-EA-PILAT-01:cam1:Wavelength'
pilat_detdist       = 'BL02I-EA-PILAT-01:cam1:DetDist'
pilat_filtertrasm   = 'BL02I-EA-PILAT-01:cam1:FilterTrasm'
pilat_filetemplate  = 'BL02I-EA-PILAT-01:cam1:FileTemplate'
pilat_beamx         = 'BL02I-EA-PILAT-01:cam1:BeamX'
pilat_beamy         = 'BL02I-EA-PILAT-01:cam1:BeamY'
#ZEBRA
zebra1_and2_inp1        = 'BL02I-EA-ZEBRA-01:AND2_INP1'
zebra1_and2_inp2        = 'BL02I-EA-ZEBRA-01:AND2_INP2'
zebra1_and3_inp1        = 'BL02I-EA-ZEBRA-01:AND3_INP1'
zebra1_and3_inp2        = 'BL02I-EA-ZEBRA-01:AND3_INP2'
zebra1_out1_ttl         = 'BL02I-EA-ZEBRA-01:OUT1_TTL'
zebra1_out2_ttl         = 'BL02I-EA-ZEBRA-01:OUT2_TTL'
zebra1_out3_ttl         = 'BL02I-EA-ZEBRA-01:OUT3_TTL'
zebra1_out4_ttl         = 'BL02I-EA-ZEBRA-01:OUT4_TTL'
zebra1_pc_arm_out       = 'BL02I-EA-ZEBRA-01:PC_ARM_OUT'
zebra1_pc_arm           = 'BL02I-EA-ZEBRA-01:PC_ARM'
zebra1_pc_disarm        = 'BL02I-EA-ZEBRA-01:PC_DISARM'
zebra1_pc_arm_sel       = 'BL02I-EA-ZEBRA-01:PC_ARM_SEL'
zebra1_pc_gate_sel      = 'BL02I-EA-ZEBRA-01:PC_GATE_SEL'
zebra1_pc_gate_inp      = 'BL02I-EA-ZEBRA-01:PC_GATE_INP'
zebra1_pc_gate_start    = 'BL02I-EA-ZEBRA-01:PC_GATE_START'
zebra1_pc_gate_wid      = 'BL02I-EA-ZEBRA-01:PC_GATE_WID'
zebra1_pc_pulse_sel     = 'BL02I-EA-ZEBRA-01:PC_PULSE_SEL'
zebra1_pc_pulse_inp     = 'BL02I-EA-ZEBRA-01:PC_PULSE_INP'
zebra1_pc_pulse_start   = 'BL02I-EA-ZEBRA-01:PC_PULSE_START'
zebra1_pc_pulse_wid     = 'BL02I-EA-ZEBRA-01:PC_PULSE_WID'
zebra1_pc_pulse_step    = 'BL02I-EA-ZEBRA-01:PC_PULSE_STEP'
zebra1_soft_in_b0       = 'BL02I-EA-ZEBRA-01:SOFT_IN:B0'
zebra1_soft_in_b1       = 'BL02I-EA-ZEBRA-01:SOFT_IN:B1'
zebra1_soft_in_b2       = 'BL02I-EA-ZEBRA-01:SOFT_IN:B2'
zebra1_pc_enc           = 'BL02I-EA-ZEBRA-01:PC_ENC'
zebra1_pc_dir           = 'BL02I-EA-ZEBRA-01:PC_DIR'
zebra1_reset_proc       = 'BL02I-EA-ZEBRA-01:SYS_RESET.PROC'
zebra1_config_file      = 'BL02I-EA-ZEBRA-01:CONFIG_FILE'
zebra1_config_read_proc = 'BL02I-EA-ZEBRA-01:CONFIG_READ.PROC'
zebra1_or1_ena_b0       = 'BL02I-EA-ZEBRA-01:OR1_ENA:B0'
#BPMs
qbpm1_inten = 'BL02I-DI-QBPM-01:INTEN'
qbpm2_inten = 'BL02I-DI-QBPM-02:INTEN'
qbpm3_inten = 'BL02I-DI-QBPM-03:INTEN'
#FAST SHUTTER
shtr_ctrl1 = 'BL02I-EA-SHTR-01:CTRL1'
shtr_ctrl2 = 'BL02I-EA-SHTR-01:CTRL2'
shtr_toggle = shtr_ctrl1
shtr_pos    = shtr_ctrl2
#XPRESS3
xsp3_acquire           = 'BL02I-EA-XSP3-01:Acquire'
xsp3_erase             = 'BL02I-EA-XSP3-01:ERASE'
xsp3_acquiretime       = 'BL02I-EA-XSP3-01:AcquireTime'
xsp3_numimages         = 'BL02I-EA-XSP3-01:NumImages'
xsp3_triggermode       = 'BL02I-EA-XSP3-01:TriggerMode' 
xsp3_c1_mca_roi1_llm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI1_LLM'
xsp3_c1_mca_roi2_llm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI2_LLM'
xsp3_c1_mca_roi3_llm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI3_LLM'
xsp3_c1_mca_roi4_llm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI4_LLM'
xsp3_c1_mca_roi1_hlm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI1_HLM'
xsp3_c1_mca_roi2_hlm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI2_HLM'
xsp3_c1_mca_roi3_hlm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI3_HLM'
xsp3_c1_mca_roi4_hlm   = 'BL02I-EA-XSP3-01:C1_MCA_ROI4_HLM'
xsp3_c1_roi1_value_rbv = 'BL02I-EA-XSP3-01:C1_ROI1:Value_RBV'
xsp3_c1_roi2_value_rbv = 'BL02I-EA-XSP3-01:C1_ROI2:Value_RBV'
xsp3_c1_roi3_value_rbv = 'BL02I-EA-XSP3-01:C1_ROI3:Value_RBV'
xsp3_c1_roi4_value_rbv = 'BL02I-EA-XSP3-01:C1_ROI4:Value_RBV'
# WBS White Beam Slits
wbs_x_gap     = 'BL02I-AL-SLITS-01:X:GAP'
wbs_x_inboard = 'BL02I-AL-SLITS-01:X:INBOARD'
wbs_y_gap     = 'BL02I-AL-SLITS-01:Y:GAP'
wbs_y_bottom  = 'BL02I-AL-SLITS-01:Y:BOTTOM'
# Mono
dcm_bragg  = 'BL02I-OP-DCM-01:BRAGG'
dcm_t2     = 'BL02I-OP-DCM-01:T2'
dcm_roll1  = 'BL02I-OP-DCM-01:ROLL1'
dcm_pitch2 = 'BL02I-OP-DCM-01:PITCH2'
dcm_lambda = 'BL02I-OP-DCM-01:LAMBDA'
dcm_energy = 'BL02I-OP-DCM-01:ENERGY'
# MBS1
mbs1_x_plus  = 'BL02I-AL-SLITS-02:X:PLUS'
mbs1_x_minus = 'BL02I-AL-SLITS-02:X:MINUS'
mbs1_y_plus  = 'BL02I-AL-SLITS-02:Y:PLUS'
mbs1_y_minus = 'BL02I-AL-SLITS-02:Y:MINUS'
# PreFocussing Mirrors
hpfm_y1 = 'BL02I-OP-HPFM-01:Y1'
hpfm_y2 = 'BL02I-OP-HPFM-01:Y2'
hpfm_y3 = 'BL02I-OP-HPFM-01:Y3'
hpfm_x1 = 'BL02I-OP-HPFM-01:X1'
hpfm_x2 = 'BL02I-OP-HPFM-01:X2'
vpfm_y1 = 'BL02I-OP-VPFM-01:Y1'
vpfm_y2 = 'BL02I-OP-VPFM-01:Y2'
vpfm_y3 = 'BL02I-OP-VPFM-01:Y3'
vpfm_x1 = 'BL02I-OP-VPFM-01:X1'
vpfm_x2 = 'BL02I-OP-VPFM-01:X2'
# MBS2
mbs2_x_gap     = 'BL02I-AL-SLITS-03:X:GAP'
mbs2_x_inboard = 'BL02I-AL-SLITS-03:X:INBOARD'
mbs2_y_gap     = 'BL02I-AL-SLITS-03:Y:GAP'
mbs2_y_top     = 'BL02I-AL-SLITS-03:Y:TOP'
# Lancelot
lance_x = 'BL02I-EA-DET-03:X'
lance_y = 'BL02I-EA-DET-03:Y'
# MBS3
mbs3_x_gap     = 'BL02I-AL-SLITS-04:X:GAP'
mbs3_x_inboard = 'BL02I-AL-SLITS-04:X:INBOARD'
mbs3_y_gap     = 'BL02I-AL-SLITS-04:Y:GAP'
mbs3_y_top     = 'BL02I-AL-SLITS-04:Y:TOP'
# MicroFocussing Mirrors
hmfm_x     = 'BL02I-OP-HMFM-01:X'
hmfm_y     = 'BL02I-OP-HMFM-01:Y'
hmfm_pitch = 'BL02I-OP-HMFM-01:PITCH'
vmfm_x     = 'BL02I-OP-VMFM-01:X'
vmfm_y     = 'BL02I-OP-VMFM-01:Y'
vmfm_pitch = 'BL02I-OP-VMFM-01:PITCH'
mtab_z     = 'BL02I-OP-MTAB-01:Z'
# Collimation Table
ctab_x1 = 'BL02I-MO-TABLE-01:X1'
ctab_x2 = 'BL02I-MO-TABLE-01:X2'
# Attenuators
att_disc1 = 'BL02I-OP-ATTN-01:DISC1'
att_disc2 = 'BL02I-OP-ATTN-01:DISC2'
att_match = 'BL02I-OP-ATTN-01:MATCH'
# ScatterGuard
sg1_x = 'BL02I-AL-GUARD-01:X'
sg1_y = 'BL02I-AL-GUARD-01:Y'
# APerture
ap1_x         = 'BL02I-AL-APTR-01:X'
ap1_y         = 'BL02I-AL-APTR-01:Y'
ap1_mp_select = 'BL02I-AL-APTR-01:MP:SELECT'
# Vertical Pin Goniometer
vgon_omega = 'BL02I-MO-GONIO-02:OMEGA'
vgon_kappa = 'BL02I-MO-GONIO-02:KAPPA'
vgon_phi   = 'BL02I-MO-GONIO-02:PHI'
vgon_pinxs = 'BL02I-MO-GONIO-02:PINXS'
vgon_pinyh = 'BL02I-MO-GONIO-02:PINYH'
vgon_pinzs = 'BL02I-MO-GONIO-02:PINZS'
ptab_x     = 'BL02I-MO-PTAB-01:X'
ptab_z     = 'BL02I-MO-PTAB-01:Z'
ptab_y     = 'BL02I-MO-PTAB-01:Y'
# Horizontal Tray Goniometer
hgon_omega  = 'BL02I-MO-GONIO-01:OMEGA'
hgon_trayys = 'BL02I-MO-GONIO-01:TRAYYS'
hgon_trayzs = 'BL02I-MO-GONIO-01:TRAYZS'
ttab_x      = 'BL02I-MO-TTAB-01:X'
ttab_y      = 'BL02I-MO-TTAB-01:Y'
ttab_z      = 'BL02I-MO-TTAB-01:Z'
# Cryo
cryo2_trans     = 'BL02I-CG-JET-01:TRANS'
cryo2_mp_select = 'BL02I-CG-JET-01:MP:SELECT'
cryo2_p1701     = 'BL02I-CG-JET-01:P1701'
# Beamstop
absb_x         = 'BL02I-RS-ABSB-02:X'
absb_y         = 'BL02I-RS-ABSB-02:Y'
absb_z         = 'BL02I-RS-ABSB-02:Z'
absb_roty      = 'BL02I-RS-ABSB-02:ROTY'
absb_mp_select = 'BL02I-RS-ABSB-02:MP:SELECT'
absb_roty      = 'BL02I-RS-ABSB-02:ROTY'
# LED
led1_doxcurrent_ouputcurrent = 'BL02I-DI-LED-01:DOXCURRENT:OUTPUTCURRENT'
led2_doxcurrent_ouputcurrent = 'BL02I-DI-LED-02:DOXCURRENT:OUTPUTCURRENT'
led3_doxcurrent_ouputcurrent = 'BL02I-DI-LED-03:DOXCURRENT:OUTPUTCURRENT'
led4_doxcurrent_ouputcurrent = 'BL02I-DI-LED-04:DOXCURRENT:OUTPUTCURRENT'
# Backlight
blight_y          = 'BL02I-MO-LIGHT-01:Y'
blight_mp_select = 'BL02I-MO-LIGHT-01:MP:SELECT'
# Detector
det_y = 'BL02I-EA-DET-01:Y'
det_z = 'BL02I-EA-DET-01:Z'
# Fast grid diagnostics
pmc_gridstatus  = 'BL02I-MO-STEP-10:signal:P2401'
pmc_gridcounter = 'BL02I-MO-STEP-10:signal:P2402'
# Fluorescence Detector 
fluo_trans     = 'BL02I-EA-DET-02:TRANS'
fluo_out_limit = 'BL02I-EA-DET-02:OUT:LIMIT'
# PMAC Strings
step08_pmac_str = 'BL02I-MO-IOC-08:ASYN8.AOUT'
step09_pmac_str = 'BL02I-MO-IOC-09:ASYN9.AOUT'
step10_pmac_str = 'BL02I-MO-IOC-10:ASYN10.AOUT'
step11_pmac_str = 'BL02I-MO-IOC-11:ASYN11.AOUT'
step12_pmac_str = 'BL02I-MO-IOC-12:ASYN12.AOUT'
step08_pmac_response = 'BL02I-MO-IOC-08:ASYN8.AINP'
step09_pmac_response = 'BL02I-MO-IOC-09:ASYN9.AINP'
step10_pmac_response = 'BL02I-MO-IOC-10:ASYN10.AINP'
step11_pmac_response = 'BL02I-MO-IOC-11:ASYN11.AINP'
step12_pmac_response = 'BL02I-MO-IOC-12:ASYN12.AINP'
# General Purpose PV
iocxx_gp1  = 'BL02I-EA-IOC-xx:GP1'
iocxx_gp2  = 'BL02I-EA-IOC-xx:GP2'
iocxx_gp3  = 'BL02I-EA-IOC-xx:GP3'
iocxx_gp4  = 'BL02I-EA-IOC-xx:GP4'
iocxx_gp5  = 'BL02I-EA-IOC-xx:GP5'
iocxx_gp6  = 'BL02I-EA-IOC-xx:GP6'
iocxx_gp7  = 'BL02I-EA-IOC-xx:GP7'
iocxx_gp8  = 'BL02I-EA-IOC-xx:GP8'
iocxx_gp9  = 'BL02I-EA-IOC-xx:GP9'
iocxx_gp10 = 'BL02I-EA-IOC-xx:GP10'
iocxx_gp11 = 'BL02I-EA-IOC-xx:GP11'
iocxx_gp12 = 'BL02I-EA-IOC-xx:GP12'
iocxx_gp13 = 'BL02I-EA-IOC-xx:GP13'
iocxx_gp14 = 'BL02I-EA-IOC-xx:GP14'
iocxx_gp15 = 'BL02I-EA-IOC-xx:GP15'
