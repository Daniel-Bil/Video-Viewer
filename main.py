import os

from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.editor import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.editor import AudioFileClip


def mp4_2_mp3converter(file1: str, file2: str):
    video = VideoFileClip(f"{file1}.mp4")
    video.audio.write_audiofile(f"{file2}.mp3")


def shorten_video(file1: str, start: int, end: int):
    video = VideoFileClip(f"{file1}.mp4")
    if end > video.duration:
        raise Exception("To long video")

    shortened_video = video.subclip(start, end)
    shortened_video.write_videofile(f"{file1}_shortened.mp4")


def shorten_audio(file1: str, start: int, end: int):
    audio = AudioFileClip(f"{file1}.mp3")
    if end > audio.duration:
        raise Exception("To long video")

    shortened_audio = audio.subclip(start, end)
    shortened_audio.write_audiofile(f"{file1}_shortened.mp3")


def combine_video_with_sound(file1:str, file2:str):
    video_clip = VideoFileClip(f'{file1}.mp4')
    audio_clip = AudioFileClip(f'{file2}.mp3')
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile('combined_videosound.mp4', codec='libx264', audio_codec='aac')

def combine_sounds(file1:str, file2:str):
    audio_clip1 = AudioFileClip(f'{file1}.mp3')
    audio_clip2 = AudioFileClip(f'{file2}.mp3')
    final_audio = concatenate_audioclips([audio_clip1, audio_clip2])
    final_audio.write_audiofile("output_sound.mp3")


def convert_mkv_2_mp4(file_name: str):
    video_clip = VideoFileClip(f"{file_name}.mkv")
    video_clip.write_videofile(f"{file_name}.mp4", codec="libx264")

def convert_mp4_2_gif(file_name: str):
    # Load the MP4 file
    video_clip = VideoFileClip(f"{file_name}.mp4")

    # Convert the video to a GIF with a specified frame rate
    video_clip.write_gif(f"{file_name}.gif", fps=30)


def shadow_clip(file1: str, file2: str):
    pass

if __name__ == '__main__':
    print("main")

    shorten_video("C:\\Users\\dxxx4\\Videos\\Desktop\\Desktop 2024.09.19 - 17.31.25.02",0,480)
    # convert_mp4_2_gif("./starrail/ratio_shortened")
    # mp4_2_mp3converter("bogdanoff","bogdanoff")

    # shorten_audio("bogdanoff",98,100)

    # combine_sounds("VVV_shortened", "VVV")
    # combine_video_with_sound("nuclear_shortened","VVV")
