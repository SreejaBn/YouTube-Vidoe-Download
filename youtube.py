import subprocess

def download_youtube_video():
    url = input("Paste the YouTube link here: ")

    print("\nAvailable resolution options:")
    print("1. Best available (default)")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    print("5. 360p")
    print("6. Custom (enter resolution like '1920x1080' or format code like '299+140')")

    choice = input("Enter your choice (1-6): ")

    yt_dlp_args = ["yt-dlp"]

    if choice == '1':
        yt_dlp_args.extend(["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"])
        print("Downloading best available resolution...")
    elif choice == '2':
        yt_dlp_args.extend(["-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best"])
        print("Downloading 1080p video...")
    elif choice == '3':
        yt_dlp_args.extend(["-f", "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best"])
        print("Downloading 720p video...")
    elif choice == '4':
        yt_dlp_args.extend(["-f", "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best"])
        print("Downloading 480p video...")
    elif choice == '5':
        yt_dlp_args.extend(["-f", "bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]/best"])
        print("Downloading 360p video...")
    elif choice == '6':
        custom_res = input("Enter custom resolution (e.g., '1920x1080') or format code (e.g., '299+140'): ")
        # Check if it's a resolution string or a format code
        if 'x' in custom_res:
            # Assuming it's a resolution like '1920x1080'
            width, height = custom_res.split('x')
            yt_dlp_args.extend(["-f", f"bestvideo[width<={width}][height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[width<={width}][height<={height}][ext=mp4]/best"])
        else:
            # Assuming it's a format code like '299+140'
            yt_dlp_args.extend(["-f", custom_res])
        print(f"Downloading video with custom resolution/format: {custom_res}...")
    else:
        print("Invalid choice. Downloading best available resolution by default.")
        yt_dlp_args.extend(["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"])

    yt_dlp_args.append(url)

    try:
        print("Starting download...")
        subprocess.run(yt_dlp_args, check=True) # Added check=True to raise CalledProcessError for non-zero exit codes
        print("Download completed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during download: {e}")
        print("Please ensure yt-dlp is installed and the URL is valid.")
    except FileNotFoundError:
        print("Error: yt-dlp command not found.")
        print("Please ensure yt-dlp is installed and added to your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
