from pytube import YouTube
import os

# def Download(link):
#     c = 0
#     try:
#         youtubeObject = YouTube(link)
#         audio_stream = youtubeObject.streams.filter(only_audio=True).first()
#         audio_stream.download(output_path="./qwerty")
#         default_filename = audio_stream.default_filename
#         new_filename = f"download{c}.mp4"
#         os.rename(os.path.join("./qwerty", default_filename), os.path.join("./qwerty", new_filename))
#         print("Download is completed successfully")
#     except Exception as e:
#         print("An error has occurred:", e)
def Download(link):
    c = 0
    try:
        youtubeObject = YouTube(link)
        videoStream = youtubeObject.streams.get_lowest_resolution()
        videoStream.download(output_path="./qwerty")
        default_filename = videoStream.default_filename
        new_filename = f"download{c}.mp4"
        os.rename(os.path.join("./qwerty", default_filename), os.path.join("./qwerty", new_filename))
        print("Download is completed successfully")
    except Exception as e:
        print("An error has occurred:", e)
link = input("Enter the YouTube video URL: ")
Download(link)
