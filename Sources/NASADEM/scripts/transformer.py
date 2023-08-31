import rasterstats
import rasterio
import geopandas as gpd
import pandas as pd
import os
import glob
import numpy as np
path = os.getcwd()+'/Sources/NASADEM/'

assam_rc_gdf = gpd.read_file(os.getcwd()+'/Maps/Assam_Revenue_Circles/assam_revenue_circle_nov2022.shp')

dem_raster = rasterio.open(path+'/data/NASADEM_DEM_30.tif')
dem_raster_array = dem_raster.read(1)

mean_dicts = rasterstats.zonal_stats(assam_rc_gdf.to_crs(dem_raster.crs),
                                     dem_raster_array,
                                     affine= dem_raster.transform,
                                     stats= ['mean'],
                                     nodata=dem_raster.nodata,
                                     geojson_out = True)
dfs = []
for rc in mean_dicts:
    dfs.append(pd.DataFrame([rc['properties']]))

dem_zonal_stats_df = pd.concat(dfs).reset_index(drop=True)
dem_zonal_stats_df = dem_zonal_stats_df.rename(columns={'mean':'elevation_mean'})

dem_zonal_stats_df.to_csv(path+"data/NASADEM.csv")
# slope_raster = rasterio.open(path+'/data/NASADEM_SLOPE_30.tif')
# slope_raster_array = slope_raster.read(1)

# mean_dicts = rasterstats.zonal_stats(assam_rc_gdf.to_crs(slope_raster.crs),
#                                      slope_raster_array,
#                                      affine= slope_raster.transform,
#                                      stats= ['mean'],
#                                      nodata=slope_raster.nodata,
#                                      geojson_out = True)
# dfs = []
# for rc in mean_dicts:
#     dfs.append(pd.DataFrame([rc['properties']]))

# slope_zonal_stats_df = pd.concat(dfs).reset_index(drop=True)
# slope_zonal_stats_df = slope_zonal_stats_df.rename(columns={'mean':'slope_mean'})
