from astropy_healpix import HEALPix
import astropy.units as u
from geopy.geocoders import Nominatim
from math import log2, pi, acos


class NotPowerOf2(Exception):
    pass


def create_grid(reso: int) -> HEALPix:
    hp = HEALPix(nside=reso, order="nested")
    return hp


def search_by_lonlat(lon, lat, hp: HEALPix) -> list:
    return hp.cone_search_lonlat(lon * u.deg, lat * u.deg,
                                 radius=1 * u.deg)


def calculate_location_steradian(loc_pixels: list, hp: HEALPix):
    return len(loc_pixels) * hp.pixel_area


def calculate_surface_area(sol_angle, radius=6371000 * u.m):
    return sol_angle.value * radius ** 2


def calculate_cone_angle(sol_angle):
    return 2 * acos(1 - (sol_angle.value / (2 * pi))) * u.rad


def find_geolocation(lon, lat):
    geolocator = Nominatim(user_agent="geoapiExercises")
    loc = geolocator.reverse(str(lat) + "," + str(lon))
    return loc


if __name__ == "__main__":
    resolution = int(input("Write a number. Must be a power of two: "))
    if not log2(resolution).is_integer():
        raise NotPowerOf2("The number should be a power of 2!")
    longitude = float(input("Write longitude: "))
    latitude = float(input("Write latitude: "))

    healpix = create_grid(resolution)
    visible_pixels = search_by_lonlat(longitude, latitude, healpix)

    solid_angle = calculate_location_steradian(visible_pixels, healpix)
    area = calculate_surface_area(solid_angle)
    plane_angle = calculate_cone_angle(solid_angle)

    location = find_geolocation(longitude, latitude)

    print("We are at the " + str(location))
    print("The solid angle(field of view) is " + str(solid_angle))
    print("The cone's angle(plane angle) is " + str(plane_angle))
    print("The surface area is " + str(area))

