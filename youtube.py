import subprocess

url = input("Paste the YouTube link here: ")

try:
    print("Downloading video...")
    subprocess.run(["yt-dlp", "-f", "bestvideo+bestaudio", url])
    print("Download completed.")
except Exception as e:
    print(f"An error occurred: {e}")
