import bh_deedoo.cmds.deedoo as deedoo
import bh_deedoo.cmds.deedoo2 as deedoo2

import typer
app = typer.Typer()
app.add_typer(deedoo.app, name="deedoo")
app.add_typer(deedoo2.app, name="deedoo2")
def main():
    app()
