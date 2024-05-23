from langchain_community.llms import Bedrock

def get_text_response(input_content): #text-to-text client function

    llm = Bedrock( #create a Bedrock llm client
        model_id="ai21.j2-ultra-v1", #set the foundation model  cohere.command-r-v1:0
                    
                                        # anthropic.claude-3-sonnet-20240229-v1:0
        model_kwargs={
            "maxTokens": 512, 
            "temperature": 1, 
            "topP": 0.5, 
            "stopSequences": [], 
            "countPenalty": {"scale": 0 }, 
            "presencePenalty": {"scale": 0 }, 
            "frequencyPenalty": {"scale": 0 }
        }
        # model_kwargs={
        #     "max_tokens": 512,
        #     "temperature": 0,
        #     "p": 0.01,
        #     "k": 0,
        #     "stop_sequences": [],
        #     "return_likelihoods": "NONE"
        # }
    )
    
    return llm.invoke(input_content) #return a response to the prompt

