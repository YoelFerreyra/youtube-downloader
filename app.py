import subprocess
import sys

try:
    import yt_dlp
except ImportError:
    print("Installing yt-dlp...")
    subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
    import yt_dlp

def check_ffmpeg():
    """Checks if ffmpeg is installed and installs it if necessary."""
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("ffmpeg is already installed.")
    except subprocess.CalledProcessError:
        print("Installing ffmpeg...")
        subprocess.run([sys.executable, "-m", "pip", "install", "imageio[ffmpeg]"], check=True)
        print("ffmpeg installed successfully.")

def download_video(url, output_format="mp4"):
    """Downloads a YouTube video and converts it to the desired format using yt-dlp and ffmpeg."""
    check_ffmpeg()
    try:
        print(f"Downloading video from: {url}")
        if output_format == "mp3":
            subprocess.run([
                sys.executable, "-m", "yt_dlp", "-f", "bestaudio", "--extract-audio", "--audio-format", "mp3", "-o", "%(title)s.%(ext)s", url
            ], check=True)
        else:
            subprocess.run([
                sys.executable, "-m", "yt_dlp", "-f", "bestvideo+bestaudio", "--merge-output-format", output_format, "-o", "%(title)s.%(ext)s", url
            ], check=True)
        print("Download completed.")
    except subprocess.CalledProcessError as e:
        print("Error downloading the video:", e)
        sys.exit(1)

def main():
    url = input("Enter the YouTube video URL: ")
    output_format = input("Output format (mp4/mkv/webm/mp3): ") or "mp4"
    download_video(url, output_format)

if __name__ == "__main__":
    main()