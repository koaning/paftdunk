import uvicorn
import click

from paftdunk.web import create_app


@click.group()
def main():
    pass


@click.command()
def train():
    """trains a model"""
    pass


@click.command()
def demo():
    """stars a demo server"""
    pass


@click.command()
def evaluate():
    """evaluates a model"""
    pass


@click.command()
@click.option("--model", help="folder containing trained model")
def serve(model):
    """start a recommender server"""
    app = create_app(model)
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")


main.add_command(train)
main.add_command(evaluate)
main.add_command(serve)
main.add_command(demo)


if __name__ == "__main__":
    main()
