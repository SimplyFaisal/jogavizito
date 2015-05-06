import pandas as pd
import urllib2
import pymongo
from datetime import datetime


def file_names():
    url_base = 'http://www.football-data.co.uk/mmz4281/{}/E0.csv'
    files = []
    for i, j in zip(range(0,15), range(1,15)):
        season = str(i).rjust(2,'0') + str(j).rjust(2, '0')
        files.append(url_base.format(season))
    return files

def dictionize(frame):
    _dict = dict(zip(cf.iterrows()))
    try:
        _dict['Date'] = datetime.strptime(_dict['Date'], '%d/%m/%Y')
    except Exception as e:
        print e
    return _dict

def download_csv(url):
    response = urllib2.urlopen(url)
    return pd.read_csv(response)


if __name__ == '__main__':
    files = file_names()
    for _file in files[1:2]:
        try:
            cf = download_csv(_file)
            dictionize(cf)
        except Exception as e:
            print e
    
