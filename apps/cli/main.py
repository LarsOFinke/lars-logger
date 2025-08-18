import typer

app = typer.Typer(help="Logger CLI")
# app.add_typer(auth_app, name="auth")


@app.command()
def app():
    print("CLI app started!")
    return 0


if __name__ == "__main__":
    app()
