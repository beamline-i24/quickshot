#!/bin/usr/python
import pv
from time import sleep
from ca import caput, caget 

def flush_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

def beamline(action, args_list=None):
    print '\n***** Entering Beamline'
    print 'beamline - ', action
    if args_list:
        for arg in args_list: print arg
    
    # Not sure when this is used
    if action == 'safe-mount':
        caput(pv.fluo_trans, 'OUT')
        caput(pv.ap1_mp_select, 'Out')

    elif action == 'fluorescence-collect':
        caput(pv.shtr_ctrl1, 'Maual')
        caput(pv.fluo_trans, 'IN')
        caput(pv.ap1_mp_select, 'In')
        #caput(pv.absb_mp_select, 'Rotatable')
        caput(pv.absb_mp_select, 'Data Collection Far')
        #sleep(2)
        #caput(pv.absb_roty, 186)
        #sleep(1)
        caput(pv.blight_mp_select, 'In')

    elif action == 'collect':
        caput(pv.ap1_mp_select, 'In')
        caput(pv.absb_mp_select, 'Data Collection')
        caput(pv.absb_roty, 6)
        sleep(4)
        caput(pv.blight_mp_select, 'Out')
        sleep(2)

    elif action == 'grid-collect':
        caput(pv.det_z, 500)
        caput(pv.blight_mp_select, 'Out')

    elif action == 'quickshot':
        print 'quickshot', args_list
        det_dist = args_list[0]
        caput(pv.det_z, det_dist)
        actual_dist = str(int(caget(pv.det_z+'.RBV')))
        requested_dist = str(int(det_dist)) 
        while actual_dist != requested_dist:
            #text = '%s %s' %(actual_dist, requested_dist)
            #flush_print(text)
            actual_dist = str(int(caget(pv.det_z+'.RBV')))
            sleep(0.2)
    
    elif action == 'return-to-normal':
        print 'Return to Normal'
        print 80*'!'
        modechange('Tray_switch2pin')
        print 80*'!'

    else:
        print 'Unknown action for beamline method', action
        sleep(0.1)

    print '***** leaving beamline'
    return 1

