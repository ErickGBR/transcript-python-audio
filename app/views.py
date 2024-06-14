from django.http import JsonResponse
from django.shortcuts import render
from .helpers import AudioTranscriber

def transcribe_audio_view(request):
    if request.method == "POST":
        url = request.POST.get('audio_url')
        transcriber = AudioTranscriber()
        
        audio_path = transcriber.download_audio(url)
        transcribed_text = transcriber.transcribe_audio(audio_path)
        language = transcriber.detect_language(transcribed_text)
        
        output_file = f"output/output_{language}.txt"
        if not os.path.exists("output"):
            os.makedirs("output")
        
        transcriber.create_and_open_txt(transcribed_text, output_file)
        
        response_data = {
            "transcribed_text": transcribed_text,
            "language": language,
            "output_file": output_file
        }
        return JsonResponse(response_data)
    return render(request, 'transcribe.html')

