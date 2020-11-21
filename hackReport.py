import requests
import bcolors
import sys, argparse
from bs4 import BeautifulSoup
import csv


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
    if ((sys.argv[1] != 'l') | (sys.argv[1] != '-s') | (sys.argv[1] != '-c')):
        try:
            input_start = sys.argv[2]
            input_length = sys.argv[4]
            input_loc = sys.argv[6]
            parser = argparse.ArgumentParser()
            parser.add_argument("-s", required=True)
            parser.add_argument("-l", required=True)
            parser.add_argument("-c", required=True)
            print(bcolors.BITALIC + "Testing for HackerOne Reports")

            with open(input_loc, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["URL_Found", "Title"])
                writer.writerow('')

            int_input_length = int(input_length)

            base_url = 'https://hackerone.com/reports/'

            for report in range(int_input_length):
                rep = int(input_start) + report
                report_url = base_url + str(rep)

                report_url_status = requests.get(report_url, allow_redirects=False).status_code

                if (report_url_status == 200):
                    print(report_url)
                    print(bcolors.OKMSG + 'Report exists, you can check Report ')
                    # print(bcolors.OKMSG + 'Report Name and URL saved in the given location, you can check csv file')
                    co = requests.get(report_url)
                    soup = BeautifulSoup(co.text, 'html.parser')
                    try:
                        title = soup.find('meta', property='og:title')
                        print(title['content'])
                        print('****************************************************************************')
                    except:
                        print(bcolors.ERRMSG + ' not found')

                    with open(input_loc, 'a') as file:
                        writer = csv.writer(file, escapechar='/', lineterminator='\n')
                        try:
                            writer.writerow([report_url, title['content']])
                            writer.writerows('')
                        finally:
                            file.close()

        except:
            print(
                bcolors.OKMSG + 'Please enter python hackReport.py -s <start location > -l < Quantity of reports you want to check> -c <CSV file location> ')
    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(
            bcolors.BOLD + 'usage: hackReport.py [-h] -s  Start Location Of report' '\n' '-l LENGTH' '\n' '-c CSV file location' '\n' 'OPTIONS:' '\n' '-h,--help    '
                           'show this help message and exit' '\n''-h LENGTH,   --length LENGTH How many reports you want to check' '\n' '-c CSV,   --csv Where you want to save existing report information')
    elif ((sys.argv[1] != '-l') | (sys.argv[1] != '-s') | (sys.argv[1] != '-c')):
        print(
            bcolors.OKMSG + 'Please enter -s < start location > -l < How many reports you want to search> -c <location of csv file where you want to save exisitng report information>')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from (-l,-s,-c) or -h')
