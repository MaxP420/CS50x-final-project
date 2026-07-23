import blenderproc as bproc
import bpy
import numpy as np
import random
from pathlib import Path


bproc.init()


def Object_count_calculator(Cones, total_cones, config):
    # Calc the count of normal cones. Skip Knocked Cones 
    for cone in Cones:
        if cone["appearance"] == False:
            cone["count"] = 0
        elif cone["knocked"] == True:
            continue 
        else:
            cone["count"] = round(total_cones * cone["appearance_percentage"] / 100)
    

    # Calc the knocked over cones and subtract them from the total count of the normal cones 
    for cone in Cones: 
        if cone["knocked"] == True:
            if cone["name"] == "yellow_cone_knocked_over":
                cone["count"] = round(Cones[2]["count"] * cone["appearance_percentage"] / 100)
                Cones[2]["count"] -= cone["count"]
            elif cone["name"] == "blue_cone_knocked_over":
                cone["count"] = round(Cones[0]["count"] * cone["appearance_percentage"] / 100)
                Cones[0]["count"] -= cone["count"]
            elif cone["name"] == "orange_cone_knocked_over":
                cone["count"] = round(Cones[1]["count"] * cone["appearance_percentage"] / 100)
                Cones[1]["count"] -= cone["count"]


    # Calc numbers of distractor types and number of distractors per type 
    config["number_of_distractortypes"] = random.randint(config["MinNumber_of_distractor_Types"], config["MaxNumber_of_distractor_Types"])
    config["number_of_distractors"] = random.randint(config["MinNumber_of_distractors_of_Type"], config["MaxNumber_of_distractors_of_Type"])


def Innit_Base_Scene(Tribuene_path, Zaun_path, Baeume_path):
    Tribuene = bproc.loader.load_blend(Tribuene_path)
    Zaun = bproc.loader.load_blend(Zaun_path)
    Baeume = bproc.loader.load_blend(Baeume_path)
    

def get_configs():
    script_dir = Path(__file__).parent
    generator_dir = script_dir.parent

    Config = {
        # Choose a range of number of cones to include in the scene and whether to include damaged or knocked over cones
        "Include_blue": True, 
        "appearance_blue": 33,
        "Include_orange": True, 
        "appearance_orange": 33,
        "Include_yellow": True,
        "appearance_yellow": 33, 


        "MinNumber_of_cones": 10,
        "MaxNumber_of_cones": 15,
        "Include_Knocked_Over_Cones": True,
        "appearance_percentage_of_knocked_over_cones": 50, #in percent 

        #Distractors
        "MinNumber_of_distractor_Types": 2, # How many different types of distractors to include in the scene
        "MaxNumber_of_distractor_Types": 3,
        "MinNumber_of_distractors_of_Type": 2, # Number of distractors of each type to include in the scene
        "MaxNumber_of_distractors_of_Type": 3,
        "number_of_distractors": 0,
        "number_of_distractortypes": 0,

        # Placement Bounds or Objects
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,

        #Lighting. Choose which lighting conditions to include in the scene. If All_Lightings is selected a randome lighting condition will be choosen
        "All_lightings": True,
        "BadWeather":  False,
        "Daylight": False,
        "Sunset": False,
        "Sunrise": False,
        "Nighttime": False,

        #Artefacts. Choose whether to apply motion blur and/or distortion to the final pictures
        "MotionBlur": False,
        "Distortion": False,

        #Number of images to generate. Choose how many Numbers of scenes to generate and how many pictures per scene to generate. If YOLO_Annotation is set to True, the script will also generate YOLO annotations for each image
        "Number_of_Camera_Poses": 1,
        "YOLO_Annotation": True,

        #Set Camera Resolution x,y and an output directory 
        "CameraResX": 640,
        "CameraResY": 640,
        "Output_path": str(generator_dir / "output")
    }
    return Config


def Select_Street(config, Streets, WetStreets):
    if config["BadWeather"]:
        street_path = random.choice(WetStreets)
    else:
        street_path = random.choice(Streets)

    Street = bproc.loader.load_blend(street_path)


