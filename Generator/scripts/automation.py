import subprocess
import sys
import time
import paths

# ============================================================
#  Settings 
# ============================================================
RUNS = 100
WARTE_SEKUNDEN_CONVERTER = 5                               # Sekunden nach "Blender quit" bis Converter startet
STOP_SIGNAL              = "Cleaning temporary directory"  # Erkennungsstring im Terminal
# ============================================================


def run_generator():
    process = subprocess.Popen(
        ["blenderproc", "run", paths.BLENDER_SKRIPT], # tells the function how to run the script
        stdout=subprocess.PIPE,                       # stores all outputs in the PIPE to be able to read it line for line 
        stderr=subprocess.STDOUT,                     # Errors are stored in stderr
        text=True,                                    # Everything is stored as text
        bufsize=1                                     # Buffer line for line 
    )

    stop = False
    for line in process.stdout:                       # Read every line 
        if STOP_SIGNAL in line:                       # If Termination signal is detected set stop to true and wait
            stop = True
    process.wait()
    return stop

def run_converter():
    process = subprocess.Popen(
            [sys.executable, paths.CONVERTER_SCRIPT],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
    process.wait()
    

def main():
    print(f"Atomation startet - {RUNS} planned")
    print()
    for run in range(1, RUNS + 1):
        print(f"Run {run}")
        stop = run_generator()                        # Detect the termination line 
        time.sleep(WARTE_SEKUNDEN_CONVERTER)          # Wait shortly for to ensure all images loaded into the folder and the coco.json is updated before trying to convert


        if stop:
            run_converter()                           # Run the converter script to create a .txt file for each images with its annotations 
        




if __name__ == "__main__":
    main()