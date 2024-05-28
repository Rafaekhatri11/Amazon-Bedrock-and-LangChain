# Multimodal Chatbot with Amazon Bedrock, Anthropic Claude 3, and Streamlit

This repository contains the code and resources to build a multimodal chatbot using Amazon Bedrock, Anthropic Claude 3, and Streamlit. The chatbot can understand and respond to both text and image inputs, making interactions richer and more engaging.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [ChatMessage Class](#chatmessage-class)
  - [Utility Functions](#utility-functions)
  - [API Interaction Functions](#api-interaction-functions)
  - [Streamlit App](#streamlit-app)

## Introduction
A multimodal chatbot can handle multiple types of input, such as text and images. This project demonstrates the integration of text and image understanding using Amazon Bedrock, Anthropic Claude 3, and Streamlit.

## Features
- **State and Memory Management**: Tracks chat history externally (up to 20 previous chats) to handle state, ensuring meaningful and context-aware conversations. (After 20 chats, previous history will be lost.)
- **Streamlit Interface**: Provides a sleek and interactive front-end interface for a seamless user experience.

## Technologies Used
- **AWS Bedrock**: The backbone for the application, providing all the computational power for the AI model to work.
- **Boto3**: The AWS SDK for Python, used to interact with AWS Bedrock.
- **Anthropic Claude 3**: For understanding and generating responses to both text and image inputs.
- **Streamlit**: For creating an intuitive and interactive front-end interface.

1. Navigate to the project directory:

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run multimodal_chatbot_app.py --server.port 8080 --server.enableXsrfProtection=false
    ```
2. Open the provided URL in your web browser.
3. Interact with the chatbot by entering text or uploading images.

## Code Overview

### ChatMessage Class
A class to store chat messages, which can be either text or image messages.

### Utility Functions
- Converts image bytes to a BytesIO object.
- Converts image bytes to a Base64-encoded string.
- Reads and returns bytes from an image file.

### API Interaction Functions
- Converts chat messages to the format required by the Anthropic Claude Messages API.
- Constructs the request body for the InvokeModel API call.
- Interacts with the Anthropic Claude model to generate responses.

### Streamlit App
The Streamlit app provides a user interface for interacting with the multimodal chatbot. Key components include:
- Chat Input: For entering text messages.
- File Uploader: For uploading images.
- Buttons: For adding predefined images to the chat.
- Chat History: Displays the conversation history, including both text and image messages.