def Select_HDRI(config, Daylight_HDRIs, Sunset_HDRIs, Sunrise_HDRIs, Nighttime_HDRIs, Cloudy_HDRIs):
    # Reset lighting flags before choosing a new environment.
    config["Daylight"] = False
    config["Sunset"] = False
    config["Sunrise"] = False
    config["Nighttime"] = False
    config["BadWeather"] = False

    if config["All_lightings"]:
        lighting_choice = random.choice(["Daylight", "Sunset", "Sunrise", "Nighttime", "Cloudy"])
   

    if lighting_choice == "Daylight":
        config["Daylight"] = True
        selected_hdri = random.choice(Daylight_HDRIs)
        bproc.world.set_world_background_hdr_img(selected_hdri)
        light = bproc.types.Light()
        light.set_type("POINT")
        light.set_location([4.076, 1, 6])
        light.set_energy(1000)
    elif lighting_choice == "Sunset":
        config["Sunset"] = True
        selected_hdri = random.choice(Sunset_HDRIs)
        bproc.world.set_world_background_hdr_img(selected_hdri)
        light = bproc.types.Light()
        light.set_type("POINT")
        light.set_location([6.0, -3.0, 1.8])
        light.set_energy(500)
        light.set_color([1.0, 0.42, 0.22])
    elif lighting_choice == "Sunrise":
        config["Sunrise"] = True
        selected_hdri = random.choice(Sunrise_HDRIs)
        bproc.world.set_world_background_hdr_img(selected_hdri)
        light = bproc.types.Light()
        light.set_type("POINT")
        light.set_location([-6.0, -2.0, 2.5])
        light.set_energy(350)
        light.set_color([1.0, 0.58, 0.32])
    elif lighting_choice == "Nighttime":
        config["Nighttime"] = True
        selected_hdri = random.choice(Nighttime_HDRIs)
        bproc.world.set_world_background_hdr_img(selected_hdri)
        light = bproc.types.Light()
        light.set_type("POINT")
        light.set_location([2.0, -1.0, 8.0])
        light.set_energy(35)
        light.set_color([0.55, 0.65, 1.0])
    else:
        config["BadWeather"] = True
        selected_hdri = random.choice(Cloudy_HDRIs)
        bproc.world.set_world_background_hdr_img(selected_hdri)

    print(f"{selected_hdri}")


def set_category_ids(Cones):
    #Loop through the Cones and set the category_id and supercategory, requiered for correct annotations
    for cone in Cones:
        cone["obj"].set_name(cone["name"])
        cone["obj"].set_cp("category_id", cone["category_id"])
        cone["obj"].set_cp("supercategory", cone["supercategory"])


    for obj in bproc.object.get_all_mesh_objects():
        if obj not in [cone["obj"] for cone in Cones]:
            obj.set_cp("category_id", 0)
            obj.set_cp("supercategory", "background")


def select_distractors(distractors_all, config, distractors_in_scene):
    # Choose a random number of distractor types to include in the scene
    selected_distractor_types = random.sample(distractors_all, config["number_of_distractortypes"])
    

    for distractor in selected_distractor_types:
        # Choose a random number of distractors of this type to include in the scene
        for _ in range(config["number_of_distractors"]):
            distractor_obj = bproc.loader.load_blend(distractor["path"])[0]
            distractor_obj.set_location([0,0,-5])  # Random location
            distractors_in_scene.append(distractor_obj)


