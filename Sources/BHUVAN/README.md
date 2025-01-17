# BHUVAN Disaster Services
BHUVAN Disaster Services provides inundation maps of various flood events in India. Check this [link](https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php?id=flood) to explore the data source.

![Alt text](<docs/IDS-DRR ETL BHUVAN.jpg>)

**Variables extracted from the source:**
1. `inundation_pct`: Percentage of pixels that are inundated atleast once in a revenue circle in a month
2. `intensity_mean`: Mean intensity of inundation in a revenue circle in a month. Intensity is the number of times a pixel is inundated in a month divided by the maximum number of times a pixel is inundated in the given month.
3.  `intensity_sum`: Sum intensity of inundation in a revenue circle in a month. Intensity is the number of times a pixel is inundated in a month divided by the maximum number of times a pixel is inundated in the given month.

**Time Taken to run the scripts:** 
1. `transformer.py`: 45.81272932000138 seconds

## Project Structure
- `scripts` : Contains the scripts used to obtain the data
    - `get_dates.py`: Scrapes the BHUVAN portal to get all the dates on which the flood inundation maps are available for Assam
    - `gdal_wms.py`: Downloads the compressed inundation map for chosen dates from BHUVAN WMS layer in `.tif` format
    - `remove_watermark.py`: Removed `bhuvn` watermarks from the inundation maps downloaded
    - `transformer.py`: Stitches the inundation maps and creates the required variables for a chosen month
    - `upload_to_s3.py`: Uploads the individual flood inundation maps to S3 for archival

- `data`: Contains datasets generated using the scripts.
    - `PNGs`: Contains flood inundation maps of a given day before geo-referencing.
    - `tiffs`: Contains flood inundation maps of a given day after geo-referencing. Raw, after removing water marks and also stitched maps of a given month.


