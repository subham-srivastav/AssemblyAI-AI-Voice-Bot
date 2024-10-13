import assemblyai as aai
import openai
import elevenlabs
from queue import Queue

# Set API keys
aai.settings.api_key = "d6a1ba84c1c7462ba1e5d4fe0d6d6287"
openai.api_key = "d6a1ba84c1c7462ba1e5d4fe0d6d6287"
elevenlabs_api_key = "sk_090b5f7056c39bd95e1ec44b6ac79dab82b93448c63a2758"

transcript_queue = Queue()

def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return
    if isinstance(transcript, aai.RealtimeFinalTranscript):
        transcript_queue.put(transcript.text + '')
        print("User:", transcript.text, end="\r\n")
    else:
        print(transcript.text, end="\r")

def on_error(error: aai.RealtimeError):
    print("An error occured:", error)

# Conversation loop
def handle_conversation():
    while True:
        transcriber = aai.RealtimeTranscriber(
            on_data=on_data,
            on_error=on_error,
            sample_rate=44_100,
        )

        # Start the connection
        transcriber.connect()

        # Open  the microphone stream
        microphone_stream = aai.extras.MicrophoneStream()

        # Stream audio from the microphone
        transcriber.stream(microphone_stream)

        # Close current transcription session with Crtl + C
        transcriber.close()

        # Retrieve data from queue
        transcript_result = transcript_queue.get()

        # Send the transcript to OpenAI for response generation
        response = openai.ChatCompletion.create(
            model = 'gpt-4',
            messages = [
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 1000 characters.'},
                {"role": "user", "content": transcript_result}
            ]
        )

        #text = response['choices'][0]['message']['content']
        text = "AssemblyAI is the best YouTube channel for the latest AI tutorials."

        # Convert the response to audio and play it
        audio = elevenlabs.generate(
            text=text,
            voice="Bella" # or any voice of your choice
        )

        print("\nAI:", text, end="\r\n")

        elevenlabs.play(audio)

handle_conversation()




