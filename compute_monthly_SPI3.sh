#/bin/bash
echo Cancelling all netcdf files in this and tmp/ directories!

rm *.nc tmp/*.nc

indir=SPI3
outdir=SPI3/month
mkdir -p $outdir

cdo cat $indir/*.nc tmp/tmp.nc

template_grid=ecmwf-51/prec/monthly-means/08/ecmwf-51_08.nc
cdo -O remapcon,$template_grid tmp/tmp.nc tmp/tmp2.nc

cdo -O splitmon tmp/tmp2.nc $outdir/spi3_


