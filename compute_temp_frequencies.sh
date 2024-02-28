#/bin/bash
echo Cancelling all netcdf files in this and tmp/ directories!

imi=12

#for m in ecmwf ukmo meteo_france dwd cmcc ncep eccc; do
#for m in ukmo meteo_france dwd cmcc ncep eccc; do
#for m in ecmwf; do
#for m in ukmo; do
#for m in meteo_france; do
#for m in dwd; do
#for m in cmcc; do
#for m in ncep; do
#for m in eccc; do
for m in era; do

for imi in {1..12}; do

ini=$(printf "%02d" $imi)

  rm *.nc tmp/*.nc

  if [ $m == "ecmwf" ]; then
    v=51
  elif [ $m == "ukmo" ]; then
    v=601
  elif [ $m == "meteo_france" ]; then
    v=8
  elif [ $m == "dwd" ]; then
    v=21
  elif [ $m == "cmcc" ]; then
    v=35
  elif [ $m == "ncep" ]; then
    v=2
  elif [ $m == "jma" ]; then
    v=2
  elif [ $m == "eccc" ]; then
    v=3
  elif [ $m == "era" ]; then
    v=5
  fi

  indir=${m}-${v}/temp/monthly-means/${ini}

  cp $indir/${m}-${v}_${ini}.nc tmp.nc

  indir2=${m}-${v}/temp/monthly-percentiles/${ini}
  cp $indir2/${m}-${v}_${ini}.nc tmpp.nc
  #./freqt_ecmwf.py
  #./fre3t.py
  ./fre4t.py

  outdir=${m}-${v}/temp/monthly-frequencies/${ini}
  mkdir -p $outdir
  mv -f tmp2.nc ${outdir}/${m}-${v}_${ini}.nc

done
done
