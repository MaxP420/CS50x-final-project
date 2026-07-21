# Synthetic Data Generation for Automated YOLO Model Training for Formula Student

## Video Demo
<!-- Füge hier deinen Demo-Link ein -->


## Description

This project provides an automated pipeline for generating large amounts of synthetic data for training a YOLO computer vision model.

It focuses on simulating kart-racing scenes with street cones in various conditions to create diverse and realistic training data. The generated dataset is intended for the YOLO-based perception system used in the autonomous driving stack of the **Strohm und Söhne** Formula Student race car from Nuremberg.

The project uses **BlenderProc2**, a procedural Blender-based rendering pipeline developed by the German Aerospace Center, to create photorealistic synthetic imagery.

## Features

- Automated generation of synthetic training data.
- Photorealistic rendering with BlenderProc2.
- Support for cone detection in kart-racing scenarios.
- Designed for YOLO-based object detection training.
- Easy extension with additional assets and scene variations.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.10 or newer
- Git
- Blender
- pip
- Git LFS, if the repository uses large assets

## Project Structure

```bash
project-root/
├── Generator/          # Main generation scripts
├── assets/             # External asset files
│   ├── blend/
│   ├── jpg/
│   ├── png/
│   └── exr/
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Python dependencies

If your project contains a `requirements.txt` file, install the required Python packages with:

```bash
pip install -r requirements.txt
```

If no `requirements.txt` exists, install the missing dependencies manually as needed.

### 3. Install Blender

BlenderProc requires Blender to be installed on your system.

- Download Blender from the official website.
- Make sure Blender is available on your system path, or note the installation directory for later configuration.

### 4. Install BlenderProc

You can install BlenderProc in two ways.

#### Option A: Install via pip

```bash
pip install blenderproc
```

#### Option B: Install from source

```bash
git clone https://github.com/DLR-RM/BlenderProc
cd BlenderProc
pip install -e .
```

This installs BlenderProc in editable mode so that the `blenderproc` command can be used from anywhere on your system.

### 5. Download the assets folder

The project requires a separate `assets` folder containing the necessary 3D models, textures, and image resources.

- Download the assets folder separately.
- Place it in the root directory of the project.
- The folder structure must look like this:

```bash
project-root/
├── Generator/
├── assets/
│   ├── blend/
│   ├── jpg/
│   ├── png/
│   └── exr/
```

If the repository uses Git LFS, make sure the assets are pulled correctly after cloning:

```bash
git lfs install
git lfs pull
```

## Usage

1. Make sure the `assets` folder is placed correctly in the project root.
2. Open the `Generator` folder.
3. Run the main generation script.
4. Adjust configuration settings such as output path, scene parameters, and dataset size if needed.

Example:

```bash
python main.py
```

If your entry file has a different name, replace `main.py` with the correct script.

## Configuration

Depending on your setup, you may need to configure:

- The path to Blender or BlenderProc.
- Input and output directories.
- Scene parameters.
- The number of generated samples.
- Asset paths inside the project.

## Notes

- The assets folder is not stored directly in the repository because of its size.
- Make sure the folder is named exactly `assets`.
- If BlenderProc or Blender is not found, check your installation and system path.
- Depending on your system, you may need to adjust file paths in the configuration.

## Troubleshooting

### BlenderProc command not found

Make sure BlenderProc is installed correctly:

```bash
pip install -e .
```

### Assets missing

Verify that the `assets` folder is located in the project root and contains the required subfolders.

### Permission errors

Run the terminal or shell with the required permissions, or install packages in a virtual environment.

## License

<!-- Add your license here -->
Specify the license for your project here.

## Contact

<!-- Add your contact information here -->
For questions or contributions, contact the project maintainer.
