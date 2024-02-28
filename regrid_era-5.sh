#/bin/bash
echo Cancelling all netcdf files in this and tmp/ directories!

imi=12

for imi in {1..12}; do

ini=$(printf "%02d" $imi)

#var=prec
var=temp

m1=ERA
m2=era
v=5

rm *.nc tmp/*.nc

indir=${m1}-${v}/${var}/monthly-means/${ini}
outdir=${m2}-${v}/${var}/monthly-means/${ini}
mkdir -p $outdir

ref=ecmwf-51/${var}/monthly-means/01/ecmwf-51_01.nc

infile=$indir/${m1}-${v}_${ini}.nc
outfile=$outdir/${m2}-${v}_${ini}.nc

cdo -O remapcon,$ref $infile $outfile

#ncrename -v tp,tprate $outfile

done
