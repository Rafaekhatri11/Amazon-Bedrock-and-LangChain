import json
import boto3

session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

def chunk_handler(chunk):
    print(chunk, end='')

def get_streaming_response(prompt, streaming_callback):

    bedrock_model_id = "anthropic.claude-3-sonnet-20240229-v1:0" #set the foundation model
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 20,
        "temperature": 0,
        "messages": [
            {
                "role": "user",
                "content": [{ "type": "text", "text": prompt } ]
            }
        ],
    })
    
    response = bedrock.invoke_model_with_response_stream(modelId=bedrock_model_id, body=body) #invoke the streaming method
    
    for event in response.get('body'):
        # print("Checking event ", event )
        chunk = json.loads(event['chunk']['bytes'])
        # print("Checking typy", chunk['type'])
        if chunk['type'] == 'content_block_delta':
            if chunk['delta']['type'] == 'text_delta':
                streaming_callback(chunk['delta']['text'])
                # print("checking text", chunk['delta']['text'])

prompt = "Tell me a story about two puppies and two kittens who became best friends:"
                
get_streaming_response(prompt, chunk_handler)

