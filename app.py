from flask import Flask, request, jsonify
from models import db
from config import DATABASE_URI
import pandas as pd
from flask import render_template
from libraries.etl import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db.init_app(app)

#Frontend Section
@app.route('/')
def root():
    return render_template('home.html')

@app.route('/upload_csv_form')
def upload_csv_form():
    return render_template('upload_csv.html')

@app.route('/hires_by_deparment_jobs')
def get_page_hires_by_departmens_jobs():
    return render_template('hires_by_departments_and_jobs.html')

@app.route('/hires_above_mean')
def get_page_hires_above_mean():
    return render_template('hires_above_mean.html')


#Backend section
@app.route('/upload_csv', methods=['POST'])
def upload_csv():

    csv_file = request.files['file']
    if not csv_file:
        return jsonify({"error":"No file uploaded"}), 400
    
    file_name = csv_file.filename
    
    try:

        df = pd.read_csv(csv_file, header=None)

        if file_name == 'departments.csv':

            fn_transform_load_departmens(df)

        elif file_name == 'jobs.csv':

            fn_transform_load_jobs(df)

        elif file_name == 'hired_employees.csv':

            fn_transform_load_employees(df)

        else:

            return jsonify({"error": "Unsupported file type"}), 400

        return jsonify({"message": "File uploaded and processed successfully"}), 200


    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/metrics/departments_above_mean', methods=['GET'])
def departments_above_mean():

    query = 'select * from vst_hires_above_mean'
    result = fn_get_data(query)
    output = []

    for row in result:
        output.append({'id': row[0],
                       'department': row[1],
                       'hired': row[2]})
    
    return jsonify(output)

@app.route('/metrics/hires_by_department_and_job', methods=['GET'])
def hires_by_department_and_job():

    query = 'select * from vst_hires_by_department_and_job;'
    result = fn_get_data(query)
    output = []
    
    for row in result:
        output.append({
            "department": row[0],
            "job": row[1],
            "Q1": row[2],
            "Q2": row[3],
            "Q3": row[4],
            "Q4": row[5]
        })
    return jsonify(output)

#Main section
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)