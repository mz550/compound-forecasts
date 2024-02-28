#!/usr/bin/env python3
import netCDF4 as nc
import numpy as np
from datetime import datetime
today = datetime.today()

dp = nc.Dataset('tmpp.nc')
spi=np.array(dp['spg03'])

ds = nc.Dataset('tmp.nc')
f16=np.array(ds['f16'])
f33=np.array(ds['f33'])
f66=np.array(ds['f66'])
f84=np.array(ds['f84'])
f90=np.array(ds['f90'])

lons = np.array(ds['longitude'])
lats = np.array(ds['latitude'])
time1 = ds['time']
times = np.array(time1)
print(times)

shp = spi.shape
print(shp)

nt = shp[0]
ny = shp[1]
nx = shp[2]

msk=(spi>-10).astype(int)
c16=np.multiply((f16>0.32).astype(int),(spi<-1).astype(int))
c33=np.multiply((f33>0.66).astype(int),(spi<-1).astype(int))
c66=np.multiply((f66>0.66).astype(int),(spi<-1).astype(int))
c84=np.multiply((f84>0.32).astype(int),(spi<-1).astype(int))
c90=np.multiply((f90>0.20).astype(int),(spi<-1.28).astype(int))
c90x=np.multiply((f90>0.50).astype(int),(spi<-1.28).astype(int))
sp1=(spi<-1).astype(int)
sp1p3=(spi<-1.28).astype(int)
g16=np.multiply((f16>0.32).astype(int),msk)
g33=np.multiply((f33>0.66).astype(int),msk)
g66=np.multiply((f66>0.66).astype(int),msk)
g84=np.multiply((f84>0.32).astype(int),msk)
g90=np.multiply((f90>0.20).astype(int),msk)
g90x=np.multiply((f90>0.50).astype(int),msk)

print(c16)

f = nc.Dataset('tmp2.nc','w', format='NETCDF4')
f.createDimension('longitude', len(lons))
f.createDimension('latitude', len(lats))
f.createDimension('time', len(times))
longitude = f.createVariable('longitude', 'f4', 'longitude')
latitude = f.createVariable('latitude', 'f4', 'latitude')  
time = f.createVariable('time', 'i4', 'time')  
cond33 = f.createVariable('c33', 'f4', ('time', 'latitude', 'longitude'))
cond66 = f.createVariable('c66', 'f4', ('time', 'latitude', 'longitude'))
cond16 = f.createVariable('c16', 'f4', ('time', 'latitude', 'longitude'))
cond84 = f.createVariable('c84', 'f4', ('time', 'latitude', 'longitude'))
cond90 = f.createVariable('c90', 'f4', ('time', 'latitude', 'longitude'))
cond90x= f.createVariable('c90x', 'f4', ('time', 'latitude', 'longitude'))
freq16 = f.createVariable('f16', 'f4', ('time', 'latitude', 'longitude'))
freq33 = f.createVariable('f33', 'f4', ('time', 'latitude', 'longitude'))
freq66 = f.createVariable('f66', 'f4', ('time', 'latitude', 'longitude'))
freq84 = f.createVariable('f84', 'f4', ('time', 'latitude', 'longitude'))
freq90 = f.createVariable('f90', 'f4', ('time', 'latitude', 'longitude'))
freq90x= f.createVariable('f90x', 'f4', ('time', 'latitude', 'longitude'))
mask = f.createVariable('msk', 'f4', ('latitude', 'longitude'))
spim1 = f.createVariable('spim1', 'f4', ('time','latitude', 'longitude'))
spim1p3 = f.createVariable('spim1p3', 'f4', ('time','latitude', 'longitude'))
longitude[:] = lons
latitude[:] = lats
time[:] = times
cond33[:,:,:] = c33
cond66[:,:,:] = c66
cond16[:,:,:] = c16
cond84[:,:,:] = c84
cond90[:,:,:] = c90
cond90x[:,:,:] = c90x
freq16[:,:,:] = g16
freq33[:,:,:] = g33
freq66[:,:,:] = g66
freq84[:,:,:] = g84
freq90[:,:,:] = g90
freq90x[:,:,:] = g90x
mask[:,:] = msk[0,:,:]
spim1[:,:,:] = sp1[:,:,:]
spim1p3[:,:,:] = sp1p3[:,:,:]

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

