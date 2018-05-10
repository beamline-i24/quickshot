import pv, sys
import quickshot as qs
from ca import caget, caput

def initiate():
    print 'Initiate GenPV'
    energy = caget(pv.dcm_energy)
    det_dist = caget(pv.det_z)
    caput(pv.ioc12_gp1,  '/dls/i24/data/2018/cm19649-2')
    caput(pv.ioc12_gp2,  'quickshot')
    caput(pv.ioc12_gp3,  'shot1')
    caput(pv.ioc12_gp4,  '100')
    caput(pv.ioc12_gp5,  '0.01')
    caput(pv.ioc12_gp6,  str(energy))
    caput(pv.ioc12_gp7,  str(det_dist))
    caput(pv.ioc12_gp8,  0)
    caput(pv.ioc12_gp9,  '-')
    caput(pv.ioc12_gp10, '-')
    caput(pv.ioc12_gp11, '-')
    caput(pv.ioc12_gp12, '-')
    caput(pv.ioc12_gp13, 'control.inp')
    caput(pv.ioc12_gp14, '-')
    caput(pv.ioc12_gp15, 'initiate test complete')

def add_write(control_fid):
    print 'add/write'
    directory =   caget(pv.ioc12_gp1)
    subdir =      caget(pv.ioc12_gp2)
    filename =    caget(pv.ioc12_gp3)
    num_imgs =    caget(pv.ioc12_gp4)
    exp_time =    caget(pv.ioc12_gp5)
    energy =      caget(pv.ioc12_gp6)
    det_dist =    caget(pv.ioc12_gp7)
    g = open(control_fid, 'w')
    line1  = 'directory    (txt): %s\n' % directory 
    line2  = 'subdir       (txt): %s\n' % subdir 
    line3  = 'filename     (fid): %s\n' % filename
    line4  = 'num_imgs       (#): %s\n' % num_imgs 
    line5  = 'exp_time     (sec): %s\n' % exp_time
    line6  = 'energy        (eV): %s\n' % energy
    line7  = 'det_dist      (mm): %s\n' % det_dist
    g.write(line1)
    g.write(line2)
    g.write(line3)
    g.write(line4)
    g.write(line5)
    g.write(line6)
    g.write(line7)
    g.close()
    print open(control_fid, 'r').read()

def main(arg):
    if 'initiate' in arg:
        initiate()
    elif 'run' in arg:
        control_fid = caget(pv.ioc12_gp13)
        print control_fid
        add_write(control_fid)
        print 'Running quickshot.py', control_fid
        token = qs.run(control_fid)
    else:
        print 'Unknown arg'
    
if __name__ == '__main__':
    main(sys.argv[1])
