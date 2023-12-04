# Astronomy Picture of the Day (APOD) Wallpaper Updater

Automatically update your desktop wallpaper to a NASA Astronomy Picture of the Day.


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
5. You're done! Your wallpaper should now update every morning to the latest NASA APOD.
