from openai import OpenAI

class OpenAIClient:
    def __init__(self, model):
        self.client = OpenAI()
        self.model = model

    def create_completion(self, prompt):
      completion = self.client.chat.completions.create(
          model=self.model,
          messages=[
              {"role": "user", "content": prompt}
          ]
      )
      return completion
  
    def generate_image(self, prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url