def place_objects(Cones, distractors_in_scene, config):
    # z placement bounds
    z_value = 0
    z_Knocked = 0.106


    for cone in Cones:
        cone_name = cone["name"]
        if cone_name == "blue_cone_knocked_over" or cone_name == "orange_cone_knocked_over" or cone_name == "yellow_cone_knocked_over" and not config["Include_Knocked_Over_Cones"]:
            continue
        count = cone["count"]
        for i in range(count):
            # Duplicate the cone 
            cone_duplicate = cone["obj"].duplicate()
            cone_duplicate.set_cp("category_id", cone["category_id"])
            cone_duplicate.set_cp("supercategory", cone["supercategory"])
            cone_duplicate.set_name(cone["name"])
            
            #Calculate Random x and y within bounds 
            x = np.random.uniform(config["x_min"], config["x_max"])
            y = np.random.uniform(config["y_min"], config["y_max"])
            #Place Knocked Over Cones with a different height and random z rotation
            if cone_name == "blue_cone_knocked_over" or cone_name == "orange_cone_knocked_over" or cone_name == "yellow_cone_knocked_over":
                cone_duplicate.set_rotation_euler([1.8812272548675537, 4.155973343245023e-10, np.random.uniform(0, 2 * np.pi)])
                cone_duplicate.set_location([x, y, z_Knocked])
            else:
                cone_duplicate.set_location([x, y, z_value])
                cone_duplicate.set_rotation_euler([0, 0, np.random.uniform(0, 2 * np.pi)])

    
    for distractors in distractors_in_scene:
        for i in range(config["number_of_distractors"]):
            # Duplicate the distractor
            distractor_duplicate = distractors.duplicate()
            
            # Randomize placement within bounds
            x = np.random.uniform(config["x_min"], config["x_max"])
            y = np.random.uniform(config["y_min"], config["y_max"])
            distractor_duplicate.set_location([x, y, z_value])


def setup_camera_render(config):
    #Add Lens Distortion
    #Set Random K1 and K2 Values
    # Kameraprofile (simuliert verschiedene Dashcam-Typen)
    camera_profiles = [
        {"name": "Weitwinkel",   "k1": -0.28, "k2":  0.10},
        {"name": "Standard",     "k1": -0.15, "k2":  0.05},
        {"name": "Leicht verz.", "k1": -0.05, "k2":  0.01},
        {"name": "Kein Effekt",  "k1":  0.00, "k2":  0.00},
    ]

    #Kamera platzieren 
    #POI Random setzen 
    #Set Resolution

    for i in range(config["Number_of_Camera_Poses"]):
        if config["Distortion"]:
            profile = random.choice(camera_profiles)
            # Kameramatrix (Brennweite + Hauptpunkt)
            orig_res_x, orig_res_y = config["CameraResX"], config["CameraResY"]
            cam_K = np.array([[349.554, 0.0, 336.84], [0.0, 349.554, 189.185], [0.0, 0.0, 1.0]])
            p1, p2 = 0.000311976, -9.62967e-5
            bproc.camera.set_intrinsics_from_K_matrix(cam_K, orig_res_x, orig_res_y, bpy.context.scene.camera.data.clip_start, bpy.context.scene.camera.data.clip_end)
            mapping_coords = bproc.camera.set_lens_distortion(profile["k1"], profile["k2"], 0.0, p1, p2)

        else:
            bproc.camera.set_resolution(config["CameraResX"], config["CameraResY"])
        
        poi = np.random.uniform([-10, -10, 0], [10, 10, 0])  # Random POI innerhalb des Platzierungsrahmens 
        # Sample random camera location above objects in a circle around the POI
        location = np.random.uniform([-15, -15, 1], [15, 15, 2])
        # Compute rotation based on vector going from location towards poi
        rotation_matrix = bproc.camera.rotation_from_forward_vec(poi - location, inplane_rot=np.random.uniform(0,0))
        # Add homog cam pose based on location an rotation
        cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)
        bproc.camera.add_camera_pose(cam2world_matrix)


    #Rendern
    # 6. Aktiviere Normals 
    bproc.renderer.enable_normals_output()
    bproc.renderer.enable_distance_output(activate_antialiasing=True)

    if config["MotionBlur"]:
        bproc.renderer.enable_motion_blur(
        motion_blur_length=0.3,
        rolling_shutter_type="TOP",
        rolling_shutter_length=0.03
        )
        bproc.renderer.enable_depth_output(activate_antialiasing=False)


    bproc.renderer.enable_segmentation_output(map_by=["category_id", "instance", "name"])
    data = bproc.renderer.render()
    #bproc.writer.write_hdf5("output/", data)


    if config["Distortion"]:
        #Post process the data and apply the lens distortion
        # post process the data and apply the lens distortion
        for key in ['colors', 'distance', 'normals']:
            # use_interpolation should be false, for everything except colors
            use_interpolation = key == "colors"
            data[key] = bproc.postprocessing.apply_lens_distortion(data[key], mapping_coords, orig_res_x, orig_res_y, use_interpolation=use_interpolation)



    output_dir = Path(config["Output_path"])
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create bounding boxes for each cone with its respective lable 
    bproc.writer.write_coco_annotations(str(output_dir),    # subdic coco_data
        instance_segmaps=data["instance_segmaps"],
        instance_attribute_maps=data["instance_attribute_maps"],
        colors=data["colors"],
        color_file_format="JPEG",
    )


