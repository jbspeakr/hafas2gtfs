# -*- encoding: utf-8 -*-
"""
Projector

Provides standard projectors to transform coordinates:
    UTM32 to LatLon
    GK2 to LatLon

"""
from pyproj import Proj

projector_utm = Proj(
    proj='utm',
    zone=32,
    ellps='WGS84'
)

projector_gk = Proj(
    proj='tmerc',
    lat_0=0,
    lon_0=6,
    k=1,
    x_0=2500000,
    y_0=0,
    ellps='bessel',
    towgs84='582,105,414,1.04,0.35,-3.08,8.3',
    units='m'
)


def convert_gk(x, y):
    """ GK2LatLon """
    lon, lat = projector_gk(x, y, inverse=True)
    return lat, lon


def convert_utm(x, y):
    """ UTM2LatLon """
    lon, lat = projector_utm(x, y, inverse=True)
    return lat, lon
