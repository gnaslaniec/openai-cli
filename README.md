# OpenAI CLI Application

### Overview
A simple Python CLI application demonstrating how to integrate with the OpenAI API to leverage the power of natural language processing, to generate text or image based on user input.

### Prerequisites
Before using this application, ensure you have the following:

- Python 3.x installed
- OpenAI API key (sign up at https://beta.openai.com/signup/ to get yours)

## Instalation

1 - Clone the repository:
```bash
$ git clone https://github.com/your-username/openai-cli.git
$ cd openai-cli
```

2 - Create and activate a virtual environment:
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3 - Install the required dependencies:
```bash
$ pip install -e .
```

4 - Add the OpenAI API key to your environment variables:
```bash
$ export OPENAI_API_KEY=your_api_key
```
To make this change persistent, consider adding the line to your shell profile file (e.g., .bashrc, .zshrc).

## Usage
Run the CLI application by executing the following command in your terminal:

```bash
$ openai_cli
```
Follow the on-screen instructions to input your text prompts and interact with the OpenAI language model. The generated text or image url will be displayed in the console.
