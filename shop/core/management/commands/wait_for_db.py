import socket
import time
import os
import psycopg2

from psycopg2 import OperationalError as Psycopg20perror

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self,*args, **options):
        self.stdout.write('Connecting to database...')
        db_up = False
        while db_up == False: 
            try:
                conn = psycopg2.connect(dbname=os.environ.get('DB_NAME'), user=os.environ.get('DB_USER'), host=os.environ.get('DB_HOST'), 
                                        password=os.environ.get('DB_PASSWORD'), port=os.environ.get('DB_PORT'))
                # conn = psycopg2.connect(dbname='postgres', user='maus', host='db', 
                #                         password='maus', port='5432')
                cursor = conn.cursor()
                db_up = True
            except(Psycopg20perror, OperationalError):
                self.stdout.write('Database unavailable, waiting...kurva')    
                time.sleep(1)   
        self.stdout.write(self.style.SUCCESS('Database is ready!!!'))



