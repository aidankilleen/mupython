# netcdfhw.py


import netCDF4 as nc


fn = "./data/sresa1b_ncar_ccsm3-example.nc"

ds = nc.Dataset(fn)


print(ds['prcp'])
