# ATS for Recruiters

This project is an Applicant Tracking System (ATS) for recruiters, built using Django and Django Rest Framework. The application helps recruiters manage and track job applications, with a focus on candidate management. It allows creating, updating, deleting, and searching candidates based on their names.

## Features

- **Candidate Model**: Tracks the following details about candidates:
  - Name
  - Age
  - Gender
  - Email
  - Phone Number


- **API Endpoints**:
  - **Create**: Add a new candidate.
  - **Update**: Update an existing candidate.
  - **Delete**: Remove a candidate.
  - **Search**: Search candidates by name, with results sorted based on relevancy (partial name matches are also considered).

## Search Logic

The search functionality works on the candidate's name. It returns results sorted based on the number of words in the search query that match the candidate’s name. The more matches, the higher the relevancy.

### Example:
For a search query `Ajay Kumar Yadav`, results will be ordered as:
["Ajay Kumar Yadav", "Ajay Kumar", "Ajay Yadav", "Kumar Yadav", "Ramesh Yadav", "Ajay Singh"]


**Important**: The search is done entirely through ORM queries (no Python scripts for filtering or sorting).

## Installation

To set up and run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

3. Create the database migrations:

    ```bash
    python manage.py makemigrations

4. Apply the migrations to the database:
    ```bash
    python manage.py migrate

5. Start the Django development server:
    ```bash
    python manage.py runserver

Now, the application should be up and running at http://127.0.0.1:8000/.