# Synthetic Data Generation for Automated YOLO Model Training for Formula Student

## Video Demo
<!-- Füge hier deinen Demo-Link ein -->


## Description

This project provides an automated pipeline for generating large amounts of synthetic data for training a YOLO computer vision model.

It focuses on simulating kart-racing scenes with street cones in various conditions to create diverse and realistic training data. The data is used for the traing of a YOLO-based perception system used in the autonomous driving system of the **Strohm und Söhne** Formula Student race car from Nuremberg.

The project uses **BlenderProc2**, a procedural Blender-based rendering pipeline developed by the German Aerospace Center, to create photorealistic synthetic imagery.

## Features

- Automated generation of synthetic training data.
- Photorealistic rendering with BlenderProc2.
- Automated generation of bounding boxes and conversion to YOLO-annotation format. 

## Requirements

Before running the project, make sure you have the following installed:

- Git LFS, if the repository uses large assets

## Project Structure

```bash
project-root/
├── Generator/          # Main generation scripts
├── assets/             # External asset files
│   ├── cone Textures/
│   ├── cones/
│   ├── distractor textures/
│   └── distractor objects/
│   ├── environment elements/
│   ├── environment elements textures/
│   ├── hdri´s/
├── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install BlenderProc

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

The `blenderproc` command can now be used from anywhere on your system.

## Usage

1. Make sure the `assets` folder is placed correctly in the Generator folder.
2. Open the `Generator` folder.
3. Run the main.py generation script with ```blenderproc run scripts/main.py ```
4. Adjust configuration settings such as scene parameters in main.py ´s ```get_config function```, and dataset size if needed.

If your entry file has a different name, replace `main.py` with the correct script.

## Configuration

Set configurations in the `get_configs` function in main.py 

- Lighting Conditions (Daytime, Nightime, Rain) 
- Motion Blur / Camera Distortion
- Which Objects to include and their amounts
- Placement bounds for objects and camera on the surface 
- Number of camera poses per scene (pictures per scene) and amount of scenes to render
- Camera resolution 

## Notes

- The assets folder is downloaded via LFS Git

## Troubleshooting

### BlenderProc command not found

Make sure BlenderProc is installed correctly:

```bash
pip install -e .
```

### Assets missing

Verify that the `assets` folder is located in the project root and contains the required subfolders.


## Citation

@article{Denninger2023, 
- doi = {10.21105/joss.04901},
- url = {https://doi.org/10.21105/joss.04901},
- year = {2023},
- publisher = {The Open Journal}, 
- volume = {8},
- number = {82},
- pages = {4901}, 
- author = {Maximilian Denninger and Dominik Winkelbauer and Martin Sundermeyer and Wout Boerdijk and Markus Knauer and      Klaus H. Strobl and Matthias Humt and Rudolph Triebel},
- title = {BlenderProc2: A Procedural Pipeline for Photorealistic Rendering}, 
- journal = {Journal of Open Source Software}
