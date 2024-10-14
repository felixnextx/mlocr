import os
import tempfile
from subprocess import PIPE, Popen



def recogniseImage(img, frmt='sdf'):
    fd, fpath = tempfile.mkstemp()
    os.write(fd, img)
    os.close(fd)
    arguments = ["/usr/bin/osra"]
   
    if frmt and frmt in ('can', 'smi', 'sdf'):
        arguments.extend(['-f', frmt])
        arguments.append('-c')
    arguments.append(fpath)
    p = Popen(arguments, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result, err = p.communicate(input=img)
    os.remove(fpath)

    ret = result.decode('utf-8')
    return ret
