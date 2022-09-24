import os
import zipfile


def main():
    # Unzip ReleasableAircraft.zip to the current directory.
    with zipfile.ZipFile("ReleasableAircraft.zip", "r") as zip_ref:
        zip_ref.extractall()
    # Delete ReleasableAircraft.zip.
    os.remove("ReleasableAircraft.zip")


if __name__ == '__main__':
    main()
