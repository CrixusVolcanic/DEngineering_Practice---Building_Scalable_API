# Data Engineering Practice: Building a Scalable API and Data Exploration System

This project is a hands-on practice aimed at developing a robust data engineering solution. The goal is to build a scalable REST API that handles historical data migration, batch processing, and data exploration with SQL. The project is designed to simulate real-world challenges and best practices in data engineering.

## Project Structure

### Section 1: REST API for Data Migration and Processing

In this section, a REST API was developed to:

1. Ingest Historical Data: Load data from CSV files representing different entities like departments, jobs, and employees.
2. Batch Data Upload: Process and upload this data to a SQL database.
3. Batch Transactions: Handle batch insertions of up to 1000 rows per request to ensure efficient data processing.

### Section 2: Data Exploration Using SQL

This section focuses on exploring the data inserted into the database:

1. Hiring Trends Analysis: Generate a report showing the number of employees hired per job and department in 2021, broken down by quarters.
2. Departmental Hiring Performance: Identify departments that hired more employees than the average across all departments, ranked in descending order.

### Bonus Track: Testing & Containerization

To enhance the robustness of the solution:

- Automated Testing: Comprehensive tests were implemented to validate the API’s functionality, using various testing libraries.
- Containerization: A Dockerfile was created to containerize the application, simplifying deployment and ensuring consistent environments.

### Technology Stack

- Programming Language: Python
- Framework: Flask for the API
- Database: MySQL
- Containerization: Docker
- Testing: PyTest

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/CrixusVolcanic/globant_test.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd globant_test
    ```

3. **Ensure you have Docker and Docker Compose installed on your system**. If you do not have them installed, you can find instructions for installing them [here](https://docs.docker.com/get-docker/) and [here](https://docs.docker.com/compose/install/).

4. **Build the Docker image**:

    ```bash
    docker-compose build
    ```

5. **Start the application using Docker Compose**:

    ```bash
    docker-compose up
    ```

The application will start running in the Docker container. You can access the application in your web browser at `http://localhost:8080`.

6. **To stop the application**:

    - Press `Ctrl + C` in the terminal where Docker Compose is running.
    - Alternatively, you can run the following command to stop the application and remove Docker containers:

        ```bash
        docker-compose down
        ```

## API Endpoints

- `/`: Home page of the application.
- `/upload_csv_form`: Page for uploading CSV files.
- `/upload_csv`: Endpoint for uploading CSV files to the application.
- `/metrics/departments_above_mean`: Endpoint for fetching data on departments above mean.
- `/metrics/hires_by_department_and_job`: Endpoint for fetching data on hires by department and job.

## Testing

To run the tests:

1. Activate your virtual environment (if not already active).
2. Run the tests using pytest:

    ```bash
    pytest test/
    ```

## File Structure

- `app.py`: Main application file.
- `config.py`: Configuration file.
- `models.py`: SQLAlchemy models for the application.
- `resources`: Directory containing SQL scripts and other resources.
- `templates`: Directory containing HTML templates.
- `test`: Directory containing test scripts.
- `requirements.txt`: File containing a list of required packages.
- `Dockerfile`: Docker configuration file.
- `docker-compose.yml`: Docker Compose configuration file.
- `README.md`: This file, providing an overview of the application.
