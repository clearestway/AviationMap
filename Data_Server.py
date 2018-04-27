
import urllib2



def aviation_data():
    # each function gets a specific data list from the server

        url="https://www.aviationweather.gov/gis/scripts/MetarJSON.php"
        response_metar = urllib2.urlopen(url)
        metar = response_metar.read()
        data_metar = open('templates/metar_data.JSON', 'w')
        data_metar.write(metar)
        data_metar.close()






        url1='https://www.aviationweather.gov/gis/scripts/AirepJSON.php'

        response_aircraft = urllib2.urlopen(url1)

        aircraftrep = response_aircraft.read()
        data_airreport = open('templates/aircraftrep_data.JSON', 'w')
        data_airreport.write(aircraftrep)
        data_airreport.close()


        url2="https://www.aviationweather.gov/gis/scripts/SigmetJSON.php"

        response_sigmet = urllib2.urlopen(url2)
        sigmet = response_sigmet.read()
        data_sigmet = open('templates/sigmet_data.JSON', 'w')
        data_sigmet.write(sigmet)
        data_sigmet.close()

        url3 ="https://www.aviationweather.gov/gis/scripts/AirmetJSON.php"

        response_airmet = urllib2.urlopen(url3)
        airmet = response_airmet.read()
        data_airmet = open('templates/airmet_data.JSON','w')
        data_airmet.write(airmet)
        data_airmet.close()


if __name__ == '__main__':
    aviation_data()
