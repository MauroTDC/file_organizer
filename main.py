import os
import shutil
import sys

folders = {
    "Images": ["jpg", "jpeg", "apng", "png", "avif", "gif", "jfif", "pjpeg", "pjp", "svg", "webp", "bmp", "ico", "cur", "tif", "tiff"],
    "Videos": ["webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "mng", "avi", "mts", "m2ts", "ts", "mov", "qt", "wmv", "yuv", "rm", "rmvb", "viv", "asf", "amv", "mp4", "mpg", "mpv", "mpg", "mpeg", "3gp"],
    "Documents": ["pdf", "doc", "docx", "txt", "rtf", "odt", "html", "md", "tex", "xls", "xlsx", "csv", "ppt", "pptx", "odp", "epub", "mobi"]
}


def main():
    path = input("Enter the path to the folder you want to organize: ")
    if not os.path.isdir(path):
        sys.exit("The specified path was not found")
    organize_files(path)


def organize_files(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(
            os.path.join(folder_path, f))]

        for file in files:
            # Get the file extension
            extension = os.path.splitext(file)[1][1:].lower()
            moved = False

            for folder, extensions in folders.items():
                if extension in extensions:
                    destination_folder = os.path.join(folder_path, folder)
                    # Check if the new folder already exists
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)

                    shutil.move(os.path.join(folder_path, file),
                                os.path.join(folder_path, folder, file))
                    moved = True
                    break

            if not moved:
                # If file doesnt belong to any category, it moves to "Others"
                others_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)

                destination_file = os.path.join(others_folder, file)
                shutil.move(os.path.join(folder_path, file), destination_file)

        print("File organization completed")
    except FileNotFoundError:
        sys.exit("Directory not found")
    except PermissionError:
        print("Unable to access some files or folders.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
