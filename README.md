# Astronomy Picture of the Day (APOD) Wallpaper Updater

Automatically update your desktop wallpaper to the NASA Astronomy Picture of the Day.

## Usage

`apod_wallpaper_updater [OPTIONS]`

### Options
| Short | Long | Type | Default | Help |
|:------|:-----|:-----|:--------|:-----|
| -k    | --api-key | string | DEMO_KEY | NASA OpenAPI Key. (See https://api.nasa.gov/) |
| -d    | --date | %Y-%m-%d | Today | Specify a date to retrieve. |
| -n    | --notify | | false | Show a notification with information about the image. |
|       | --help | | | Show the help message and exit. |

## Setup

### Windows Task Scheduler

Follow these steps to set up a daily task to update your wallpaper to the current APOD.

1. Download the latest `APOD-Wallpaper-Updater.exe` and `APOD-Windows-Task.xml` from [GitHub](https://github.com/kForth/APOD-Wallpaper-Updater/releases/latest), saving them to `C:\Program Files\APOD-Wallpaper-Updater`
2. Open `Task Scheduler`
3. Select `Import Task...`
   1. Open `APOD-Windows-Task.xml`
   2. Update the `Name` and `Description` if desired
   3. Click `OK`
4. (Optional) Right-Click the newly-created task and select `Run`
5. (Optional) By default, the `DEMO_KEY` api key is used but you can change this by setting an `NASA_OPENAPI_KEY` environment variable. See [api.nasa.gov/](https://api.nasa.gov/) for information about getting your own key to remove certain restrictions.
6. You're done! Your wallpaper should now update every morning to the latest NASA APOD.

## Running from source

1. Clone this repository:

    ```
    git clone https://github.com/kForth/APOD-Wallpaper-Updater.git
    cd APOD-Wallpaper-Updater
    ```

2. Setup a virtualenv:

    ```
    python -m virtualenv venv
    venv/Scripts/activate # Windows
    ```

3. Install the module:

    ```
    python -m pip install -e .
    ```

3. Test it out:

    ```
    python -m apod_wallpaper_udpater --help
    ```

4. Done.


## Compiling

### Windows - PyInstaller

To create the distributable windows `.exe`, use PyInstaller and the provided spec:

```
pyinstaller windows/APOD-Wallpaper-Updater.spec
```
