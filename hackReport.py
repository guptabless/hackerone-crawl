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
        if (sys.argv[1] != 'l'):
            try:
                input_length = sys.argv[2]
                parser = argparse.ArgumentParser()
                parser.add_argument("-l", required=True)
                print(bcolors.BITALIC + "Testing for HackerOne Reports")
                int_input_length = int(input_length)
                report = 0
                base_url = 'https://hackerone.com/reports/1'
                for report in range(int_input_length):
                    report_url = base_url + str(report)
                    report_url_status = requests.get(report_url, allow_redirects=False).status_code
                    print(report_url,report_url_status)
                    print("********************************************************************")
                    if (report_url_status == 200):
                        print(bcolors.OKMSG + 'Report exists, you can check Report ')
                    elif (report_url_status == 302):
                        print(bcolors.OKMSG + 'Report exists but you have to login first')
                    elif (report_url_status == 404):
                        print(bcolors.ERRMSG + 'Report does not exist')
            except:
                print(bcolors.OKMSG + 'Please enter python hackReport.py -l < Quantity of reports you want to check> ')
        elif (sys.argv[1] == '-h'):
            print(bcolors.BOLD + 'usage: hackReport.py [-h] -l LENGTH' '\n' 'OPTIONS:' '\n' '-h,--help    '
                                 'show this help message and exit' '\n''-h LENGTH,   --length LENGTH How many reports you want to check')
        elif (sys.argv[1] != '-u'):
            print(bcolors.OKMSG + 'Please enter -l < How many reports you want to search>')
else:
        banner()
        print(bcolors.ERR + 'Please select at-least 1 option from -l or -h')
