#!/usr/bin/env python3
import netCDF4 as nc
import numpy as np
from datetime import datetime
today = datetime.today()

dp = nc.Dataset('tmpp.nc')
p16=np.array(dp['p16'])
p33=np.array(dp['p33'])
p66=np.array(dp['p66'])
p84=np.array(dp['p84'])
p90=np.array(dp['p90'])

ds = nc.Dataset('tmp.nc')

tprate=ds['t2m']

lons = np.array(ds['longitude'])
lats = np.array(ds['latitude'])
time1 = ds['time']
times = np.array(time1)
print(times)

tprate2=np.array(tprate)

shp = tprate2.shape

nt = shp[0]
ne = shp[1]
ny = shp[2]
nx = shp[3]

f16=np.sum(tprate2<p16,1)/ne
f33=np.sum(tprate2<p33,1)/ne
f66=np.sum(tprate2>p66,1)/ne
f84=np.sum(tprate2>p84,1)/ne
f90=np.sum(tprate2>p90,1)/ne

print(f33.mean(0))

f = nc.Dataset('tmp2.nc','w', format='NETCDF4')
f.createDimension('longitude', len(lons))
f.createDimension('latitude', len(lats))
f.createDimension('time', len(times))
longitude = f.createVariable('longitude', 'f4', 'longitude')
latitude = f.createVariable('latitude', 'f4', 'latitude')  
time = f.createVariable('time', 'i4', 'time')  
freq33 = f.createVariable('f33', 'f4', ('time', 'latitude', 'longitude'))
freq66 = f.createVariable('f66', 'f4', ('time', 'latitude', 'longitude'))
freq16 = f.createVariable('f16', 'f4', ('time', 'latitude', 'longitude'))
freq84 = f.createVariable('f84', 'f4', ('time', 'latitude', 'longitude'))
freq90 = f.createVariable('f90', 'f4', ('time', 'latitude', 'longitude'))
longitude[:] = lons
latitude[:] = lats
time[:] = times
freq33[:,:,:] = f33
freq66[:,:,:] = f66
freq16[:,:,:] = f16
freq84[:,:,:] = f84
freq90[:,:,:] = f90

#Add global attributes
f.description = "1993-2016 hindcasts percentiles exceeding time-series"
f.history = "created " + today.strftime("%d/%m/%y")
f.Conventions = 'CF-1.6'

# add attributes to dimension varables
longitude.units = ds['longitude'].units
longitude.long_name = ds['longitude'].long_name
#longitude.axis = 'x'

latitude.units = ds['latitude'].units
latitude.long_name = ds['latitude'].long_name
#latitude.axis = 'y'

time.units = time1.units

f.close()

