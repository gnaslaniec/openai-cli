import click

from openai_cli.client import OpenAIClient

@click.group()
def cli():
    pass

@cli.command()
@click.argument("prompt")
@click.option(
    "-m", "--model", default="gpt-3.5-turbo", help="OpenAI model to use."
)
def completion(prompt: str, model: str) -> None:
    """Return OpenAI response from a text prompt."""
    client = OpenAIClient(model)
    completion = client.create_completion(prompt=prompt)
    click.echo(completion.choices[0].message.content)
    
@cli.command()
@click.argument("prompt")
@click.option("-m", "--model", default="dall-e-3", help="DallE model to use.")
@click.option("-s", "--save", is_flag=True, show_default=True, default=False, help="Saves the image on disk")
def image(prompt: str, model: str, save: bool) -> None:
    """Return OpenAI image from a text prompt."""
    if save:
        click.echo("TODO SAVE IMAGE")
    client = OpenAIClient(model)
    image_url = client.generate_image(prompt)
    click.echo(image_url)


@cli.command()
@click.option(
    "-m", "--model", default="gpt-3.5-turbo", help="OpenAI model to use."
)
def repl(model: str) -> None:
    """Start interactive shell session for OpenAI completion API."""
    client = OpenAIClient(model)
    while True:
        print(client.create_completion(prompt=input("Prompt: ")).choices[0].message.content)
        print()

if __name__ == "__main__":
    cli()