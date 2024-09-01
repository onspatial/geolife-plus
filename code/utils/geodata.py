from pyproj import Transformer

def convert_coordinate(latitude, longitude, target_crs="epsg:4326", source_crs="epsg:32046"):
    transformer = Transformer.from_crs(source_crs, target_crs)
    return transformer.transform(latitude, longitude)