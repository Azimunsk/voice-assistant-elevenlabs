#import libraries 
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation 
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig
#Load environment variables
load_dotenv()

AGENT_ID = os.getenv('AGENT_ID')
API_KEY = os.getenv('API_KEY')

#print("Agent ID:", AGENT_ID)
#print("API Key:", API_KEY[:5] + "..." if API_KEY else "Not found")


#Conversation setup
user_name = 'Zimmy'
schedule = 'Call with the ssn head at 11:00; Gym with ayesha at 18:00'
prompt = f'You are chill helpful assistant. Your interlocutor has the following schedule:{schedule}.'
first_message = f'Hello{user_name}, how can i help you today?'
conversation_override = {
    'agent':{
        'prompt':{
            'prompt':prompt,
        },
        'first_message': first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body = {},
    dynamic_variables = {},
)
client = ElevenLabs(api_key=API_KEY)
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)

#callbacks for responses
def print_agent_response(response):
    print(f'Agent:{response}')

def print_interrupted_response(original, corrected):
    print(f'Agent Interrupted, truncated response:{corrected}')

def print_user_transcript(transcript):
    print(f'User:{transcript}')
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=False,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response= print_agent_response,
    callback_agent_response_correction = print_interrupted_response,
    callback_user_transcript=print_user_transcript,

)


conversation.start_session()
# import elevenlabs
# print(elevenlabs.__version__)
