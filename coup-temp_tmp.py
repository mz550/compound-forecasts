#!/usr/bin/env python3
import netCDF4 as nc
import numpy as np
from datetime import datetime
today = datetime.today()

import matplotlib.pyplot as plt

ds = nc.Dataset('tmp.nc')
c16=np.array(ds['c16'])
c33=np.array(ds['c33'])
c66=np.array(ds['c66'])
c84=np.array(ds['c84'])
c90=np.array(ds['c90'])
f16=np.array(ds['f16'])
f33=np.array(ds['f33'])
f66=np.array(ds['f66'])
f84=np.array(ds['f84'])
f90=np.array(ds['f90'])
mask=np.array(ds['msk'])
spim1=np.array(ds['spim1'])

lons = np.array(ds['longitude'])
lats = np.array(ds['latitude'])
time1 = ds['time']
times = np.array(time1)
print(times)

shp = c16.shape
print(shp)

nt = shp[0]
ny = shp[1]
nx = shp[2]

ntd2=int(nt/2)

a161=np.mean(c16[:,:,:],0)
a331=np.mean(c33[:,:,:],0)
a661=np.mean(c66[:,:,:],0)
a841=np.mean(c84[:,:,:],0)
a901=np.mean(c90[:,:,:],0)
dry1=np.mean(spim1[:,:,:],0)
#b161=np.multiply(np.mean(f66[:,:,:],0),dry1)
#b331=np.multiply(np.mean(f33[:,:,:],0),dry1)
#b661=np.multiply(np.mean(f66[:,:,:],0),dry1)
#b841=np.multiply(np.mean(f84[:,:,:],0),dry1)
b161=np.mean(f16[:,:,:],0)
b331=np.mean(f33[:,:,:],0)
b661=np.mean(f66[:,:,:],0)
b841=np.mean(f84[:,:,:],0)
b901=np.mean(f90[:,:,:],0)
#r161=np.divide(a161,b161)
#r331=np.divide(a331,b331)
#r661=np.divide(a661,b661)
#r841=np.divide(a841,b841)
r161=a161-(b161*dry1)
r331=a331-(b331*dry1)
r661=a661-(b661*dry1)
r841=a841-(b841*dry1)
r901=a901-(b901*dry1)

f = nc.Dataset('tmp2.nc','w', format='NETCDF4')
f.createDimension('longitude', len(lons))
f.createDimension('latitude', len(lats))
f.createDimension('time', len(times))
longitude = f.createVariable('longitude', 'f4', 'longitude')
latitude = f.createVariable('latitude', 'f4', 'latitude')
time = f.createVariable('time', 'i4', 'time')
rcond33 = f.createVariable('a331', 'f4', ('latitude', 'longitude'))
rcond66 = f.createVariable('a661', 'f4', ('latitude', 'longitude'))
rcond16 = f.createVariable('a161', 'f4', ('latitude', 'longitude'))
rcond84 = f.createVariable('a841', 'f4', ('latitude', 'longitude'))
rcond90 = f.createVariable('a901', 'f4', ('latitude', 'longitude'))
rfreq16 = f.createVariable('b161', 'f4', ('latitude', 'longitude'))
rfreq33 = f.createVariable('b331', 'f4', ('latitude', 'longitude'))
rfreq66 = f.createVariable('b661', 'f4', ('latitude', 'longitude'))
rfreq84 = f.createVariable('b841', 'f4', ('latitude', 'longitude'))
rfreq90 = f.createVariable('b901', 'f4', ('latitude', 'longitude'))
xfreq16 = f.createVariable('r161', 'f4', ('latitude', 'longitude'))
xfreq33 = f.createVariable('r331', 'f4', ('latitude', 'longitude'))
xfreq66 = f.createVariable('r661', 'f4', ('latitude', 'longitude'))
xfreq84 = f.createVariable('r841', 'f4', ('latitude', 'longitude'))
xfreq90 = f.createVariable('r901', 'f4', ('latitude', 'longitude'))
mask2 = f.createVariable('msk', 'f4', ('latitude', 'longitude'))
rspim1 = f.createVariable('rspi1', 'f4', ('latitude', 'longitude'))
longitude[:] = lons
latitude[:] = lats
time[:] = times
rcond33[:,:] = a331
rcond66[:,:] = a661
rcond16[:,:] = a161
rcond84[:,:] = a841
rcond90[:,:] = a901
rfreq16[:,:] = b161
rfreq33[:,:] = b331
rfreq66[:,:] = b661
rfreq84[:,:] = b841
rfreq90[:,:] = b901
xfreq16[:,:] = r161
xfreq33[:,:] = r331
xfreq66[:,:] = r661
xfreq84[:,:] = r841
xfreq90[:,:] = r901
mask2[:,:] = mask
rspim1[:,:] = dry1

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

