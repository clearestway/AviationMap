import threading
import urllib2


# a function to retrieve the data from aviationweather.gov


def aviation_data():
    # each function gets a specific data list from the server

        url="http://www.aviationweather.gov/adds/dataserver_current/current/metars.cache.csv"
        response_metar = urllib2.urlopen(url)
        metar = response_metar.read()
        data_metar = open('metar_data.csv', 'w')
        data_metar.write(metar)



        url1='http://www.aviationweather.gov/adds/dataserver_current/current/aircraftreports.cache.csv'

        response_aircraft = urllib2.urlopen(url1)

        aircraftrep = response_aircraft.read()
        data_airreport = open('aircraftrep_data.csv', 'w')
        data_airreport.write(aircraftrep)
        data_airreport.close()


        url2="http://www.aviationweather.gov/adds/dataserver_current/current/airsigmets.cache.csv"

        response_sigmet = urllib2.urlopen(url2)
        sigmet = response_sigmet.read()
        data_sigmet = open('sigmet_data.csv', 'w')
        data_sigmet.write(sigmet)
        data_sigmet.close()


        url3="http://www.aviationweather.gov/adds/dataserver_current/current/tafs.cache.csv"
        response_taf = urllib2.urlopen(url3)
        taf = response_taf.read()
        data_taf = open('taf_data.csv', 'w')
        data_taf.write(taf)

