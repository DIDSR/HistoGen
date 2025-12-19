from nudiff.image_syn.utils.script_util import create_model_and_diffusion
from nudiff.image_syn.utils import dist_util
import scipy.io as sio
import skimage.io as io
from nudiff.image_syn.utils.datasets import get_hv
import numpy as np
import glob, os
import torch
from tqdm import tqdm
import matplotlib.pyplot as plt
import argparse
import skimage.measure as measure
from PIL import Image
import matplotlib.colors as mpc
from skimage import segmentation
from scipy import ndimage

def convert_mask(inst):
    sem = np.zeros(inst.shape[:2])
    sem[inst > 0] = 1
    hv = get_hv(inst).astype(np.float32)
    mask = np.concatenate([sem[:,:,None], hv], axis=-1)
    return mask

def crop_and_pad_inst_mask(inst,crop_mask=None):

    if crop_mask is not None and len(crop_mask)==2:
        inst = inst[:crop_mask[0],:crop_mask[1]]

    h, w = inst.shape
    h_padded, w_padded = int(np.ceil(h/32.0)*32), int(np.ceil(w/32.0)*32)
    h_front = (h_padded-h)//2
    w_front = (w_padded-w)//2
    inst_padded = np.zeros([h_padded, w_padded], dtype=inst.dtype)
    inst_padded[h_front:h_front+h, w_front:w_front+w] = inst
    return inst_padded

def load_inst_mask_from_path(mask_file_path,mask_key='inst_map'):

    if mask_file_path.endswith('.mat'):
        mask = sio.loadmat(mask_file_path)[mask_key]
    else:
        mask = io.imread(mask_file_path)

    return mask



def plot_generated_images(gen_images,mask=None,mask_outline=True,figsize=(10,4),dpi=100):
    num_images = len(gen_images)
    cols = num_images if num_images < 5 else 5
    rows = 1 + num_images//cols

    mask_cmap = mpc.ListedColormap(['black', 'lightgreen'])
    maskb_cmap = mpc.ListedColormap(['none', 'lightgreen'])

    if mask is not None:
        mask = mask[:,:,0]
        mask = (mask - mask.min()) / (mask.max() - mask.min()).astype(np.bool_)
        mask_boundary = get_mask_outline(mask, widen=2)

    fig, axs = plt.subplots(rows,cols, figsize=figsize, dpi=dpi)

    axs = axs.ravel()

    for i in range(num_images):
        im = axs[i].imshow(gen_images[i])
        axs[i].axis('off')
        if mask is not None:
            im_m = axs[i].imshow(mask,cmap=mask_cmap, alpha=0.2)
            im_mb = axs[i].imshow(mask_boundary,cmap=maskb_cmap, alpha=0.9)

    for ax in axs[num_images:]:
        ax.remove()
    
    fig.tight_layout()

    return fig

def get_mask_outline(binary_mask, widen=False):
    outline = segmentation.find_boundaries(binary_mask, mode='inner')
    if widen:
        structure = np.ones((int(widen), int(widen)), dtype=bool)
        # Apply binary dilation
        outline = ndimage.binary_dilation(outline, structure=structure, iterations=1)
    return outline

def save_output_uint8(gen_images, mask_name=None, output_path='./output'):

    os.makedirs(output_path,exist_ok=True)
    if mask_name == None:
        mask_fname = 'mask.tif'
    else:
        mask_fname = mask_name+'.tif'
    
    for i, an_image in enumerate(gen_images):
        image_fname = f"{mask_name}_generated_image_{i}.png"
        an_image_uint8 = Image.fromarray((an_image * 255).astype(np.uint8))
        an_image_uint8.save(os.path.join(output_path,image_fname))

    return True



def is_valid_directory(parser, arg):
    if not os.path.isdir(arg):
        parser.error("The directory %s does not exist!" % arg)
    else:
        return arg

def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg
