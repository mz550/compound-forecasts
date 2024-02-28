#!/usr/bin/env python3
import netCDF4 as nc
import numpy as np
from datetime import datetime
today = datetime.today()

ds = nc.Dataset('tmp.nc')

tprate=ds['t2m']

lon = np.array(ds['longitude'])
lat = np.array(ds['latitude'])

tprate2=np.array(tprate)

shp = tprate2.shape

nh = shp[0]
ne = shp[1]
ny = shp[2]
nx = shp[3]

print(tprate2.shape)
tprate3=tprate2[:,:,:,:].reshape(1,ne*nh,ny,nx).squeeze()
print(tprate3.shape)

mea=np.mean(tprate3,0)
p50=np.percentile(tprate3,50,0)
p33=np.percentile(tprate3,33.3,0)
p66=np.percentile(tprate3,66.6,0)
p16=np.percentile(tprate3,15.9,0)
p84=np.percentile(tprate3,84.1,0)
p90=np.percentile(tprate3,90,0)
print(p84.shape)

f = nc.Dataset('tmp2.nc','w', format='NETCDF4')
f.createDimension('longitude', len(lon))
f.createDimension('latitude', len(lat))
longitude = f.createVariable('longitude', 'f4', 'longitude')
latitude = f.createVariable('latitude', 'f4', 'latitude')  
mean = f.createVariable('mea', 'f4', ('latitude', 'longitude'))
median = f.createVariable('p50', 'f4', ('latitude', 'longitude'))
perc33 = f.createVariable('p33', 'f4', ('latitude', 'longitude'))
perc66 = f.createVariable('p66', 'f4', ('latitude', 'longitude'))
perc16 = f.createVariable('p16', 'f4', ('latitude', 'longitude'))
perc84 = f.createVariable('p84', 'f4', ('latitude', 'longitude'))
perc90 = f.createVariable('p90', 'f4', ('latitude', 'longitude'))
longitude[:] = lon 
latitude[:] = lat
mean[:,:] = mea
median[:,:] = p50
perc33[:,:] = p33
perc66[:,:] = p66
perc16[:,:] = p16
perc84[:,:] = p84
perc90[:,:] = p90

#Add global attributes
f.description = "1993-2016 hindcasts precipitation percentiles"
f.history = "created " + today.strftime("%d/%m/%y")
f.Conventions = 'CF-1.6'

# add attributes to dimension varables
longitude.units = ds['longitude'].units
longitude.long_name = ds['longitude'].long_name
#longitude.axis = 'x'

latitude.units = ds['latitude'].units
latitude.long_name = ds['latitude'].long_name
#latitude.axis = 'y'

f.close()
