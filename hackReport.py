import requests
import bcolors
import sys, argparse

def banner():
    print("""
           ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░░█████╗░███╗░░██╗███████╗░░░░░░██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
           ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
           ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝██║░░██║██╔██╗██║█████╗░░█████╗██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
           ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗██║░░██║██║╚████║██╔══╝░░╚════╝██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
           ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║╚█████╔╝██║░╚███║███████╗░░░░░░██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
           ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░                                                                                       
                                                                                                                               Code By: NG
              """
          )
if len(sys.argv) > 1:
        banner()
        if ((sys.argv[1] != 'l') | (sys.argv[1] == '-s')):
            try:
                input_start = sys.argv[2]
                input_length = sys.argv[4]
                parser = argparse.ArgumentParser()
                parser.add_argument("-s", required=True)
                parser.add_argument("-l", required=True)
                print(bcolors.BITALIC + "Testing for HackerOne Reports")
                int_input_length = int(input_length)

                base_url = 'https://hackerone.com/reports/'

                for report in range(int_input_length):
                    rep = int(input_start) + report
                    report_url = base_url + str(rep)

                    report_url_status = requests.get(report_url, allow_redirects=False).status_code
                    if (report_url_status == 200):
                        print(report_url)
                        print(bcolors.OKMSG + 'Report exists, you can check Report ')
            except:
                print(bcolors.OKMSG + 'Please enter python hackReport.py -s <start location > -l < Quantity of reports you want to check> ')
        elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
            print(bcolors.BOLD + 'usage: hackReport.py [-h] -s  Start Location Of report' '\n' '-l LENGTH' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-h LENGTH,   --length LENGTH How many reports you want to check')
        elif ((sys.argv[1] != '-l') | (sys.argv[1] != '-s')):
            print(bcolors.OKMSG + 'Please enter -s < start location > -l < How many reports you want to search>')
else:
        banner()
        print(bcolors.ERR + 'Please select at-least 1 option from (-l,-s) or -h')



