# ListOnImg

A simple utility tool for overlaying text lists onto images.

## Description

ListOnImg takes a list of text items and renders them as centered text lines on a background image. The text is automatically spaced evenly across the image height.

## Requirements

- Python 3.12+
- uv (Python package manager)
- Pillow (PIL)

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Install uv first, then add the required dependencies:

```
uv add pillow
```

## Usage

1. Place your background image as `canvas.png` in the project directory
2. Edit the `items` list in `listonimg.py` with your desired text
3. Run the script:
   ```
   python listonimg.py
   ```
4. The result will be saved as `result.png`

## Features

- Automatic text centering
- Even vertical spacing
- Configurable text list
- Arial font at 32pt size

## Files

- `listonimg.py` - Main script
- `canvas.png` - Input background image (required)
- `result.png` - Output image with text overlay