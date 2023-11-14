import re

def nmea_to_lat_long(nmea_sentence):
    pattern = re.compile(r'\$GPGGA,(\d+\.\d+),(\d+\.\d+),([NS]),(\d+\.\d+),([EW]),.*\*([0-9A-Fa-f]+)')
    match = pattern.match(nmea_sentence)

    if not match:
        print("invalid syntax")
        return None
    
    # Extract relevant groups from the match
    _, lat_deg, lat_dir, lon_deg, lon_dir, _ = match.groups()

    # Convert latitude and longitude to decimal degrees
    latitude = float(lat_deg[:2]) + float(lat_deg[2:]) / 60.0
    longitude = float(lon_deg[:3]) + float(lon_deg[3:]) / 60.0

    # Adjust for direction (N/S, E/W)
    if lat_dir == 'S':
        latitude = -latitude
    if lon_dir == 'W':
        longitude = -longitude

    return latitude, longitude


#$GPGGA,131042.652,5246.176,N,00506.306,E,1,12,1.0,0.0,M,0.0,M,,*69
print(nmea_to_lat_long(input("NMEA sentence: \n")))
