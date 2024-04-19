# FFMPEG
This Python script uses FFmpeg and Streamlink to extract frames and audio from a live stream URL.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python (version 3.6 or higher)
- FFmpeg
- Streamlink
You can install Streamlink using pip:
```python
pip install streamlink
```

## Usage
- Replace live_stream_url with your desired live stream URL.
- Run the script using Python:
```python
python ffmpeg_live_stream.py
```
The script will extract one frame per second from the live stream for a duration of 10 seconds and save them as frame_01.jpg, frame_02.jpg, and so on. It will also extract the audio and save it as output_audio1.mp3.

## Dependencies
- Streamlink
- FFmpeg

## License
This project is licensed under the MIT License.
