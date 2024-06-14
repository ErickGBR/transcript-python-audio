```markdown
# Audio Transcription Project

This project allows you to transcribe audio files from a given URL, detect the language of the transcription, and save the transcription to a text file.

## Features

- Download audio from a provided URL.
- Transcribe the audio to text using Whisper.
- Detect the language of the transcribed text.
- Save the transcribed text to a file.

## Requirements

- Python 3.7+
- Django 3.2+
- FFmpeg
- pip (Python package installer)

## Setup Instructions

### Clone the Repository

```sh
git clone https://github.com/ErickGBR/transcript-python-audio.git
cd transcribe_audio
```

### Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Create a `requirements.txt` file with the following content:

```text
Django>=3.2
requests>=2.25.1
openai-whisper
langdetect
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

### Configure and Run the Django Project

1. Apply database migrations:

    ```sh
    python manage.py migrate
    ```

2. Run the Django development server:

    ```sh
    python manage.py runserver
    ```

3. Open your web browser and navigate to `http://localhost:8000/transcribe/`.

### Docker Instructions

If you prefer to use Docker, follow these instructions:

#### Create a `Dockerfile`

Create a `Dockerfile` with the following content:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Build and Run the Docker Container

1. Build the Docker image:

    ```sh
    docker build -t transcribe_audio .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8000:8000 transcribe_audio
    ```

3. Open your web browser and navigate to `http://localhost:8000/transcribe/`.

## Usage

### Web Interface

1. Navigate to `http://localhost:8000/transcribe/`.
2. Enter the URL of an audio file (in MP3 format).
3. Click "Transcribe".
4. The transcribed text and detected language will be displayed, and the transcription will be saved to a text file.

### Code Overview

- `app/helpers.py`: Contains the `AudioTranscriber` class with methods for downloading audio, transcribing it, detecting the language, and saving the transcription.
- `app/views.py`: Contains the view function `transcribe_audio_view` to handle the transcription process via the web interface.
- `app/templates/transcribe.html`: The HTML template for the web interface.

## Troubleshooting

### Permission Denied Errors with Docker

If you encounter a `permission denied` error when running Docker commands, you may need to add your user to the `docker` group:

```sh
sudo usermod -aG docker $USER
```

Then, restart your session.

### Missing Dependencies

Ensure all required dependencies are installed. You can install FFmpeg with the following command:

```sh
sudo apt-get install ffmpeg
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```