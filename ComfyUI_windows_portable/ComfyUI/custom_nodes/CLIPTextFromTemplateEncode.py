
import csv
import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))


import comfy.utils

class ClipTextFromTemplateEncode:

    styles = None

    def __init__(self):
        pass
    
    def handle_prompt_change(self, value):
        # Do something with the new value of the "prompt" input node
        print("New prompt value:", value)
    
    @classmethod
    def INPUT_TYPES(cls):


  

        if not os.path.exists("styles.csv"):
            print("WARNING styles.csv does not exist - ClipTextFromTemplateEncode cannot be used")
            cls.styles = [["No Styles.csv", "(((Cartoon sad face))) negativity", "positivity"]]
        else:
            with open("styles.csv", "r") as f:
                reader = csv.reader(f, dialect='excel')
                #cls.styles = [row for row in reader if row[1]!="prompt" and row[0]!= "None"]
                cls.styles = [row for row in reader if len(row) == 3 and row[1] != "prompt" and row[0] != "None"]

        # Prepend the new row to cls.styles
        cls.styles.insert(0, ["None", "", ""])

        style_names = [row[0] for row in cls.styles]

        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "Positive "}),
                "additionalNegative": ("STRING", {"multiline": True, "default": "Negative"}),
                "style1": (style_names, {"default": style_names[0]}),
                "style2": (style_names, {"default": style_names[0]}),
                "style3": (style_names, {"default": style_names[0]}),
                "logPrompt": (["No", "Yes"],{"default":"No"}),               
                "clip" : ("CLIP",)
            },
        }



    RETURN_TYPES = ("CONDITIONING", "CONDITIONING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "condition"
    OUTPUT_NODE = False
    CATEGORY = "conditioning"

    def condition(self, prompt, style1,style2,style3,logPrompt,additionalNegative,clip):
        positive=""
        negative=""

        if style1=="None" and style2=="None" and style3=="None":
            positive=prompt
        else:
            for row in self.styles:
                if row[0] == style1 or row[0] == style2 or row[0] == style3:
                    positive += row[1]              
                    negative += row[2]

            if "{prompt}" not in positive:
                positive =  prompt + " " + positive
            else:
                positive = positive.replace("{prompt}", prompt)

        negative+=" "+additionalNegative
        if logPrompt == "Yes":
            print("Positive = [" + positive + "]")
            print("Negative = [" + negative + "]")
         

        return ([[clip.encode(positive), {}]],[[clip.encode(negative), {}]], )

NODE_CLASS_MAPPINGS = {
    "ClipTextFromTemplateEncode": ClipTextFromTemplateEncode
}
