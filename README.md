# simple-django-project
## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)


#### 2. Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir env

# Create virtual environment
virtualenv ./env/

# Activate virtual environment
source env/bin/activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/namanjain9501/walkover.git"
```

#### 4. Install requirements
```bash
cd simple-django-project/
pip install -r requirements.txt
```


#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# For search feature we need to index certain tables to the haystack. For that run below command.
python manage.py rebuild_index

# Run the server
python manage.py runserver 0:8000

# your server is up on port 8000
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go.

