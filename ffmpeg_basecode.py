#basic ffmpeg code
import subprocess
import streamlink

# Replace this with your live stream URL
live_stream_url = "https://www.youtube.com/watch?v=Wg0GwGB2-AI"

# Fetch the best quality stream URL
streams = streamlink.streams(live_stream_url)
stream_url = streams["best"].url

# FFmpeg command
ffmpeg_command = [
    'ffmpeg',
    '-i', stream_url,           # Input stream URL
    '-t', '10',                 # Duration to process the input
    '-vf', 'fps=1',             # Extract one frame per second
    'frame_%02d.jpg',           # Output frame file name pattern
    '-vn',                      # Ignore the video for the audio output
    '-acodec', 'libmp3lame',    # Set the audio codec to MP3
    '-t', '10',                 # Duration for the audio extraction
    '-y',                       # Overwrite output files without asking
    'output_audio1.mp3'          # Audio output file
]

# Run the FFmpeg command
subprocess.run(ffmpeg_command)
