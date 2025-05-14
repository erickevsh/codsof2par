import speech_recognition as sr
from moviepy.editor import VideoFileClip,AudioFileClip

class MovieManager:
    def get_wav_audio(self, mp4_file,wav_file):
        vc=VideoFileClip(mp4_file)
        ac=vc.audio
        ac.write_audiofile(wav_file,codec='pcm_s16le')
        ac.close()
        vc.close()

def audio_to_text(self,audio_file):
    r=sr.Recognizer()
    with sr.AudioFile(audio_file)as source:
        audio=r.record(source)
    try:
        text=r.recognize_google(audio)
        return text
    except:
        return f'unknow: {str(e)}'
    
    def remove_audio(self.mp4_file,output_mp4_file):
        video = VideoFileClip(mp4_file)
        video_Without_audio = Video.Without_audio()
        video_Without_audio.close()
        video.close()

    def speech_to_text(self, audio_file)
        r = sr.Recognizer()

        hellow=sr.AudioFile(audio_file)
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("Text: "+s)
        except Exception as e:
            print("Exception: "+str(e))
        return s

def text_to_speech(self, to_translate,to_lang):
    tranlated = GoogleTranslator(
        source='auto',
        larget=to_lang).translate(to_translate)
    print(tranlated)
    myobj = gTTS(
        text=tranlated,
        lang=to_lang,
        slow=False)
    myobj.save("welcome.mp3")

def add_audio_to_video(self, mp4_file, mp3_file,output_mp4_file):
    videoclip = VideoFileClip(mp4_file)
    audioclip = AudioFileClip(mp3_file)

    new_audioclip = CompositiveAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(output_mp4_file)
    
mm=MovieManager()
#mm.get_wav_audio('video.mp4', 'audio.wav')

