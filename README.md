# File Organizer Script

This Python script helps you organize files in a specified directory by categorizing them into different folders based on their extensions. The categories include Images, Videos, Documents, and Others.

## Features

- Automatically organizes files into predefined categories:
  - Images: jpg, jpeg, apng, png, avif, gif, jfif, pjpeg, pjp, svg, webp, bmp, ico, cur, tif, tiff
  - Videos: webm, mkv, flv, vob, ogv, ogg, drc, mng, avi, mts, m2ts, ts, mov, qt, wmv, yuv, rm, rmvb, viv, asf, amv, mp4, mpg, mpv, mpeg, 3gp
  - Documents: pdf, doc, docx, txt, rtf, odt, html, md, tex, xls, xlsx, csv, ppt, pptx, odp, epub, mobi
- Moves files that do not fit into these categories to an "Others" folder.
- Provides error messages for common issues like permission errors or invalid paths.

## Made with
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" />

## Requirements 

- Python 3.x
- Basic Python libraries (os, shutil, sys)

## Usage

1. Run the script
```bash
python file_organizer.py
```

2. Provide the Directory Path
```bash
Enter the path to the folder you want to organize: /path/to/your/folder
```

## Author

[MauroTDC](https://github.com/MauroTDC)
