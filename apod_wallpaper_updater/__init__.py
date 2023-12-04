"""Top-level package for APOD Wallpaper."""

__author__ = """Kestin Goforth"""
__email__ = "kgoforth1503@gmail.com"
__version__ = "0.1.0"

import json
import os
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from tempfile import NamedTemporaryFile

from notifypy import Notify

from apod_wallpaper_updater.wallpaper import set_wallpaper

URL_PATH = "https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date:%Y-%m-%d}"
DATE_FMT = "%Y-%m-%d"
API_KEY = "DEMO_KEY"


@dataclass
class ApodImg:
    """A class to represent a NASA APOD image reposnse"""

    copyright: str = ""
    """The name of the copyright holder"""
    date: str = ""
    """The date of the APOD image"""
    explanation: str = ""
    """The supplied text explanation of the image"""
    hdurl: str = ""
    """The URL the high-resolution image"""
    media_type: str = ""
    """The type of media returned ('image' or 'video')"""
    service_version: str = ""
    """The service version used"""
    title: str = ""
    """The title of the image"""
    url: str = ""
    """The URL the low-resolution image"""

    @property
    def file_ext(self) -> str:
        """The file extension of the img"""
        return os.path.splitext(self.hdurl or self.url)[-1]

    def __str__(self) -> str:
        return f"ApodImg:{self.date}"


def get_apod_img(
    api_key: str = API_KEY, date: (datetime | None) = None
) -> ApodImg | None:
    """Get the URL for the latest APOD.

    Args:
        api_key (str): NASA OpenAPI Key

    Returns:
        str: Image URL
    """
    resp = urllib.request.urlopen(
        URL_PATH.format(api_key=api_key, date=date or datetime.today())
    )
    if resp.status != 200:
        raise ConnectionError(f"Unable to load NASA APOD, {resp.status} {resp.reason}")

    return ApodImg(**json.loads(resp.read().decode()))


def download_img(img: ApodImg) -> str:
    """Download the APOD to a temporary file

    Args:
        img (ApodImg): The APOD image to download

    Returns:
        str: Filepath of the downloaded APOD image
    """
    img_file = NamedTemporaryFile(mode="+w", suffix=img.file_ext)
    img_file.close()
    urllib.request.urlretrieve(img.hdurl or img.url, img_file.name)
    return img_file.name


def send_notification(message: str) -> None:
    """Send an OS notification with preconfigured settings and a specified message.

    Args:
        message (str): The notification message.
    """
    notification = Notify()
    notification.title = "NASA Astronomy Picture of the Day"
    notification.message = message
    notification.application_name = f"{__name__}.py"
    notification.send(block=False)


def update_apod_wallpaper(
    api_key: str = API_KEY, date: (datetime | None) = None, notify: bool = True
):
    """Set the desktop wallpaper to the specified APOD.

    Args:
        api_key (str): NASA OpenAPI Key
        date (datetime): The specific date image to use (default: today)
        notify (bool): If true, an OS notification will contain image information
    """
    try:
        img = get_apod_img(api_key, date)
    except urllib.error.HTTPError as ex:
        if notify:
            send_notification(ex)
        return False

    img_file = download_img(img)
    try:
        if not set_wallpaper(img_file):
            return False
    except (FileNotFoundError, NotImplementedError) as ex:
        if notify:
            send_notification(ex)
        return False

    if notify:
        send_notification(
            "\n".join(
                [
                    "Wallpaper Updated!",
                    img.title,
                    img.explanation,
                    f"Copyright (C) {img.copyright}",
                    img.date,
                ]
            )
        )

    return True
