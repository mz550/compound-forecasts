#/bin/bash
echo Cancelling all netcdf files in this and tmp/ directories!

imi=12

for m in ecmwf ukmo meteo_france dwd cmcc ncep eccc era; do
#for m in ecmwf; do
#for m in ukmo; do

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
  elif [ $m == "eccc" ]; then
    v=3
  elif [ $m == "era" ]; then
    v=5
  fi

  indir=${m}-${v}/temp/monthly-cond/${ini}

  cp $indir/${m}-${v}_${ini}.nc tmp.nc

  ./coup-temp_tmp.py
  #./coup-temp_tmp2.py

  outdir=${m}-${v}/coup-temp/
  mkdir -p $outdir
  echo $outdir
  mv -f tmp2.nc ${outdir}/${m}-${v}_${ini}.nc

done
done
