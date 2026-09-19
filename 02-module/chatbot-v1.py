from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv
import os


load_dotenv()
project_endpoint = os.environ.get('END_POINT')
project_client = AIProjectClient(
    #Connexion to azure without using the API
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

open_client = project_client.get_openai_client()

#We use an OpenClient just to make a simple request to the model 

last_response = None

while True:
    message = input("\nYou:")
    if message == "quit":
        break

    #Sending an input to the model in my project via the open client 
    response = open_client.responses.create(
        model="gpt-4.1-mini",
        input=message, 
        max_output_tokens=200,
        #For the first cae with id = None 
        **({"previous_response_id": last_response} if last_response else {})
    )

    print(response.output_text)
    last_response = response.id
