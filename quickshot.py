#!/usr/bin/python
import pv, os, sys, time
import setup_beamline as sup
from time import sleep
from ca import caput, caget 

def flush_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()

def save_file(tmp_fid, fid):
    if os.path.isfile(fid):
        timestr = time.strftime("%Y%m%d_%H%M%S_")
        timestamp_fid = timestr + fid 
        os.rename(fid, timestamp_fid)
        print '\n', fid, 'already exists ... moving old file to:', timestamp_fid
        print 'Saving', fid
        os.rename(tmp_fid, fid)
        if os.path.isfile(fid):
            print fid, 'Saved'
        else:
            print 'An Error Occured Saving', fid
    else:
        print '\nSaving', fid
        os.rename(tmp_fid, fid)
        if os.path.isfile(fid):
            print fid, 'Saved'
        else:
            print 'An Error Occured Saving', fid

def scrape_control(control_fid):
    f = open(control_fid, 'r')
    for line in f.readlines():
        print '\t', line.rstrip(),
        entry = line.rstrip('\n').split(':')
        if entry[0].startswith('directory'):
            e = str(entry[1].lstrip())
            directory = '/' + e.rstrip('/').lstrip('/') + '/'
	    print
        elif entry[0].startswith('subdir'):
            e = str(entry[1].lstrip())
            subdir = e.rstrip('/').lstrip('/') + '/'
	    print
        elif entry[0].startswith('filename'):
            e = str(entry[1].lstrip())
            filename = e.rstrip('/').lstrip('/')
	    print
        elif entry[0].startswith('num_imgs'):
            num_imgs = int(entry[1].lstrip())
	    print
        elif entry[0].startswith('exp_time'):
            exp_time = float(entry[1].lstrip())
	    print
        elif entry[0].startswith('energy'):
            energy =  float(entry[1].lstrip())
	    print
        elif entry[0].startswith('det_dist'):
            det_dist =  float(entry[1].lstrip())
	    print
        elif entry[0].startswith('control_fid'):
            control_fid = str(entry[1].lstrip())
	    print
        else:
 	    print 80*'-', 'You Fucked Up', entry[0]
    f.close()
    return [directory, subdir, filename, num_imgs, exp_time, energy, det_dist, control_fid]

def run(control_fid):
    print 'Start of Run in quickshot.py'
    caput(pv.ioc12_gp8, 0)
    print control_fid
    [directory, subdir, filename, num_imgs, exp_time, energy, det_dist, control_fid]= scrape_control(control_fid)

    ######## Preperation
    sup.beamline('quickshot', [det_dist])
    
    filepath = directory + subdir 
    print '\n', filepath + filename, '\n'
    print 'Setting Shutter to Auto'
    caput(pv.shtr_ctrl1, 'Auto')
    
    sup.pilatus('quickshot', [filepath, filename, num_imgs, exp_time])
   
    gate_start = 1.0
    gate_width = (exp_time * num_imgs) + 0.5
    print 'gate_start', gate_start
    print 'gate_width', gate_width
    sup.zebra1('quickshot', [gate_start, gate_width]) 

    ########## Collect
    print 'pilatus acquire ON'  
    caput(pv.pilat_acquire, 1)
    sleep(0.2)
    caput(pv.pilat_acquire, 1)
    while True:
        # ioc12_gp8 is the ABORT button
        if caget(pv.ioc12_gp8) == 0:
            print '\tZebra ARMED' 
            caput(pv.zebra1_pc_arm, 1) 
            sleep(gate_start)
	else:
	    print 50*'ABORTED '
	    caput(pv.pilat_acquire, 0)
	    break

        if caget(pv.ioc12_gp8) == 0:
            print '\t\tFast Shutter Opening'
            caput(pv.zebra1_soft_in_b1, 1)
            
	    i = 0
            text_list = ['|', '/', '-', '\\']
	    while True:
		line_of_text = '\r\t\t\t Waiting   ' + 30*('%s' %text_list[i%4])
		flush_print(line_of_text)
		sleep(0.5)
                i += 1
		if caget(pv.ioc12_gp8) != 0:
		    print 50*'ABORTED '
	            caput(pv.pilat_acquire, 0)
		    break
                if caget(pv.zebra1_pc_arm_out) != 1:
                    print ' ----> Zebra Disarmed <----- '
		    break
	else:
	    break
	break

    caput(pv.ioc12_gp8, 1)
    print '\n\t\tFast Shutter Closing'
    caput(pv.zebra1_soft_in_b1, 0)
    print '\tZebra DISARMED' 
    caput(pv.zebra1_pc_disarm, 1) 
    print 'Pilatus Acquire STOP'  
    caput(pv.pilat_acquire, 0)
    sleep(0.5)

    ######### Clean Up
    #print 'Setting zebra back to normal'
    sup.zebra1('return-to-normal')
    sup.pilatus('return-to-normal')
    print 'End of Run in quickshot.py'
    return 1
    
if __name__ == '__main__':
    run(control_fid = sys.argv[1])
