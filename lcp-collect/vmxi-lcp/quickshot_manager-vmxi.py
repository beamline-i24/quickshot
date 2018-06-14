#!/bin/usr/python
import pv-vmxi, sys
import quickshot-vmxi as qs
from ca-vmxi import caget, caput

def initiate():
    energy = caget(pv.dcm_energy)
    det_dist = caget(pv.det_z)
    print 'Initiate GenPV'
    caput(pv.ioc12_gp1,  'cm16788-4')
    caput(pv.ioc12_gp2,  'lcp-extruder/syringe-N/run-N')
    caput(pv.ioc12_gp3,  'protein-name')
    caput(pv.ioc12_gp4,  '100')
    caput(pv.ioc12_gp5,  '0.01')
    caput(pv.ioc12_gp6,  str(energy))
    caput(pv.ioc12_gp7,  str(det_dist))
    caput(pv.ioc12_gp8,  0)
    caput(pv.ioc12_gp13, 'control.inp')
    caput(pv.ioc12_gp15, 'initialization complete')
    return 1

def read_write():
    print 'Reading',
    directory   = caget(pv.ioc12_gp1)
    subdir      = caget(pv.ioc12_gp2)
    filename    = caget(pv.ioc12_gp3)
    num_imgs    = caget(pv.ioc12_gp4)
    exp_time    = caget(pv.ioc12_gp5)
    energy      = caget(pv.ioc12_gp6)
    det_dist    = caget(pv.ioc12_gp7)
    control_fid = caget(pv.ioc12_gp13)
    print 'Writing',
    g = open(control_fid, 'w')
    line1  = 'directory    (txt): /dls/i02-2/data/2017/%s\n' % directory 
    line2  = 'subdir       (txt): %s\n' % subdir 
    line3  = 'filename     (fid): %s\n' % filename
    line4  = 'num_imgs       (#): %s\n' % num_imgs 
    line5  = 'exp_time     (sec): %s\n' % exp_time
    line6  = 'energy        (eV): %s\n' % energy
    line7  = 'det_dist      (mm): %s\n' % det_dist
    line8  = 'control_fid (.inp): %s\n' % control_fid
    g.write(line1)
    g.write(line2)
    g.write(line3)
    g.write(line4)
    g.write(line5)
    g.write(line6)
    g.write(line7)
    g.write(line8)
    g.close()
    return control_fid 

def main(arg):
    if 'initiate' in arg:
        initiate()
    elif 'run' in arg:
        print '\n\n'
        print 14*'Start '
        control_fid = read_write()
        print 'Running quickshot.py'
        qs.run(control_fid)
    else:
        print 'Unknown arg'
    print 15*'Done '
    
if __name__ == '__main__':
    main(sys.argv[1])
