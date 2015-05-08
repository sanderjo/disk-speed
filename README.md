# disk-speed
Measure disk speed from Python. Disk can be SSD, HDD, MMC, flash drive, NAS, Cloud, as long as it is mounted.

The measurement will take 0.5 second.

# Purpose

Loosely measure the speed of a 'disk', in order to realize the speed difference between a SSD and a Cloud mount.

# Usage:

Without parameter:

```
$ ./disk-speed.py 
Absolute path of filename  /home/sander/disk-speed/outputTESTING.txt
Disk writing speed: 154.509901638 Mbytes per second
```
FWIW: this is a SSD.


With a parameter specifying the directory to be tested:
```
$ ./disk-speed.py /home/sander/
Absolute path of filename  /home/sander/outputTESTING.txt
Disk writing speed: 143.504647188 Mbytes per second
```

With a different directory specified, in this case a mount on a remote server
```
$ ./disk-speed.py '/run/user/1000/gvfs/sftp:host=server.example.com,port=2222/home/sander/'
Absolute path of filename  /run/user/1000/gvfs/sftp:host=server.example.com,port=2222/home/sander/outputTESTING.txt
Disk writing speed: 0.569606459526 Mbytes per second
```
Note the difference in speed.

# Accuracy

Speed measured this speed is not too far away from the Real Stuff with hdparm:
```
$ sudo hdparm -tT /dev/sda6 | tail -1
 Timing buffered disk reads: 618 MB in  3.00 seconds = 205.86 MB/sec
```

 


