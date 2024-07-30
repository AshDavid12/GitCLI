# Natural Language to Git Command Translator

This project provides a CLI tool that translates natural language descriptions into Git commands and executes them within a Git repository. The tool uses OpenAI's GPT-3.5-turbo model for natural language processing and the `git` library for executing Git commands.

## Project Structure

```plaintext
.
├── git_commands.py
├── nlp_helper.py
├── cli.py
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
```

## Overview
**git_commands.py** -  This module contains a function to execute Git commands.  
**nlp_helper.py** - This module interacts with the OpenAI API to convert natural language prompts into Git commands.  
**cli.py**- This module sets up a CLI interface using Click to translate natural language inputs into Git commands and execute them.


## Installation
To run this project locally, follow these steps:  

### Clone the repository:  
```
git clone https://github.com/yourusername/GitCLI.git  
cd GitCLI
```  
### Install Poetry: 
If you don't have Poetry installed, you can install it by following the instructions here.  
Install the dependencies:`poetry install`  
### Set up environment variables:  
Create a .env file in the root directory of the project and add your OpenAI API key:
```OPENAI_API_KEY=your_openai_api_key``` 
### Using Docker Compose 
Build and run the Docker containers:
`docker-compose up --build`  

## Usage

Run the CLI tool by providing a natural language description of the Git command you want to execute:  
```
poetry run python cli.py "create a new branch named feature-x"
```  
The tool will translate the input into a Git command and execute it within the current repository.
