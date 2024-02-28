#!/usr/bin/env python3
import cdsapi
import os

c = cdsapi.Client()

#models = [ 'ecmwf', 'ukmo', 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma' ]
#systems = [ '5', '600', '7', '21', '3', '2', '2' ]

#models = [ 'meteo_france', 'dwd', 'cmcc', 'ncep', 'jma' ]
#systems = [ '7', '21', '35', '2', '2' ]

models = [ 'meteo_france', 'dwd', 'cmcc', 'ncep' ]
systems = [ '7', '21', '35', '2' ]

models = [ 'ecmwf' ]
systems = [ '51' ]

models = [ 'ukmo' ]
systems = [ '601' ]

models = [ 'meteo_france' ]
systems = [ '8' ]

models = [ 'dwd' ]
systems = [ '21' ]

models = [ 'cmcc' ]
systems = [ '35' ]

models = [ 'ncep' ]
systems = [ '2' ]

models = [ 'eccc' ]
systems = [ '3' ]

for m in range(0,12):

    month=str(m+1).zfill(2)

    for model,system in zip(models,systems):

        print(model,system)

        outdir = model+'-'+system+'/temp/monthly-means/'+month

        os.system( 'mkdir -p ' + outdir )

        c.retrieve(
            'seasonal-monthly-single-levels',
            {
                'originating_centre': model,
                'system': system,
                'variable': '2m_temperature',
                'product_type': 'monthly_mean',
                'year': [
                    '1993', '1994', '1995',
                    '1996', '1997', '1998',
                    '1999', '2000', '2001',
                    '2002', '2003', '2004',
                    '2005', '2006', '2007',
                    '2008', '2009', '2010',
                    '2011', '2012', '2013',
                    '2014', '2015', '2016',
                ],
                'month': month,
                'leadtime_month': [
                    '1', 
                ],
                'format': 'netcdf',
            },
            outdir + '/' + model + '-' + system + '_' + month + '.nc')
