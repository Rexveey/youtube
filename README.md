# Rex YouTube Downloader

A simple YouTube video downloader built using Python's `tkinter` for the graphical interface and `pytubefix` for downloading videos. Users can download videos by entering a YouTube video URL, and the video will be saved in the highest available resolution.

## Features

- **GUI-based YouTube downloader**: Easy-to-use interface for downloading videos.
- **MP4 format**: Downloads videos in MP4 format with the highest resolution.
- **Custom download location**: Allows users to choose the directory to save the video.
- **Error handling**: Handles invalid URLs, download errors, and missing download paths.

## Requirements

- **Python 3.6+**
- **tkinter** (comes pre-installed with most Python installations)
- **pytubefix** (modified version for YouTube compatibility)

## Installation

1. Install the required libraries using `pip`:

    ```bash
    pip install tkinter
    pip install https://github.com/JuanBindez/pytubefix
    ```

2. Save the provided Python script.

## How to Run

1. Run the script using Python:

    ```bash
    python youtube_downloader.py
    ```

2. A graphical interface will appear where you can enter the YouTube URL and select the download location.

3. Enter a valid YouTube video URL and click the "Download" button.

4. Select the folder where you want to save the video.

5. Once the download is complete, a success message will be displayed.

## Usage Example

1. Open the application.
2. Enter a YouTube URL such as:

    ```
    https://www.youtube.com/watch?v=EXAMPLE
    ```

3. Click the "Download" button.
4. Choose the directory where the video will be saved.
5. Wait for the download to finish.

##
