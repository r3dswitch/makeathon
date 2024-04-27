from osgeo import gdal

def get_geolocation(tiff_file):
    # Open the TIFF file
    dataset = gdal.Open(tiff_file, gdal.GA_ReadOnly)
    
    if dataset is None:
        print("Error: Unable to open the TIFF file.")
        return None
    
    # Get the geotransform
    geotransform = dataset.GetGeoTransform()
    
    if geotransform is None:
        print("Error: No geotransform found in the TIFF file.")
        return None
    
    # Extract geolocation information
    origin_x = geotransform[0]
    origin_y = geotransform[3]
    pixel_width = geotransform[1]
    pixel_height = geotransform[5]
    
    # Get the projection
    projection = dataset.GetProjection()
    
    return {
        "origin_x": origin_x,
        "origin_y": origin_y,
        "pixel_width": pixel_width,
        "pixel_height": pixel_height,
        "projection": projection
    }

# Example usage
tiff_file = "Forest_1.tif"
geolocation_info = get_geolocation(tiff_file)

if geolocation_info is not None:
    print("Geolocation Information:")
    print("Origin X:", geolocation_info["origin_x"])
    print("Origin Y:", geolocation_info["origin_y"])
    print("Pixel Width:", geolocation_info["pixel_width"])
    print("Pixel Height:", geolocation_info["pixel_height"])
    print("Projection:", geolocation_info["projection"])
