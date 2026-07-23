# Synthetic Data Generation for Automated YOLO Model Training for Formula Student

## Video Demo
<!-- Füge hier deinen Demo-Link ein -->


## Description

This project provides an automated pipeline for generating large amounts of synthetic data for training a YOLO computer vision model.

It focuses on simulating kart-racing scenes with street cones in various conditions to create diverse and realistic training data. The data is used for the training of a YOLO-based perception system used in the autonomous driving system of the **Strohm und Söhne** Formula Student race car from Nuremberg.

The project uses **BlenderProc2**, a procedural Blender-based rendering pipeline developed by the German Aerospace Center, to create photorealistic synthetic imagery.

## Features

- Generation of synthetic training data.
- Photorealistic rendering with BlenderProc2.
- Automated generation of bounding boxes and conversion to YOLO-annotation format. 

## Requirements

Before running the project, make sure you have the following installed:

- Git LFS (the repository uses large assets)

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
2. Adjust configuration settings such as scene parameters and number of images per scene in main.py´s ```get_config function```
3. Set the number of runs in automation.py. Dataset size = runs * images_per_scene
4. Run the automation.py generation script with ```blenderproc run automation.py ```

## Configuration

Set configurations in the `get_configs` function in main.py and the number of runs in `automation.py`

- Lighting Conditions (Daytime, Sunrise, Sunset, Nighttime, Rain) 
- Motion Blur / Camera Distortion
- Which Objects to include and their appearance percentage
- Placement bounds for objects and camera on the surface 
- Number of pictures per scene
- Camera resolution 

## Troubleshooting

### BlenderProc command not found.

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
