# Music-Genre-Classification
This Django project provides a web interface for uploading audio files, converting them from MP3 to WAV format, and processing them using custom preprocessing and prediction functions. Also uses CNN to classify music genres based on audio segments, selecting the genre with the highest probability as the prediction. 

## Features

- Upload MP3 audio files
- Convert MP3 files to WAV format
- Preprocess and predict genre using custom functions

## Requirements

- Python 3.x
- Django
- pydub
- ffmpeg (for pydub to handle audio conversion)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure `ffmpeg` is installed on your system. You can install it using Homebrew on macOS:
    ```sh
    brew install ffmpeg
    ```

## Usage

1. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/`.

3. Upload an MP3 file using the provided form.

## Project Structure

- `views.py`: Contains the view functions for handling file uploads and audio processing.
- `preprocess.py`: Custom preprocessing functions for audio files.
- `predict.py`: Custom prediction functions for audio files.

