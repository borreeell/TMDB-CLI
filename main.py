import typer
from movies.commands import movies_app

app = typer.Typer()

app.add_typer(movies_app, name="")

if "__main__" == __name__:
    app()