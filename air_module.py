# -*- coding: utf-8 -*-

import time
import glob
import csv
from subprocess import *
from glob import *

def int_identity():
    try:
        run('mkdir temp_air_dump', shell=True)
    except FileExistsError:
        run('rm -r temp_air_dump', shell=True)
        run('mkdir temp_air_dump', shell=True)
    l = None
    with open('temp_air_dump/int', 'w') as f:
        run(['ls', '/sys/class/net'], stdout=f)
    with open('temp_air_dump/int') as f:
        sps = f.read().strip().split('\n')
    k = 1
    for i in sps:
        print('You have interface #{} {}'.format(k, i))
        k += 1
    w = input('What number is WiFi interface? #')
    wifi = sps[int(w) - 1]
    run('airmon-ng check kill', shell=True)
    time.sleep(3)
    run('airmon-ng start {}'.format(wifi), shell=True)
    '''testing area'''
    with open('temp_air_dump/int', 'w') as f:
        run(['ls', '/sys/class/net'], stdout=f)
    with open('temp_air_dump/int') as f:
        sps_w = f.read().strip().split('\n')
    for i in sps_w:
        if i not in sps:
            wifi_mon = i
    try:
        return wifi_mon
    except UnboundLocalError:
        print('\n\n interface already in monitor mode \n')
        wifi_mon = 'wlan0mon'
        return wifi_mon


def air_save():
    csv_name = glob('temp_air_dump/*01.csv')[0]
    with open(csv_name) as f:
        f_file = f.readlines()
    sps = []
    for i in f_file[2:]:
        if i != '\n':
            sps.append(i)

    for i in sps:
        if i.startswith('Station MAC'):
            idx = sps.index(i)
    '''kj - только данные  AP'''
    kj = sps[:idx]
    bssid = []
    essid = []
    channel = []
    for i in kj:
        bssid.append(i.split(',')[0].strip())
        essid.append(i.split(',')[13].strip())
        channel.append(i.split(',')[3].strip())
    london = dict(zip(essid, zip(bssid, channel)))
    try:
        k = 1
        print('\n\n\n')
        run('clear', shell=True)
        for i in london.items():
            print('# {} {:<12} {:<18} channel {}'.format(k, i[0], i[1][0], i[1][1]))
            k += 1
        nbr = input('\n\n choose # network to safe: ')
        nbr = int(nbr) - 1
        print('\n\n Alright, let it work "{}"'.format(list(london.items())[nbr][0]))
        time.sleep(3)
    except IndexError:
        print('\n\n\n\n\n Choose in range from -{} to {}'.format(len(london.items()), len(london.items())))
    except ValueError:
        print("you did't pick AP")
    bssid_save = list(london.items())[nbr][1][0]
    return bssid_save, london, csv_name

def air_bssid(sps):
    data = []
    for i in sps[1:]:
        if 'Station MAC' not in i:
            data.append(i[0])
        else:
            return data

def air_scan1(i, l):
    i = str(i)
    run('rm -r temp_air_dump/air*', shell=True)
    run('airodump-ng -c {} {} -w temp_air_dump/air_dump & sleep 3 ; kill $!'.format(i, l), shell=True)
    print('\n\n\n Channel {}'.format(i))

def air_sps():
    sps = []
    with open(glob('temp_air_dump/*01.csv')[0]) as f:
        rd = csv.reader(f)
        for r in rd:
            if r != []:
                sps.append(r)
    return sps

info = '''
Country/Continent Permitted channels

North America 1 to 11
South America 1 to 11
Europe 1 to 13
Asia/Pacific (except Japan, Taiwan) 1 to 13
Japan 1 to 14
Taiwan 1 to 14
'''

