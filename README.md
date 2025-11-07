# Weather App - Python Flask

A simple weather application built with Python Flask that fetches current weather conditions from the OpenWeather API and displays them in a clean web interface.

## 🌟 Features

- Real-time weather data from OpenWeather API
- Clean and responsive user interface
- Displays temperature, feels-like temperature, and weather conditions
- Dockerized for easy deployment
- Production-ready with Waitress WSGI server

## 🛠️ Technologies Used

- **Python 3.11**
- **Flask** - Web framework
- **Waitress** - Production WSGI server
- **python-dotenv** - Environment variable management
- **requests** - HTTP library for API calls
- **Docker** - Containerization
- **OpenWeather API** - Weather data source

## 📋 Prerequisites

- Docker Desktop installed and running
- OpenWeather API key (get one free at [OpenWeather](https://openweathermap.org/api))

## 🚀 Quick Start with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/FaridBerlin/Weather-App-Python.git
cd Weather-App-Python
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
API_KEY=your_openweather_api_key_here
```

### 3. Build and Run with Docker Compose

```bash
docker compose up -d
```

### 4. Access the Application

Open your browser and navigate to:

```
http://localhost:7777
```

## 🐳 Docker Commands

### Start the Application

```bash
docker compose up -d
```

- Builds the image (if not already built)
- Starts the container in detached mode (runs in background)

### Stop the Application

```bash
docker compose down
```

- Stops and removes the container
- Network is also removed

### View Running Containers

```bash
docker compose ps
```

### View Application Logs

```bash
docker compose logs -f weather-app
```

- `-f` flag follows the logs in real-time
- Press `Ctrl+C` to exit

### Restart the Application

```bash
docker compose restart
```

### Rebuild After Code Changes

```bash
docker compose up -d --build
```

- Forces a rebuild of the Docker image
- Use this when you've made changes to the code

### Stop the Container (without removing)

```bash
docker compose stop
```

### Start the Container Again

```bash
docker compose start
```

### Execute Commands Inside the Container

```bash
docker compose exec weather-app /bin/bash
```

- Opens a bash shell inside the running container

### Remove Everything (containers, images, volumes)

```bash
docker compose down --rmi all --volumes
```

## 💻 Local Development (Without Docker)

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 2. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

```bash
API_KEY=your_openweather_api_key_here
```

### 5. Run the Application

```bash
python server.py
```

### 6. Access the Application

```
http://localhost:8000
```

## 📁 Project Structure

```
Weather-App-Python/
├── server.py              # Flask application entry point
├── weather.py             # Weather API client
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Files to exclude from Docker image
├── .env                  # Environment variables (not in git)
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   ├── index.html       # Home page with search form
│   └── weather.html     # Weather results page
└── static/              # Static files
    └── css/
        └── style.css    # Stylesheet

```

## 🔧 Configuration

### Port Configuration

- **Docker**: Accessible on port `7777` (configured in `docker-compose.yml`)
- **Local**: Runs on port `8000` (configured in `server.py`)

To change the Docker port, edit `docker-compose.yml`:

```yaml
ports:
  - "YOUR_PORT:8000"
```

## 🌐 How It Works

1. User enters a city name in the web form
2. Flask receives the request and calls the OpenWeather API
3. Weather data is fetched and parsed
4. Results are displayed in a formatted template
5. Shows temperature in Celsius, feels-like temperature, and weather description

## 📝 Environment Variables

| Variable  | Description         | Required |
| --------- | ------------------- | -------- |
| `API_KEY` | OpenWeather API key | Yes      |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Farid Berlin**

***

- GitHub: [@FaridBerlin](https://github.com/FaridBerlin)

## 🙏 Acknowledgments

- [OpenWeather API](https://openweathermap.org/) for providing weather data
- [Flask](https://flask.palletsprojects.com/) for the awesome web framework
- [Dave Gray](https://www.youtube.com/@DaveGrayTeachesCode) for the tutorial inspiration
