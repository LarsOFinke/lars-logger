import typer

app = typer.Typer(help="Life-Manager CLI")
# app.add_typer(auth_app, name="auth")


@app.command()
def app():
    print("CLI app started!")
    return 0


if __name__ == "__main__":
    app()
