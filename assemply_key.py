# # `pip3 install assemblyai` (macOS)
# # `pip install assemblyai` (Windows)
#
# import assemblyai as aai
#
# aai.settings.api_key = "d6a1ba84c1c7462ba1e5d4fe0d6d6287"
# transcriber = aai.Transcriber()
#
# transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")
#
# print(transcript.text)
#
# from elevenlabs.client import ElevenLabs
#
# client = ElevenLabs(
#   api_key="sk_090b5f7056c39bd95e1ec44b6ac79dab82b93448c63a2758", # Defaults to ELEVEN_API_KEY
# )
#
# response = client.voices.get_all()
# audio = client.generate(text="Hello there!", voice=response.voices[0])
# print(response.voices)

from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_090b5f7056c39bd95e1ec44b6ac79dab82b93448c63a2758", # Defaults to ELEVEN_API_KEY
)

response = client.voices.get_all()
# audio = client.generate(text="Hello there!", voice=response.voices[0])
print(response.voices)