
# README: YouTube Video and Audio Downloader
This project is a YouTube video and audio downloader built using Python and yt-dlp. It provides a graphical user interface (GUI) to allow users to download YouTube videos in various resolutions and audio in different qualities. It also includes a progress display for the downloads.

## Features
1. Download Video in Various Resolutions
The downloader allows you to download YouTube videos in several predefined resolutions:
360p
480p
720p (HD)
1080p (Full HD)
1440p (2K)
2160p (4K)
You can choose the resolution using radio buttons in the interface.
Videos are downloaded in MP4 format by default, and if necessary, they are merged with the best available audio stream.

2. Download Only the Audio in MP3 Format
You can also download just the audio from a YouTube video.
The audio can be downloaded in various qualities (bitrate), such as:
64 kbps
128 kbps
192 kbps
256 kbps
320 kbps
The audio is automatically converted to MP3 using FFmpeg.
The quality options are displayed as radio buttons, which allow the user to select the desired bitrate.

3. Check Available Audio Qualities
The application allows you to check the available audio qualities for a video before downloading.
After you enter the video URL, you can click on a button that will list the available audio qualities (bitrate) as radio buttons, so you can select the one that fits your needs.

4. Progress Display for Downloads
The application provides a real-time progress bar for both video and audio downloads.
The percentage of the download is updated during the download process, giving the user visibility into how much of the file has been downloaded.
Upon completion, the progress label will update to show "Download completed!"
5. Select Download Folder

The application allows you to choose where to save your downloaded video or audio files.
You will be prompted to select a folder before starting the download, ensuring that the files are saved to your desired location.
How to Use the Application
Install Dependencies:

Make sure you have Python installed.
Install the required libraries by running the following commands:
bash
Copiar código
pip install yt-dlp
pip install tkinter
pip install ffmpeg-python
Run the Application:

### Run the main.py script by executing:
```python
python main.py
```
### This will open the graphical user interface (GUI) for the YouTube downloader.
### Download Video:

Enter the YouTube video URL into the provided text field.
Select the desired video resolution (360p, 480p, 720p, etc.) using the radio buttons.
Click the "Download Video" button to download the video. A progress label will show the percentage of the download.
Download Audio:

Enter the YouTube video URL into the provided text field.
Click the "Check Audio Qualities" button to display the available audio bitrates.
Select the desired audio quality using the radio buttons.
Click the "Download Audio" button to download the audio in MP3 format. The progress label will show the download progress.
Check Available Audio Qualities:

After entering the URL, click the "Check Audio Qualities" button to see all available bitrates.
The available audio bitrates will appear as radio buttons for you to select before downloading.
Requirements
Python 3.x
yt-dlp: A powerful tool to download video and audio from YouTube and other platforms.
Tkinter: A standard Python library used to create the graphical user interface.
FFmpeg: Used to merge video and audio streams and convert audio to MP3 format.
You can install these dependencies using the following commands:

bash
Copiar código
pip install yt-dlp
pip install tkinter
pip install ffmpeg-python
For FFmpeg, if it's not already installed on your system, follow these steps:

macOS: Install via Homebrew:

```bash
=> copy code
brew install ffmpeg
```
### Windows: Download and install FFmpeg from the official website: https://ffmpeg.org/download.html

### Project Structure
Copy code
```
├── main.py        # Main Python script containing the application logic
├── README.md      # This README file
```
Future Improvements
Add support for downloading playlists.
Add options to choose file formats other than MP3 and MP4, such as WebM.
Implement a retry mechanism for failed downloads.
Provide error handling for specific YouTube restrictions like age or region blocks.
License

If you have any questions or suggestions, feel free to contribute or open an issue!