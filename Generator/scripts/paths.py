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
OUTPUT_DIR = GENERATOR_DIR 


#Knocked Over Cones


#Distractors

