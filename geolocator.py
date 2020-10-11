#Made by FoxSinOfGreed1729 
#Many thanks to TJ O'Connor
from ip2geotools.databases.noncommercial import DbIpCity
import optparse
import socket


usage = "usage: python3 geolocator [options] argument | use -h for help | only use one of -I and -H"
parser=optparse.OptionParser(usage=usage)
parser.add_option('-I', dest='ipadr', type='string', help='Specify IP')
parser.add_option('-H', dest='hostname', type='string', help='Specify Hostname')
(options, args)=parser.parse_args()
ipadr=options.ipadr
hostname=options.hostname
if ipadr==None :
    ipadr=socket.gethostbyname(hostname)

response=DbIpCity.get(ipadr, api_key='free')
print('Ip Address ', response.ip_address)
print('Region ', response.region)
print('Country ', response.country)
print('City ', response.city)
print('Latitude ', response.latitude)
print('Longitude ', response.longitude)
