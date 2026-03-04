<p align="center">
  <h1 align="center">HistoGen: Histopathology Cell Nuclei Image Generation Tool</h1>
</p>

<p align="center">
  <img src="imgs/HistoGen.png">
</p>


## Getting Started

### General Information
**`HistoGen`** is an open-source computational pathology toolbox designed to support researchers and regulatory scientists in generating Histopathology cell nuclei images. For more information, please contact: **[seyed.kahaki@fda.hhs.gov](mailto:seyed.kahaki@fda.hhs.gov)**.


### Information for Developers
Code Documentation: [Link](https://didsr.github.io/HistoGen/index.html)
Please refer to the code documentation.

## Installation

To set up the HistoGen environment, first clone this repository and navigate to the project directory:

```bash
git clone https://github.com/DIDSR/HistoGen.git
cd HistoGen
```

Create a virtual environment and install dependencies from the provided `requirements.txt`:

```bash
python3 -m venv HistoGen_env
source HistoGen_env/bin/activate
pip install -r requirements.txt
```

**Tested Environment:**
- Linux (Ubuntu 22.04 LTS recommended)
- Python 3.12+

### Dependencies
This package needs GPU. 
Some key dependencies include:

```sh
matplotlib==3.10.8
mpi4py==4.1.1
numpy==2.2.6
opencv-contrib-python==4.12.0.88
scikit-image==0.25.2
scikit-learn==1.8.0
scipy==1.16.3
tensorflow==2.20.0
torch==2.9.1
torchvision==0.24.1
```

(See `requirements.txt` for the full list.)

---

## Getting Started Examples

Jupyter notebook and scripts provided to quickly familiarize you with the capabilities and usage of HistoGen:

1. [Generate Nuclei Images](https://github.com/DIDSR/HistoGen/blob/main/01_GenerateImage.ipynb)

This notebook enables the following:

- Load an instance segmentation mask from a `.mat` file
- Convert the instance segmentation mask to semantic mask concatenated to horizontal and vertical map, as detailed in the paper [HoverNet](https://wrap.warwick.ac.uk/126044/1/WRAP-HoVer-Net-simultaneous-segmentation-classification-images-Graham-2019.pdf)
- Setup a diffusion model to generate nuclei images from the mask
- Use either a coarse or finetuned diffusion model checkpoint to generate a user specified number of nuclei images.
- Visualize the generated images with mask overlay and outline
- Save the generated images as 8-bit `.png` files

---

## Contact and Contributions

For any inquiries, suggestions, or collaborative opportunities, please contact Seyed Kahaki or Tahsin Rahman either via this GitHub repo or via email (seyed.kahaki@fda.hhs.gov or Tahsin.Rahman@fda.hhs.gov).

---

## Disclaimer
### About the Catalog of Regulatory Science Tools
The enclosed tool is part of the [Catalog of Regulatory Science Tools](https://cdrh-rst.fda.gov/), which provides a peer-reviewed resource for stakeholders to use where standards and qualified Medical Device Development Tools (MDDTs) do not yet exist. These tools do not replace FDA-recognized standards or MDDTs. This catalog collates a variety of regulatory science tools that the FDA’s Center for Devices and Radiological Health’s (CDRH) Office of Science and Engineering Labs (OSEL) developed. These tools use the most innovative science to support medical device development and patient access to safe and effective medical devices. If you are considering using a tool from this catalog in your marketing submissions, note that these tools have not been qualified as [Medical Device Development Tools](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt) and the FDA has not evaluated the suitability of these tools within any specific context of use. You may [request feedback or meetings for medical device submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-meetings-medical-device-submissions-q-submission-program) as part of the Q-Submission Program.
For more information about the Catalog of Regulatory Science Tools, email [RST_CDRH@fda.hhs.gov](mailto:RST_CDRH@fda.hhs.gov).

## Tool Reference
<!-- •	RST Reference Number: RSTXXXX.01 -->

<!-- •	Date of Publication: XX/XX/XXXX -->

•	Recommended Citation: 

```
U.S. Food and Drug Administration. (2024). HistoGen: A Generative AI tool for for Generating Nuclei Images (RSTXXXX.01). https://cdrh-rst.fda.gov/TBD
```
