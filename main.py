from astropy_healpix import HEALPix
from astropy import units as u
from geopy.geocoders import Nominatim

# hp = HEALPix(nside=2, order='nested')
# hp.pixel_area = 50 * u.meter
# print(hp.cone_search_lonlat(2.349014 * u.deg, 48.864716 * u.deg,
#                             radius=10 * u.deg))


def create_grid(resolution: int, grid_type: str):
    hp = HEALPix(nside=resolution, order=grid_type)
    return hp


def define_pixel_area(area,hp):
    hp.pixel_area = area * u.meter


def search_by_lonlat(lon, lat, radius,hp):
    return hp.cone_search_lonlat(lon * u.deg, lat * u.deg,
                                 radius=radius * u.deg)


def calculate_visible_area(pixels,hp):
    return len(pixels) * hp.pixel_area


def find_geolocation(lon, lat):
    geolocator = Nominatim(user_agent="geoapiExercises")
    return geolocator.geocode(lat + "," + lon)


if __name__ == "__main__":
    pass
