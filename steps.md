***1. Create a Virtual Environment and Install Dependencies***
python3 -m venv .venv

***2. Activate the Virtual Environment and Install Required Packages***
source .venv/bin/activate

***3. Install Required Packages***

**notice **: Make sure to run the following command inside the   *** activated virtual environment ###

pip install requests python-dotenv Flask

***4. Upgrade pip to the Latest Version***
python3  -m pip install --upgrade pip 
<!-- or -->
python3  -m pip install -U pip

pip freeze > requirements.txt

***5. Create .env & .gitignore files***

***6. OpenWeather API Key***
and add it to the .env file as shown below:
API_KEY=your_api_key_here

***7 create static and templates folders for Flask app***
mkdir static templates
inside templates create index.html file
inside static create style.css file

***8. Install Waitress for Production Deployment***
pip install waitress

pip freeze > requirements.txt