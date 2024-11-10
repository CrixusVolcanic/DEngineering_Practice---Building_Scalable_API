from models import db, Department, Job, Employee
from sqlalchemy import text
import pandas as pd

#ETL section  
def fn_transform_load_departmens(df):

    batch_size = 1000
    row_count = 0
    sql = "TRUNCATE TABLE departments RESTART IDENTITY CASCADE"

    db.session.execute(text(sql))

    column_names = ['id', 'department']
    df.columns = column_names

    for _, row in df.iterrows():
        department = Department(id=row['id'], department=row['department'])

        db.session.add(department)

        row_count += 1

        if row_count % batch_size == 0 or row_count == len(df):

            print('Batch loaded')

            db.session.commit()

def fn_transform_load_jobs(df):

    batch_size = 1000
    row_count = 0
    sql = 'TRUNCATE TABLE jobs RESTART IDENTITY CASCADE'

    db.session.execute(text(sql))

    column_names = ['id', 'job']
    df.columns = column_names

    for _, row in df.iterrows():

        job = Job(id = row['id'], job = row['job'])      

        db.session.add(job)
        row_count += 1

        if row_count % batch_size == 0 or row_count == len(df):

            print('Batch loaded')

            db.session.commit()

def fn_transform_load_employees(df):

    batch_size = 1000
    row_count = 0
    sql = 'TRUNCATE TABLE employees RESTART IDENTITY'

    db.session.execute(text(sql))

    column_names = ['id', 'name', 'datetime', 'department_id', 'job_id']
    df.columns = column_names
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['datetime'] = df['datetime'].replace({pd.NaT: None})
    df['job_id'] = df['job_id'].replace({float('nan'): None})
    df['department_id'] = df['department_id'].replace({float('nan'): None})

    for _, row in df.iterrows():

        employee = Employee(id = row['id'], name = row['name'], datetime = row['datetime'], department_id = row['department_id'], job_id = row['job_id'])

        db.session.add(employee)
        row_count += 1

        if row_count % batch_size == 0 or row_count == len(df):

            print('Batch loaded')

            db.session.commit()

def fn_get_data(query):
    
    return db.session.execute(text(query)).fetchall()