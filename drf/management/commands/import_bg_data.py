import pandas as pd
import pytz
from datetime import datetime
from drf.models import Bungalow
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Import bungalow data."

    def handle(self, *args, **options):
        # get all records from csv file.
        bg_data = pd.read_csv('bungalow.csv').replace({pd.np.nan: None})
        bg_data_list = bg_data.to_dict('records')
        # Truncate all existed data
        Bungalow.objects.all().delete()
        # Insert csv data.
       
        for record in bg_data_list:
            try:
                last_sold_date = datetime.strptime(record['last_sold_date'],'%m/%d/%Y')
                record['last_sold_date'] = pytz.utc.localize(last_sold_date)
            except:
                record['last_sold_date'] = None
            try:    
                rentzestimate_last_updated = datetime.strptime(record['rentzestimate_last_updated'],'%m/%d/%Y')
                record['rentzestimate_last_updated'] = pytz.utc.localize(last_sold_date)
            except:
                record['rentzestimate_last_updated'] = None
            try:
                zestimate_last_updated = datetime.strptime(record['zestimate_last_updated'],'%m/%d/%Y')
                record['zestimate_last_updated'] = pytz.utc.localize(last_sold_date)
            except:
                record['zestimate_last_updated'] = None
            
            Bungalow.objects.create(**record)
        
        
            
                   