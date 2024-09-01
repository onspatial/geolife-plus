def get_latitudes(points):
    latitudes = []
    for point in points:
        latitudes.append(get_number(point,0))   
    return latitudes

def get_longitudes(points):
    longitudes = []
    for point in points:
        longitudes.append(get_number(point,1))  
    return longitudes

def get_number(point,index):
    point = point.split('(')[1].split(')')[0]
    point = point.split(' ')
    return point[index].strip()