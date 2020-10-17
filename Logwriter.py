import platform
from datetime import datetime
from typing import TextIO

from Source.Health_check import *
from Source.network import *

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")

file: TextIO
with open("Log.log", "a") as file:
    file.write("\n\n{}".format(dt))

    uname = platform.uname()
    file.write("\nSystem : {}".format(uname.system))
    file.write("\nNode Name : {}".format(uname.node))
    file.write("\nRelease : {}".format(uname.release))
    file.write("\nVersion : {}".format(uname.version))
    file.write("\nMachine : {}".format(uname.machine))
    file.write("\nProcessor : {}".format(uname.processor))

    file.write("\nDisk Free : {} \nCPU usage(Two sec) : {} \n".format(check_disk_usage("/"), check_cpu_usage()))
    file.write("=" * 20 + " CPU Information" + "=" * 20)
    # Amount of cores
    file.write("\nPhysical Cores : {}".format(psutil.cpu_count(logical=False)))
    file.write("\nTotal Cores : {}".format(psutil.cpu_count(logical=True)))
    # Frequencies
    cpufrequency = psutil.cpu_freq()
    file.write("\nMax Frequency : {:.2f}Mhz".format(cpufrequency.max))
    file.write("\nMin Frequency : {:.2f}Mhz".format(cpufrequency.min))
    file.write("\nCurrent Frequency : {:.2f}Mhz".format(cpufrequency.current))
    # Usage
    file.write("\nCpu Usage Per Core : ")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        file.write("\nCore {} : {}%".format(i + 1, percentage))
    file.write("\nTotal CPU Usage : {}\n".format(psutil.cpu_percent()))

    if check_local() and check_connectivity():
        file.write("=" * 20 + " Network Information" + "=" * 20)
        file.write("\nNetwork analysis : Ok ")
        file.write("\n" + str(Network_details()))
    else:
        file.write("\nNetwork analysis : ERROR \n")