def pilatus(action, args_list=None):
    print '\n***** Entering Pilatus'
    print 'pilatus - ', action
    if args_list:
        for arg in args_list: print arg

    lamb = caget(pv.dcm_lambda)
    dist = caget(pv.det_z)
    att = caget(pv.att_match)
    caput(pv.pilat_wavelength, lamb)
    caput(pv.pilat_detdist, dist)
    caput(pv.pilat_filtertrasm, att)
    sleep(0.1)

    # fast grid scans to replace GDA
    if action == 'pmcgrid':
        [filepath, filename, total_numb_imgs, exptime] = args_list
        rampath = filepath.replace('dls/i02-2/data','ramdisk')
        acqtime = exptime - 0.001
        print 'filepath was set as', filepath
        print 'Rampath set as', rampath
        print 'Filename set as', filename 
        print 'total_numb_imgs', total_numb_imgs 
        print 'Exposure time set as', exptime, 's'
        print 'Acquire time set as', acqtime, 's'
        caput(pv.pilat_filepath, rampath + filename + '/')
        caput(pv.pilat_filename, filename)
        caput(pv.pilat_numimages, str(total_numb_imgs))
        caput(pv.pilat_acquiretime, str(acqtime))
        caput(pv.pilat_acquireperiod, str(exptime))
        caput(pv.pilat_triggermode, 'Mult. Trigger')
        caput(pv.pilat_delaytime, 0)

    # Fixed Target stage (very fast start and stop w/ triggering from GeoBrick
    elif action == 'fastchip':
        [filepath, filename, total_numb_imgs, exptime] = args_list
        rampath = filepath.replace('dls/i02-2/data','ramdisk')
        acqtime = exptime - 0.001
        print 'filepath was set as', filepath
        print 'Rampath set as', rampath
        print 'Filename set as', filename 
        print 'total_numb_imgs', total_numb_imgs 
        print 'Exposure time set as', exptime, 's'
        print 'Acquire time set as', acqtime, 's'
        caput(pv.pilat_filepath, rampath + filename + '/')
        caput(pv.pilat_filename, filename)
        caput(pv.pilat_numimages, str(total_numb_imgs))
        caput(pv.pilat_acquiretime, str(acqtime))
        caput(pv.pilat_acquireperiod, str(exptime))
        caput(pv.pilat_triggermode, 'Mult. Trigger')
        caput(pv.pilat_delaytime, 0)

    # Originally designed for small oscillation grids
    elif action == 'back-and-forth':
        [filepath, filename, total_numb_imgs, exptime] = args_list
        rampath = filepath.replace('dls/i02-2/data','ramdisk')
        acqtime = exptime - 0.01
        print 'filepath was set as', filepath
        print 'Rampath set as', rampath
        print 'Filename set as', filename 
        print 'total_numb_imgs', total_numb_imgs 
        print 'Exposure time set as', exptime, 's'
        print 'Acquire time set as', acqtime, 's'
        caput(pv.pilat_filepath, rampath)
        caput(pv.pilat_filename, filename)
        caput(pv.pilat_numimages, str(total_numb_imgs))
        caput(pv.pilat_acquiretime, str(acqtime))
        caput(pv.pilat_acquireperiod, str(exptime))
        caput(pv.pilat_imagemode, 'Multiple')
        caput(pv.pilat_triggermode, 'Ext. Trigger')
        caput(pv.pilat_delaytime, 0.000) #0.030
    
    #Collect multiple images from a non-moving target
    elif action == 'grid-collect':
        [filepath, filename, total_numb_imgs, exptime] = args_list
        rampath = filepath.replace('dls/i02-2/data','ramdisk')
        acqtime = exptime - 0.001
        print 'filepath was set as', filepath
        print 'Rampath set as', rampath
        print 'Filename set as', filename 
        print 'total_numb_imgs', total_numb_imgs 
        print 'Exposure time set as', exptime, 's'
        print 'Acquire time set as', acqtime, 's'
        caput(pv.pilat_filepath, rampath)
        sleep(0.1)
        print 'xx'
        caput(pv.pilat_filename, filename)
        sleep(0.1)
        print 'xxx'
        # caput(pv.pilat_file_num, 1)
        # Delay time needs checking
        caput(pv.pilat_delaytime, 0.03)
        # Read timeout needs to be number of images * Acq time + ??
        caput(pv.pilat_numimages, str(total_numb_imgs))
        caput(pv.pilat_acquiretime, str(acqtime))
        caput(pv.pilat_acquireperiod, str(exptime))
        caput(pv.pilat_triggermode, 'Ext. Trigger')
        # Template should be %s%s%04d.cbf normally
        # set to %s%s06d.cbf for collection
        print 'Have you set template to 06d?'
        #caput(pv.pilat_filename_template, '')

    # Quick set of images no coordinated motion 
    elif action == 'quickshot':
        print 'quickshot'
        [filepath, filename, num_imgs, exptime] = args_list
        print 'filepath was set as', filepath
        rampath = filepath.replace('dls/i02-2/data','ramdisk')
        print 'Rampath set as', rampath
        caput(pv.pilat_filepath, rampath)
        sleep(0.1)
        print 'Filename set as', filename 
        caput(pv.pilat_filename, filename)
        sleep(0.1)
        print 'num_imgs', num_imgs 
        acqtime = exptime - 0.001
        print 'Acquire time set as', acqtime, 's'
        caput(pv.pilat_acquiretime, str(acqtime))
        print 'Exposure time set as', exptime, 's'
        caput(pv.pilat_acquireperiod, str(exptime))
        print 'Pilatus takes time apprx 2sec'
        sleep(2)
        caput(pv.pilat_delaytime, 0.00)
        caput(pv.pilat_numimages, str(num_imgs))
        caput(pv.pilat_imagemode, 'Continuous')
        caput(pv.pilat_triggermode, 'Ext. Trigger')
        sleep(0.2)

    # Put it all back to GDA acceptable defaults
    elif action == 'return to normal':
        print 'Not Sure What to do in here yet'
    print '***** leaving pilatus'
    sleep(0.1)
    return 0

def xpress3(action, args_list=None):
    print '\n***** Entering xpress3'
    print 'xpress3 -', action
    if args_list:
        for arg in args_list: print arg

    if action == 'stop-and-start':
        [exp_time, lo, hi] = args_list
        caput(pv.xsp3_triggermode, 'Internal')
        caput(pv.xsp3_numimages, 1)
        caput(pv.xsp3_acquiretime, exp_time)
        caput(pv.xsp3_c1_mca_roi1_llm, lo)
        caput(pv.xsp3_c1_mca_roi1_hlm, hi)
        sleep(0.2)
        caput(pv.xsp3_c1_mca_roi1_llm, lo)
        caput(pv.xsp3_c1_mca_roi1_hlm, hi)
        sleep(0.2)
        caput(pv.xsp3_erase, 0)

    elif action == 'on-the-fly':
        [num_frms, lo, hi] = args_list
        caput(pv.xsp3_triggermode, 'TTL Veto Only')
        caput(pv.xsp3_numimages, num_frms)
        caput(pv.xsp3_c1_mca_roi1_llm, lo)
        caput(pv.xsp3_c1_mca_roi1_hlm, hi)
        sleep(0.2)
        caput(pv.xsp3_c1_mca_roi1_llm, lo)
        caput(pv.xsp3_c1_mca_roi1_hlm, hi)
        sleep(0.2)
        caput(pv.xsp3_erase, 0)

    elif action == 'return-to-normal':
        caput(pv.xsp3_triggermode, 'TTL Veto Only')
        caput(pv.xsp3_numimages, 1)
        caput(pv.xsp3_acquiretime, 1)
        caput(pv.xsp3_c1_mca_roi1_llm, 0)
        caput(pv.xsp3_c1_mca_roi1_hlm, 0)
        caput(pv.xsp3_erase, 0)

    else:
        print 'Unknown action for xpress3 method:', action

    sleep(0.1)
    print '***** leaving xpress3'
    return 1

