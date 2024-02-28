#!/usr/bin/env python3
import cdsapi
import os

c = cdsapi.Client()

models = [ 'ERA' ]
systems = [ '5' ]

#for m in range(1,2):
for m in range(12):

    month=str(m+1).zfill(2)

    for model,system in zip(models,systems):

        print(model,system)

        outdir = model+'-'+system+'/temp/monthly-means/'+month

        os.system( 'mkdir -p ' + outdir )

        c.retrieve(
            'reanalysis-era5-single-levels-monthly-means',
            {
                'variable': '2m_temperature',
                'product_type': 'monthly_averaged_ensemble_members',
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
                'time': [
                    '00:00', 
                ],
                'format': 'netcdf',
            },
            outdir + '/' + model + '-' + system + '_' + month + '.nc')
