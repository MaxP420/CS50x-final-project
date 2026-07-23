from pathlib import Path

# Basisverzeichnis: der Ordner, in dem paths.py liegt (scripts/),
# davon ausgehend eine Ebene hoch zum "Generator"-Ordner
SCRIPTS_DIR = Path(__file__).resolve().parent
GENERATOR_DIR = SCRIPTS_DIR.parent

ASSETS_DIR = GENERATOR_DIR / "assets"

CONES_DIR = ASSETS_DIR / "cones"
DAMAGED_CONES_DIR = CONES_DIR / "Damaged Cones"

DISTRACTORS_DIR = ASSETS_DIR / "distractors"
ENVIRONMENT_ELEMENTS_DIR = ASSETS_DIR / "Environment Elements"
HDRI_DIR = ASSETS_DIR / "hdri"

#Cones 
#Normal Cones 
BLUE_CONE_PATH = CONES_DIR / "smallBlueCone.blend"
YELLOW_CONE_PATH = CONES_DIR / "smallFullYellowCone.blend"
ORANGE_CONE_PATH = CONES_DIR / "smallRedCone.blend"

#Output
OUTPUT_DIR = GENERATOR_DIR / "output"
COCO_PATH = OUTPUT_DIR / "coco_annotations.json"
YOLO_LABELS_DIR = OUTPUT_DIR / "yolo_labels"

#Scripts
BLENDER_SKRIPT = SCRIPTS_DIR / "main.py"
#BLENDER_SKRIPT = BLENDER_SCRIPT
CONVERTER_SCRIPT = SCRIPTS_DIR / "CocoToYolo.py"
# script_dir = Path(__file__).parent
# generator_dir = script_dir.parent
# output_dir = generator_dir / "output"


#Knocked Over Cones


#Distractors

