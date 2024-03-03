import geoip2.database 
import pycountry 
import numpy as np 
import pandas as pd
import glob
from matplotlib import pyplot as plt

def main():
    reader = geoip2.database.Reader('/home/rswork/n-yamai/tmp/GeoIP2-City_20231229/GeoIP2-City.mmdb')
    #reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    dpath='*.txt'
    c_df = pd.DataFrame(columns=['country'])

    for path in glob.glob(dpath):
        print(path)
        p=path.replace('.txt','')
        df = make_df(reader,p,path)
        df2 = df[['country', p]].groupby('country').agg(np.sum)
        #df2['iso_code'] = df2.index
        c_df = pd.merge(c_df,df2,on='country',how='outer').fillna(0)
        
    c_df=c_df.set_index('country')

    print(c_df)
    #csvname= '/home/rswork/n-yamai/tmp/c_jp.csv'
    #c_df.to_csv(csvname)
    
    plt.stackplot(c_df.columns, c_df.loc['JPN'], c_df.loc['Other'],labels=c_df.index)
    plt.legend(loc="upper left")
    plt.show()


def country_checker(reader,ipaddress):
    try :
        response = reader.city(ipaddress)
        country =pycountry.countries.get(alpha_2=response.country.iso_code).alpha_3
        #if country !='JPN':
        #    country = 'Other'
        return country
    except:
        return None
    
def make_df(reader,p,input):
    df = pd.DataFrame(columns=['country', p])
    with open(input) as f:
        for i, l in enumerate(f):
            l = l.split()
            response = country_checker(reader,l[1])
            if i > 0:
                df=df._append(pd.DataFrame([[response, int(l[0])]],columns=['country', p]))
    return df

if __name__=="__main__":
    main()
