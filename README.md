# eplc
eastern panhandle liberation center website

## Local development

1. Make sure python3 is installed on your machine
2. In the project root directory, create and activate a virtualenv for managing dependencies:
```bash
   python3 -m venv .venv 
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate   # On Windows
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Migrate database:
```bash
   cd backend
   python manage.py migrate
```
5. Run server:
```bash
   python manage.py runserver
```
6. Test API. You should be able to visit [http://127.0.0.1:8000/api/events/](http://127.0.0.1:8000/api/events/) to see a (empty) list of events.
