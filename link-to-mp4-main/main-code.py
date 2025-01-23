import yt_dlp
import os

def download_video(url, download_path):
    """
    Downloads a YouTube video as an MP4 file to the specified directory.

    Args:
        url (str): YouTube video URL.
        download_path (str): Path to save the downloaded video.

    Returns:
        None
    """


    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Options for yt_dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }
        ],
        'quiet': False,  # Set to True to suppress unnecessary output
    }

    try:
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Unknown Title')
            output_file = os.path.join(download_path, f"{title}.mp4")

        # Confirm file existence
        if os.path.exists(output_file):
            print(f"\nDownload complete! File saved at: {output_file}")
        else:
            print("\nError: File not found after download. Please check the process.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("YouTube Video Downloader\n")

    # Get the YouTube video URL
    video_url = input("Enter the YouTube video URL: ").strip()
    if not video_url:
        print("Error: You must provide a valid YouTube URL.")
        exit(1)

    # Get the download directory
    download_dir = input("Enter the directory to save the video (leave empty for current directory): ").strip()
    if not download_dir:
        download_dir = os.getcwd()  # Default to current directory

    # Start downloading
    download_video(video_url, download_dir)
