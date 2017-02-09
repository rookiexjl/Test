# coding:utf-8
import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    region = rec['region_code']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*]Target:' + tgt + 'Geo-located.'
    print '[+]' + str(city) + ','+str(region) + ',' + str(country)
    print '[+]Latitude:'  + str(lat) + ',Longitude:' + str(long)

tgt ='58.240.57.33'
printRecord(tgt)
    
