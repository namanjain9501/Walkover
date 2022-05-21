Walkover Doc Platform
Installation
Prerequisites
1. Install Python
Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

2. Install MySQL
Install mysql-8.0.15. Follow the steps form the below reference document based on your Operating System. Reference: https://dev.mysql.com/doc/refman/5.5/en/

3. Setup virtual environment
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir env

# Create virtual environment
virtualenv ./env/

# Activate virtual environment
source env/bin/activate
4. Clone git repository
git clone "https://github.com/namanjain9501/walkover.git"
5. Install requirements
cd walkover/
pip install -r requirements.txt


6. Run the server
# Make migrations
python manage.py makemigrations
python manage.py migrate

# For search feature we need to index certain tables to the haystack. For that run below command.
python manage.py rebuild_index

# Run the server
python manage.py runserver 

# your server is up on port 8000
Try opening http://localhost:8000 in the browser. Now you are good to go.