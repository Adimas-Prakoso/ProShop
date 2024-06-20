from controller.user_control import UsrLoginWindow
from rich.console import Console
from rich.markdown import Markdown
from rich.traceback import install
from PySide6.QtWidgets import QApplication
from rich.spinner import Spinner
from time import sleep
import os

os.environ["QT_LOGGING_RULES"] = "qt.qpa.*=false"

install()

app = QApplication([])
console = Console()
md = Markdown("# Welcome to the Pro Shop Management System\n\n## Please select your role\n\n1. User\n2. Admin\n\n3. Help")
console.print(md)

choice = input("\nEnter your choice: ")

if choice == "1":
    console.log("User selected!")
    spinner = Spinner("dots")
    with console.status("[bold green]Opening user interface...[/bold green]"):
        sleep(3)
    console.log("User interface successfully opened!")
    UsrLoginWindow()
    app.exec()
elif choice == "2":
    # Add code for admin functionality
    pass
elif choice == "3":
    helps = Markdown("# Pro Shop\n\n## Help\n\n1. User\n\n- To login as a user, select 1 and enter your credentials.\n- If you don't have an account, you can register.\n\n2. Admin\n\n- To login as an admin, select 2 and enter your credentials.\n- admin default password is admin and username is admin.\n\n3. Help\n\n- To view this help message, select 3.")
    console.print(helps)
else:
    console.print("Invalid choice. Please try again.")
