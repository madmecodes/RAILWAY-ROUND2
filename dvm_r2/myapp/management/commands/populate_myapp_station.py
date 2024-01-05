# myapp/management/commands.py
import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import Station as myapp_station, Train

class Command(BaseCommand):
    help = 'Populate myapp_station model from Excel file'

    def handle(self, *args, **kwargs):
        file_path = '/home/madmecodes/Projects/RAILWAY-ROUND2/dvm_r2/myapp/management/commands/stationExcelData.xlsx'

        try:
            df = pd.read_excel(file_path)
            stations = []

            for index, row in df.iterrows():
                train_instance = Train.objects.get(train_number=row['train_number'])

                station = myapp_station(
                    train=train_instance,
                    train_number=row['train_number'],
                    station_code=row['station_code'],
                    station_name=row['station_name'],
                    distance=row['distance'],
                    arrival_time=str(row['arrival_time']),
                    halt_time=row['halt_time']
                )
                stations.append(station)

            myapp_station.objects.bulk_create(stations)
            self.stdout.write(self.style.SUCCESS('Successfully populated myapp_station model'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
