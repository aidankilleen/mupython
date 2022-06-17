# netcdf4_investigation.py
# By:Aidan
# Date: 17/6/2022

import netCDF4 as nc

fn = "C:\\data\\HadISST_sst.nc"

ds = nc.Dataset(fn)

print(ds)

# print(ds['sst'][0])
print (ds['sst'][1000])
row = ds['sst'][500][100:200]




for i in row:
    print(i)


print (len(row))