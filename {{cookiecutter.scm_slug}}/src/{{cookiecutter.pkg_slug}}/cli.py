# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "loguru",
#     "typer",
# ]
# ///
import sys

import typer
from loguru import logger
from typing_extensions import Annotated 

LOG_LEVELS = ["WARNING", "INFO", "DEBUG", "TRACE"]

app = typer.Typer()

@app.command()
def main(
    verbose: Annotated[int, typer.Option("--verbose", "-v", count=True, max=3, clamp=True)] = 0,
    quite: Annotated[bool, typer.Option("--quite", "-q", help="Suppress log messages")] = False,
    ) -> None:
  
    logger.remove(0)  # Remove default configuration
    
    if not quite:
        logger.add(
            sys.stderr,
            format="<level>{level: <8}</level> | <level>{message}</level>",
            level=LOG_LEVELS[verbose], 
            backtrace=False, 
            diagnose=True
            )
    
    exit_code = 0

    try:
        print("Hello World from {{cookiecutter.pkg_slug}}!")
    
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt Received")
    
    except Exception as err:
        exit_code = 1
        logger.opt(exception=sys.exc_info()).critical(f"Unhandled Exception")
        
    finally:
        logger.info("Finally block - Exiting program")
        sys.exit(exit_code) # Set exit code for shell tests.
