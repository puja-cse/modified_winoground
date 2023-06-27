import json
import pandas as pd
import os  



def extract_captions_winoground(dir = "../dataset/examples.jsonl"):
    """
        This function read the jsonl file containing the image caption and 
        create a csv file (named captions.csv) that contains only img_id, captio_0, caption_1.
        The csv file is further edited manually to modify the captions to reduce language compositionality. 
    """

    img_id_0 =[]
    img_id_1 =[]
    caption_0 =[]
    caption_1 =[]
    with open(dir, 'r') as file:
        for line in file:
            caption = json.loads(line)
            img_id_0.append(caption['image_0'])
            img_id_1.append(caption['image_1'])
            caption_0.append(caption['caption_0'])
            caption_1.append(caption['caption_1'])
    file.close()
    dict = {"image_0": img_id_0, "image_1": img_id_1, "caption_0": caption_0, "caption_1": caption_1 }
    df = pd.DataFrame(dict)
    if os.path.exists('../dataset/captions.csv')==False :
        df.to_csv("../dataset/captions.csv")
    return dict

def extract_edited_captions_winoground(dir="../dataset/edited_captions.xls", edited_captions=50):
    df = pd.read_excel(dir,index_col = 0)
    img_id_0 =[]
    img_id_1 =[]
    true_caption_0 =[]
    true_caption_1 =[]
    edited_caption_0 =[]
    edited_caption_1 =[]
    for i in range(edited_captions+1):
        if i==31:
            continue
        img_id_0.append(df['image_0'][i])
        img_id_1.append(df['image_1'][i])
        true_caption_0.append(df['caption_0'][i])
        true_caption_1.append(df['caption_1'][i])
        edited_caption_0.append(df['modified_caption_0'][i])
        edited_caption_1.append(df['modified_caption_1'][i])
    dict = {"image_0": img_id_0, "image_1": img_id_1, 
            "true_caption_0": true_caption_0, "true_caption_1": true_caption_1,  
            "modified_caption_0": edited_caption_0, "modified_caption_1": edited_caption_1}
    return dict