def zebra1(action, args_list=None):
    print '\n***** Entering zebra1'
    print 'zebra1 -', action
    if args_list:
        for arg in args_list: print arg

    if action == 'quickshot':
        [gate_start, gate_width] = args_list
        #Trig Source is soft SOFT_IN2
        caput(pv.zebra1_pc_arm_sel, 'Soft')
        caput(pv.zebra1_pc_gate_sel, 'Time')
        caput(pv.zebra1_pc_pulse_sel, 'External')
        caput(pv.zebra1_pc_gate_start, str(gate_start))
        caput(pv.zebra1_pc_gate_wid, str(gate_width))
        caput(pv.zebra1_pc_gate_inp, '61')
        sleep(0.1)
        caput(pv.zebra1_pc_gate_inp, '61')
        sleep(0.1)

    elif action == 'pmcgrid':
        caput(pv.zebra1_soft_in_b0, '0')
        caput(pv.zebra1_pc_gate_sel, 'External')
        caput(pv.zebra1_pc_pulse_sel, 'External')
        caput(pv.zebra1_and3_inp1, '61')
        caput(pv.zebra1_and3_inp2, '1')
        caput(pv.zebra1_out2_ttl, '34')
        caput(pv.zebra1_pc_gate_inp, '61')
        caput(pv.zebra1_pc_pulse_inp, '1')

    elif action == 'stop-and-start':
        caput(pv.zebra1_soft_in_b0, '0')
        caput(pv.zebra1_pc_gate_sel, 'External')
        caput(pv.zebra1_pc_pulse_sel, 'External')
        caput(pv.zebra1_and3_inp1, '61')
        caput(pv.zebra1_and3_inp2, '1')
        caput(pv.zebra1_out2_ttl, '34')
        caput(pv.zebra1_pc_gate_inp, '61')
        caput(pv.zebra1_pc_pulse_inp, '1')

    elif action == 'on-the-fly':
        [x_size, step_size, start_pos_x] = args_list
        caput(pv.zebra1_pc_pulse_sel, 'Position')
        caput(pv.zebra1_pc_enc, 'Enc3')
        caput(pv.zebra1_pc_dir, 'Positive')
        caput(pv.zebra1_pc_gate_start, start_pos_x)
        caput(pv.zebra1_pc_gate_width, x_size)
        caput(pv.zebra1_out3_ttl, '31')
        pulse_width = step_size - 0.0001
        caput(pv.zebra1_pc_pulse_start, 0.0)
        caput(pv.zebra1_pc_pulse_width, pulse_width)
        caput(pv.zebra1_pc_pulse_step, step_size)

    elif action == 'back-and-forth':
        [gate_width] = args_list
        caput(pv.zebra1_pc_disarm, 1)
        caput(pv.zebra1_pc_enc, 'Enc2')
        caput(pv.zebra1_pc_dir, 'Positive')
        caput(pv.zebra1_pc_gate_width, gate_width)

    elif action == 'grid-collect':
	    #Trig Source is 'Soft'
        caput(pv.zebra1_and3_inp1, '61')
        caput(pv.zebra1_pc_gate_sel, 'External')

    elif action == 'return-to-normal':
        config_fid = '/dls_sw/i02-2/epics/zebra/zebra1.dat'
        print 'Loading Config File to Zebra1', config_fid
        caput(pv.zebra1_config_file, config_fid)
        sleep(0.2)
        val = caget(pv.zebra1_config_read_proc)
        caput(pv.zebra1_config_read_proc, 1)
        sleep(2)
        print 'Zebra file restore finished'


    else:
        print 'Unknown action for zebra1 method', action
        sleep(0.1)
    print '***** leaving zebra1'
    return 1

def returntonormal():
    print '\n***** Entering Return To Normal'
    print 'returntonormal - '
    caput(pv.zebra1_disarm, 1)
    caput(pv.shtr_ctrl2, 'Close')
    caput(pv.shtr_ctrl1, 'Auto')
    zebra1('return-to-normal')
    beamline('Tray_switch2pin')
    pilatus('return-to-normal')
    xpress3('return-to-normal')
    print '***** leaving returntonormal'

def main():
    print 'Hello World!'

if __name__ == '__main__':
    main()
