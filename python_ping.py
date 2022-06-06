#/usr/bin/python3
# Needs to run with Python3
# Tested on Linux (does not work on MacOS)
import subprocess

# A Python program to return multiple 
# values from a method using class
class Ping_IP_Result:
    returnValue = 1
    responseTime = 0   
#end class Ping_IP_Result

# This function returns an object of Ping_IP_Result
# Inputs:
#     ip_address: Ipv4, IPv6 or FQDN - no validation done
#     AddressFamily: -4 or -6 - no default
#
# Returns class object Ping_IP_Result
#     returnValue: Return value of ping - 0 for success, 1 for fail
#     responseTime: Ping response time in ms (float)

def ping_ip(ip_address,AddressFamily):
    reply = subprocess.run(['ping', '-c', '1', '-n',AddressFamily, ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        ping_time = float((reply.stdout[reply.stdout.find('time=') + 5:reply.stdout.find(' ms')]))
        Ping_IP_Result.responseTime = ping_time
        Ping_IP_Result.returnValue = reply.returncode
        return Ping_IP_Result()
    else:
        Ping_IP_Result.returnValue = reply.returncode
        return Ping_IP_Result()
#end def ping_ip()

# Main 
# Pruebas
hostname = "google.com" #example
ping_return = ping_ip(hostname,'-4')
#print (ping_return.returnValue)
#print (ping_return.responseTime)
if ping_return.returnValue == 0:
    print (hostname, 'is up! Response time is ',ping_return.responseTime,' ms')
else:
    print (hostname, 'is down!')

hostname = "mdeleo.com" #example
ping_return = ping_ip(hostname,'-6')
if ping_return.returnValue == 0:
    print (hostname, 'is up! Response time is ',ping_return.responseTime,' ms')
else:
    print (hostname, 'is down!')

hostname = "2001:470:6:1::120" #example
ping_return = ping_ip(hostname,'-6')
if ping_return.returnValue == 0:
    print (hostname, 'is up! Response time is ',ping_return.responseTime,' ms')
else:
    print (hostname, 'is down!')

hostname = "datashell.mx" #example
ping_return = ping_ip(hostname,'-6')
if ping_return.returnValue == 0:
    print (hostname, 'is up! Response time is ',ping_return.responseTime,' ms')
else:
    print (hostname, 'is down!')

hostname = "nonexist" #example
ping_return = ping_ip(hostname,'-6')
if ping_return.returnValue == 0:
    print (hostname, 'is up! Response time is ',ping_return.responseTime,' ms')
else:
    print (hostname, 'is down!')
