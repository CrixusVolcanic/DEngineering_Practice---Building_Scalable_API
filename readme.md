# Globant Test Application

Welcome to the Globant Test Application repository. This application is built with Flask and SQLAlchemy and is designed to demonstrate various features, including uploading CSV files, fetching metrics, and more.

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
