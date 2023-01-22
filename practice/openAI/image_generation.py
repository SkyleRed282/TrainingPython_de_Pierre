import os
import openai

if __name__ == '__main__':

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt="Peinture d'un couché de soleil sur une plage",
        n=5,
        size="1024x1024"
    )
    print(response)