def main():
    config = get_configs() 
    
    
    # Setup relative paths - works on any computer
    script_dir = Path(__file__).parent  # scripts/
    generator_dir = script_dir.parent    # Generator/
    assets_dir = generator_dir / "assets"  # Generator/assets/


    #Paths
    # Path to the assets

    #FSF
    orange_cone_path = str(assets_dir / "Cones" / "smallRedCone.blend") #FSF full orange cone
    yellow_cone_path = str(assets_dir / "Cones" / "smallFullYellowCone.blend") #FSF Full Yellow
    blue_cone_path = str(assets_dir / "Cones" / "smallFullBlueCone.blend") #FSF full blue cone 


    #FSF damaged/imperfect
    blue_cone_damaged_path = str(assets_dir / "Cones" / "Damaged Cones" / "blue_cone_damaged.blend")
    yellow_cone_damaged_path = str(assets_dir / "Cones" / "Damaged Cones" / "smallFullYellowConeDamaged.blend")
    orange_cone_damaged_path = str(assets_dir / "Cones" / "Damaged Cones" / "smallRedConeDamaged.blend")


    #FSF Knocked OverCone ? 
    blue_knocked_over_cone_path = str(assets_dir / "Cones" / "BlueKnockedOverCone.blend")
    yellow_knocked_over_cone_path = str(assets_dir / "Cones" / "YellowKnockedOverCone.blend")
    orange_knocked_over_cone_path = str(assets_dir / "Cones" / "RedKnockedOverCone.blend")
    Cones = [blue_cone_path, orange_cone_path, yellow_cone_path, blue_cone_damaged_path, yellow_cone_damaged_path, orange_cone_damaged_path, blue_knocked_over_cone_path, yellow_knocked_over_cone_path, orange_knocked_over_cone_path]


    #Base Scene Objects
    Zaun_path = str(assets_dir / "Environment Elements" / "RoadBarrierInnit.blend")
    Baeume_path = str(assets_dir / "Environment Elements" / "TreelineInnit.blend")
    Tribuene_path = str(assets_dir / "Environment Elements" / "GroßeTribueneInnit.blend")


    #Straßentypen Normal
    PlainAspahlt_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "NormalAsphalt.blend")
    floorPattern_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "FloorPattern.blend")
    plaster_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "Plaster.blend")
    groundGrey_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "GroundGrey.blend")


    #Straßentypen Nass
    PlainAsphalt_wet_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "NormalAsphaltWet.blend")
    floorPattern_wet_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "FloorPatternWet.blend")
    plaster_wet_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "PlasterWet.blend")
    groundGrey_wet_path = str(assets_dir / "Environment Elements" / "Ground Textures" / "GroundGreyWet.blend")


    Streets = [PlainAspahlt_path, floorPattern_path, plaster_path, groundGrey_path]
    WetStreets = [PlainAsphalt_wet_path, floorPattern_wet_path, plaster_wet_path, groundGrey_wet_path]


    #Distractors
    smallSensor_path = str(assets_dir / "distractors" / "smallSensor.blend")
    redPropaneTank_path = str(assets_dir / "distractors" / "RedPropaneTank.blend")
    constructionLight_path = str(assets_dir / "distractors" / "ConstructionLight.blend")
    fireExtinguisher_path = str(assets_dir / "distractors" / "FireExtinguisher.blend")
    cardboardBox_path = str(assets_dir / "distractors" / "CardboardBox.blend")
    barrelStove_path = str(assets_dir / "distractors" / "BarrelStove.blend")
    barell_path = str(assets_dir / "distractors" / "Barrel.blend")
    redJerryCan_path = str(assets_dir / "distractors" / "RedJerryCan.blend")
    Chair_path = str(assets_dir / "distractors" / "Chair.blend")
    TrashCan_path = str(assets_dir / "distractors" / "TrashCan.blend")

    Distractors = [smallSensor_path, redPropaneTank_path, constructionLight_path, fireExtinguisher_path, cardboardBox_path, barrelStove_path, barell_path, redJerryCan_path, Chair_path, TrashCan_path]


    #HDRIs
    #Daylight 
    driving_school_path = str(assets_dir / "hdri" / "Daylight" / "driving_school_4k.exr")
    mallParkingLot_path = str(assets_dir / "hdri" / "Daylight" / "mall_parking_lot_4k.exr")
    racetrack_path = str(assets_dir / "hdri" / "zwartkops_curve_sunset_4k.exr")


    #Sunset
    belfast_sunset_path = str(assets_dir / "hdri" / "Sunset" / "belfast_sunset_4k.exr")
    bambanani_sunset_path = str(assets_dir / "hdri" / "Sunset" / "bambanani_sunset_4k.exr")


    #Sunrise
    spruit_sunrise_path = str(assets_dir / "hdri" / "Sunrise" / "spruit_sunrise_4k.exr")


    #Nighttime
    sandsloot_path = str(assets_dir / "hdri" / "Nighttime" / "sandsloot_4k.exr")


    #Cloudy (For Bad Weather)
    shudu_lake = str(assets_dir / "hdri" / "Cloudy" / "shudu_lake_4k.exr")
    airfield = str(assets_dir / "hdri" / "Cloudy" / "hanger_exterior_cloudy_4k.exr")

    Daylight_HDRIs = [driving_school_path, mallParkingLot_path, racetrack_path]
    Sunset_HDRIs = [belfast_sunset_path, bambanani_sunset_path]
    Sunrise_HDRIs = [spruit_sunrise_path]
    Nighttime_HDRIs = [sandsloot_path]
    Cloudy_HDRIs = [shudu_lake, airfield]
    HDRIs = Daylight_HDRIs + Sunset_HDRIs + Sunrise_HDRIs + Nighttime_HDRIs + Cloudy_HDRIs

    # Cone List Definitions with custom properties and innit objects
    BlueCone = bproc.loader.load_blend(blue_cone_path)
    blue_cone = BlueCone[0]
    blue_cone.set_location([0,0,-5])

    OrangeCone = bproc.loader.load_blend(orange_cone_path)
    orange_cone = OrangeCone[0]
    orange_cone.set_location([0,0,-5])

    YellowCone = bproc.loader.load_blend(yellow_cone_path)
    yellow_cone = YellowCone[0]
    yellow_cone.set_location([0,0,-5])

    BlueKnockedOverCone = bproc.loader.load_blend(blue_knocked_over_cone_path)
    blue_knocked_over_cone = BlueKnockedOverCone[0]
    blue_knocked_over_cone.set_location([0,0,-5])

    OrangeKnockedOverCone = bproc.loader.load_blend(orange_knocked_over_cone_path)
    orange_knocked_over_cone = OrangeKnockedOverCone[0]
    orange_knocked_over_cone.set_location([0,0,-5])

    YellowKnockedOverCone = bproc.loader.load_blend(yellow_knocked_over_cone_path)
    yellow_knocked_over_cone = YellowKnockedOverCone[0]
    yellow_knocked_over_cone.set_location([0,0,-5])

    # Choose which cones to inlcude in the scene and their appearance percentage
    Cones = [
        {"name": "blue_cone", "appearance_percentage": config["appearance_blue"], "count": 0, "path": blue_cone_path, "appearance": config["Include_blue"], "knocked": False, "obj": blue_cone, "category_id": 1, "supercategory": "cone"},
        {"name": "orange_cone", "appearance_percentage": config["appearance_orange"], "count": 0, "path": orange_cone_path, "appearance": config["Include_orange"], "knocked": False, "obj": orange_cone, "category_id": 2, "supercategory": "cone"},
        {"name": "yellow_cone", "appearance_percentage": config["appearance_yellow"], "count": 0, "path": yellow_cone_path, "appearance": config["Include_yellow"], "knocked": False, "obj": yellow_cone, "category_id": 3, "supercategory": "cone"},
        {"name": "yellow_cone_knocked_over", "appearance_percentage": config["appearance_percentage_of_knocked_over_cones"], "count": 0, "path": yellow_knocked_over_cone_path, "appearance": config["Include_Knocked_Over_Cones"], "knocked": True, "obj": yellow_knocked_over_cone, "category_id": 4, "supercategory": "cone"},
        {"name": "blue_cone_knocked_over", "appearance_percentage": config["appearance_percentage_of_knocked_over_cones"], "count": 0, "path": blue_knocked_over_cone_path, "appearance": config["Include_Knocked_Over_Cones"], "knocked": True, "obj": blue_knocked_over_cone, "category_id": 5, "supercategory": "cone"},
        {"name": "orange_cone_knocked_over", "appearance_percentage": config["appearance_percentage_of_knocked_over_cones"], "count": 0, "path": orange_knocked_over_cone_path, "appearance": config["Include_Knocked_Over_Cones"], "knocked": True, "obj": orange_knocked_over_cone, "category_id": 6, "supercategory": "cone"}
    ]

    # Distractor List Definitions
    distractors_all = [
        {
            "path": smallSensor_path,
            "name": "small_sensor"
        },
        {
            "path": redPropaneTank_path,
            "name": "red_propane_tank"
        },
        {
            "path": constructionLight_path,
            "name": "construction_light"
        },
        {
            "path": fireExtinguisher_path,
            "name": "fire_extinguisher"
        },
        {
            "path": cardboardBox_path,
            "name": "cardboard_box"
        },
        {
            "path": barrelStove_path,
            "name": "barrel_stove"
        },
        {
            "path": barell_path,
            "name": "barrel"
        },
        {
            "path": redJerryCan_path,
            "name": "red_jerry_can"
        },
        {
            "path": Chair_path,
            "name": "chair"
        },
        {
            "path": TrashCan_path,
            "name": "trash_can"
        },
    ]

    distractors_in_scene = []  # List to hold the distractors that will be included in the scene

    # Resets the Scene
    bproc.utility.reset_keyframes()

    # Calc the total number of cones and pass it to the Object calculator to Calculate the individual numbers of cones
    total_cones = random.randint(config["MinNumber_of_cones"], config["MaxNumber_of_cones"])
    Object_count_calculator(Cones, total_cones, config)
    Select_HDRI(config, Daylight_HDRIs, Sunset_HDRIs, Sunrise_HDRIs, Nighttime_HDRIs, Cloudy_HDRIs)
    Select_Street(config, Streets, WetStreets)
    Innit_Base_Scene(Tribuene_path, Zaun_path, Baeume_path)
    select_distractors(distractors_all, config, distractors_in_scene)
    set_category_ids(Cones)
    place_objects(Cones, distractors_in_scene, config)
    setup_camera_render(config)


















    # BlueCone = bproc.loader.load_blend(blue_cone_path)
    # blue_cone = BlueCone[0]
    # blue_cone.set_location([0, 0, 0])



    # # Set the camera to be in front of the object
    # cam_pose = bproc.math.build_transformation_mat([2.0716500282287598, -1.9419399499893188, 1.3450347185134888], [1.1093189716339111, 4.011331711240018e-09, 0.8149281740188599])
    # bproc.camera.add_camera_pose(cam_pose)


    # # Render the scene
    # data = bproc.renderer.render()

    # # Write the rendering into an hdf5 file
    # bproc.writer.write_hdf5("output/", data)
    # print(f"total_cones: {total_cones}")
    # for cones in Cones:
    #     print(f"{cones['name']} appears: {cones['count']} times")


if __name__ == "__main__":
    main()































































