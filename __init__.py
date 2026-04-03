import os

class StringSelectorAspectRatio:
    @classmethod
    def INPUT_TYPES(cls):
        # Read strings from a text file
        file_path = os.path.join(os.path.dirname(__file__), "string_options.txt")
        
        # Default options if file doesn't exist
        default_options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        model_family_options = ["SDXL", "SD", "Voxta", "Other"]
        try:
            with open(file_path, 'r') as f:
                options = [line.strip() for line in f.readlines() if line.strip()]
                if not options:
                    options = default_options
        except FileNotFoundError:
            options = default_options
            # Create the file with defaults
            with open(file_path, 'w') as f:
                f.write('\n'.join(default_options))
        
        return {
            "required": {
                "string_choice": (options,),
                "model_family": (model_family_options,),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", ["1:1", "6:5", "5:4", "4:3", "3:2", "16:10", "16:9", "19:9", "21:9", "48:35", "43:18", "2:1", "3:1", "4:1"], ["landscape", "portrait"], "INT")  # Define valid options for the combo
    RETURN_NAMES = ("selected_string", "model_family", "aspect", "direction", "shortside")  # Names for the outputs
    FUNCTION = "select_string"
    CATEGORY = "DrTim"

    def select_string(self, string_choice, model_family):
        # Determine direction (portrait, landscape or square) based on selection
        if "Portrait" in string_choice:
            print("Portrait option selected")
            selected_orientation = "portrait"
            selected_aspect = "3:2"
            if "SDXL" in model_family:
                print("SDXL model family selected")
                selected_shortside = 832
            elif "SD" in model_family:
                print("SD model family selected")
                selected_shortside = 512
            else:
                print("Other model family selected")
                selected_shortside = 512

        elif "Landscape" in string_choice:
            print("Landscape option selected")
            selected_orientation = "landscape"
            selected_aspect = "3:2"
            selected_shortside = 512
        elif "Voxta" in string_choice:
            print("Voxta option selected")
            selected_orientation = "portrait"
            selected_aspect = "48:35"
            selected_shortside = 560
        else:
            print("Neither Portrait nor Landscape specified")
            selected_orientation = "landscape"  # Default to landscape if neither specified
            selected_aspect = "1:1"
            selected_shortside = 1024

        return (string_choice, model_family, selected_aspect, selected_orientation, selected_shortside)


class StringSelectorMistral:
    @classmethod
    def INPUT_TYPES(cls):
        # Read strings from a text file
        file_path = os.path.join(os.path.dirname(__file__), "string_options_mistral.txt")
        
        # Default options if file doesn't exist
        default_options = ["Option 1", "Option 2", "Option 3"]
        
        try:
            with open(file_path, 'r') as f:
                options = [line.strip() for line in f.readlines() if line.strip()]
                if not options:
                    options = default_options
        except FileNotFoundError:
            options = default_options
            # Create the file with defaults
            with open(file_path, 'w') as f:
                f.write('\n'.join(default_options))
        
        return {
            "required": {
                "string_choice": (options,),
            }
        }
    
    RETURN_TYPES = ("STRING",['pixtral-large-latest', 'pixtral-12b-latest', 'ministral-3b-latest', 'ministral-8b-latest', 'open-mistral-nemo', 'mistral-small-latest', 'mistral-large-latest'])
    RETURN_NAMES = ("selected_string","model")
    FUNCTION = "select_string"
    CATEGORY = "DrTim"

    def select_string(self, string_choice):
        model = "selected_string"
        return (string_choice,)


class StringSelectorOR:
    @classmethod
    def INPUT_TYPES(cls):
        # Read strings from a text file
        file_path = os.path.join(os.path.dirname(__file__), "string_options_openrouter.txt")
        
        # Default options if file doesn't exist
        default_options = ["Option 1", "Option 2", "Option 3"]
        
        try:
            with open(file_path, 'r') as f:
                options = [line.strip() for line in f.readlines() if line.strip()]
                if not options:
                    options = default_options
        except FileNotFoundError:
            options = default_options
            # Create the file with defaults
            with open(file_path, 'w') as f:
                f.write('\n'.join(default_options))
        
        return {
            "required": {
                "string_choice": (options,),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_string"
    CATEGORY = "DrTim"

    def select_string(self, string_choice):
        return (string_choice,)
    


NODE_CLASS_MAPPINGS = {
    "StringSelectorAspectRatio": StringSelectorAspectRatio,
    "StringSelector": StringSelectorMistral,
    "StringSelectorOR": StringSelectorOR
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringSelectorAspectRatio": "String Selector: Aspect Ratio",
    "StringSelector": "String Selector",
    "StringSelectorOR": "String Selector OR"
}