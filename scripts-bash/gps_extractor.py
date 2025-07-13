import exifread

def get_decimal_from_dms(dms, ref):
    degrees = dms[0].num / dms[0].den
    minutes = dms[1].num / dms[1].den
    seconds = dms[2].num / dms[2].den

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps(filename):
    with open(filename, 'rb') as f:
        tags = exifread.process_file(f)

    gps_latitude = tags.get('GPS GPSLatitude')
    gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
    gps_longitude = tags.get('GPS GPSLongitude')
    gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = get_decimal_from_dms(gps_latitude.values, gps_latitude_ref.values)
        lon = get_decimal_from_dms(gps_longitude.values, gps_longitude_ref.values)
        print(f"[+] Coordenadas GPS encontradas:")
        print(f"    Latitud:  {lat}")
        print(f"    Longitud: {lon}")
        print(f"[+] Enlace Google Maps: https://www.google.com/maps?q={lat},{lon}")
    else:
        print("[-] No se encontraron datos GPS en la imagen.")

if __name__ == "__main__":
    archivo = input("📷 Ingrese el nombre del archivo de imagen (ej. foto.jpg): ")
    extract_gps(archivo)
