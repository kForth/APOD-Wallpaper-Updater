"""Console script for apod_wallpaper_updater."""
import sys
from datetime import datetime

import click

from apod_wallpaper_updater import API_KEY, DATE_FMT, update_apod_wallpaper


@click.command(
    help="Update the desktop wallpaper to the current NASA Astronomy Picture of the Day."
)
@click.option(
    "-k",
    "--api-key",
    "api_key",
    default=API_KEY,
    show_default=True,
    help="NASA OpenAPI Key. (See https://api.nasa.gov/)",
)
@click.option(
    "-d",
    "--date",
    default=datetime.today().strftime(DATE_FMT),
    show_default=True,
    type=click.DateTime(formats=(DATE_FMT,)),
    help="Specify a specific date to retrieve.",
)
@click.option(
    "-n",
    "--notify",
    is_flag=True,
    default=False,
    show_default=True,
    help="Show a notification with information about the image.",
)
def main(api_key: str, date: datetime, notify: bool):
    update_apod_wallpaper(api_key, date, notify)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
