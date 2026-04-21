# FastAPI student API

A Simple Student Management API built with FastAPI

## Features
- Create a student
- View all students
- View a singe student
- Update student
- Delete student
- Search students by name

  ---

  ## Tech Stack
  - Python
  - FastAPI
  - Unicorn

    ## Project Structure
    fastapi-student-project/
    |
    |--- app/
         |---main.py
         |---schemas.py
         |---models.py
         |---database.py
    |
    |--- requirements.txt
    |--- .gitignore
    |___ README.md


    ## How To Run Locally
    1. Clone the repository
       git clone
       https://github.com/Glorie27/fastapi-student-project.git
       cd fastapi-student-project

    2. Create a virtual environment
       python -m venv venv

    3. Activate the virtual environment
       venv\Scripts\activate

    4. Install dependencies
       pip install -r
       requirements.txt

    5. Start the Server
       uvicorn app.main:app --reload

    6. Open API documentation
       open the browser and go to: http://127.0.0.1:8000/docs

    7. API Endpoints
        - POST "/students" → Create a student
        - GET "/students" → Get all students
        - GET "/students/{id}" → Get a single student
        - PUT "/students/{id}" → Update a student
        - DELETE "/students/{id}" → Delete a student
        - GET "/students/search?name=..." → Search students
      
    8.  Notes
        - Data is stored in memory (no database yet)
        - Server reloads automatically when code changes
        - This is a beginner-friendly project for learning FastAPI
Author

Built by Glory
       
       
