import geoip2.database
import pycountry
import numpy as np
import folium
import pandas as pd

def main():
    input='a21.tyo.20230721.ip'
    df = make_df(input)
    make_map(df)
    
def country_checker(ipaddress):
    try :
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ipaddress)
        return pycountry.countries.get(alpha_2=response.country.iso_code).alpha_3
    except:
        return None
    
def make_df(input):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    df = pd.DataFrame(columns=['country', 'counts'])
    with open(input) as f:
        for i, l in enumerate(f):
            l = l.split()
            response = country_checker(l[1])
            df=df.append(pd.DataFrame([[response, int(l[0])]],columns=['country', 'counts']))
    df2 = df[["country", "counts"]].groupby('country').agg(np.sum)
    df2['iso_code'] = df2.index
    print(df2)
    return df2

def make_map(df):
    # world map import
    m = folium.Map(location=[50, 0], zoom_start=1)
    geojson = "./folium/examples/data/world-countries.json"
    # visualization
    folium.Choropleth(
    geo_data=geojson,
    name='choropleth',
    data=df, # Input DataFrame
    columns=['iso_code', 'counts'], 
    key_on='feature.id',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=1,
    legend_name='IP Adress Access' 
    ).add_to(m)
    
    m.save("world.html")

if __name__ == "__main__":
    main()