pics = """
       +@@@@      @@@@@     ;@@@@      @@@@    @@@@@ +@@@@@@@@@@@
        @@@@      +@@@       @@@       `@@     @@@#   @@@@@@@@@@@
        @@@@      @@@@      :@@@@      `@@    @@@:    @@#       :
        @@@@@    #@@@@      @@@@@      `@@   @@@`     @@#
        @@;@@    @@'@@     `@@ @@#     `@@ `@@@       @@#
        @@`@@@  #@@;@@     @@# #@@     `@@:@@@        @@@@@@@@`
        @@`:@@  @@ ;@@     @@   @@+    `@@@@@@@       @@@@@@@@`
        @@` @@@#@@ ;@@    @@@   @@@    `@@@++@@+      @@#     `
        @@` :@@@@  ;@@    @@@@@@@@@:   `@@.  @@@.     @@#
        @@`  @@@#  ;@@   #@@@@@@@@@@   `@@    @@@     @@#
        @@`  :@@   ;@@   @@,     :@@:  `@@    `@@@    @@#
        @@`   @+   ;@@  ;@@       @@@  `@@     ;@@@   @@@@@@@@@@@
       `@@+   :    @@@` @@@       @@@+ '@@:     @@@# `@@@@@@@@@@@


      :@@+`                             @
    @@@@@@@@:    @@+         `@@@@@@@@@@@      @@@;      `@@@      `@@
   @@@@. .@@@@+  @@+         `@@@@@@@@@@@      @@@@      `@@@'     `@@
  @@@       @@   @@+         `@@              .@@@@`     `@@@@:    `@@
 ,@@.        `   @@+         `@@              @@+@@@     `@@@@@.   `@@
 @@@             @@+         `@@     :       `@@ :@@     `@@ @@@`  `@@
 @@@             @@+         `@@@@@@@@       @@@  @@@    `@@  @@@  `@@
 @@@             @@+         `@@@@@@@@       @@   #@@    `@@  `@@@ `@@
 @@@             @@+         `@@            @@@@@@@@@@   `@@   .@@@`@@
 ,@@.            @@+         `@@            @@@@@@@@@@   `@@    :@@@@@
  @@@       @@   @@+         `@@           #@@      @@#  `@@     +@@@@
   @@@@. .@@@@:  @@@@@@@@@@@ `@@@@@@@@@@@  @@:      @@@  `@@      #@@@
    @@@@@@@@'    @@@@@@@@@@@ `@@@@@@@@@@@ ;@@       :@@# `@@       @@@
      :@@#.                +            +

"""
war = """
    #@@@     @@@@:    ;@@@     .@@@:        @@@@@@@@@@@@
     @@@     @@@@+    #@@;     ;@@@#        @@@@@@@@@@@@@
     @@@`   :@@@@@    @@@      @@@@@        @@@       @@@
     `@@@   @@@@@@`  .@@@     ;@@#@@#       @@@       @@@
      @@@   @@@;@@@  @@@      @@@ @@@       @@@       @@@
      +@@' @@@. @@@  @@@     ;@@` #@@@      @@@@@@@@@@@@@
       @@@ @@@  @@@;;@@;     @@@   @@@      @@@@@@@@@@@@
       @@@:@@+  `@@@@@@     ;@@`   +@@@     @@@   @@@@
       .@@@@@    @@@@@@     @@@@@@@@@@@`    @@@    @@@:
        @@@@@    +@@@@`    ;@@@@@@@@@@@@    @@@    `@@@
        #@@@`     @@@@     @@@       @@@.   @@@     #@@@
         @@@      @@@@    ;@@;       +@@@   @@@      @@@@
        @@@@@    #@@@@:  #@@@@       @@@@@ @@@@@    :@@@@@
"""

ins = """
                    @@@,   @@@@       #@@`
                    @@@`   @@@@@      +@@
                    @@@`   @@@@@@     +@@
                    @@@`   @@@@@@@    +@@
                    @@@`   @@@:@@@@   +@@
                    @@@`   @@@ :@@@@  +@@
                    @@@`   @@@  :@@@@ +@@
                    @@@`   @@@   .@@@@+@@
                    @@@`   @@@    .@@@@@@
                    @@@`   @@@     .@@@@@
                    @@@`   @@@      .@@@@
                    @@@`   @@@       .@@@
                   ;@@@@  :@@@@      @@@@@
"""
air = """
                 @@@@        :@@@   :@@@@@@@@@@@+
                 @@@@        :@@@   .@@@@@@@@@@@@;
                `@@@@@       :@@@   .@@@      ;@@@
                @@@@@@`      :@@@   .@@@       @@@
               `@@::@@@      :@@@   .@@@      +@@@
               @@@  @@@.     :@@@   .@@@@@@@@@@@@:
              `@@:  .@@@     :@@@   .@@@@@@@@@@@:
              @@@    @@@:    :@@@   .@@@   @@@.
             `@@@@@@@@@@@    :@@@   .@@@   ,@@@
             @@@@@@@@@@@@;   :@@@   .@@@    #@@@
            `@@+      `@@@   :@@@   .@@@     @@@#
            @@@        @@@#  :@@@   .@@@      @@@:
           @@@@@      @@@@@@ @@@@:  @@@@:    @@@@@@

"""
wing = """

                   `````````      `````````
                             '''`
                            '''''`
                      '    .''''''    ;
                     ''',  ,''''''   ''',
                   ,''''''  '''''; ,''''''
                  ''''''''  :''''  ,'''''''
                 '''''''',    `     ''''''''
                  ,''''''           '''''''
                    '''''     '`    ,'''',
                     ''':   .''';    '''
                      .'   ;''''''   ';
                          ''''''''',
                         ;''''''''''
                           ''''''':
                            '''''
                             ,''
"""

def wia(y, sks):
    for i in sks:
        j = len(sks) - 1
        if sks.index(i) != j:
            print(i, flush=True)
            time.sleep(y)
        else:
            run('clear', shell=True)
            print(sks[j])

