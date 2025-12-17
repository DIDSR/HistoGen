<p align="center">
  <h1 align="center">GenNuclei: A Generative AI tool for for Generating Nuclei Images</h1>
</p>

<p align="center">
  <img src="img/GenNuclei_title.png">
</p>


## Getting Started

### General Information
**`GenNuclei`** is an open-source computational pathology toolbox designed to support researchers and regulatory scientists in generating nuclei images. For more information, please contact: **[seyed.kahaki@fda.hhs.gov](mailto:seyed.kahaki@fda.hhs.gov)**.


### Information for Developers
Code Documentation: [Link](https://didsr.github.io/GenNuclei/index.html)
Please refer to the code documentation and email  **[seyed.kahaki@fda.hhs.gov](mailto:seyed.kahaki@fda.hhs.gov)** if you have any questions.

## Installation

To set up the GenNuclei environment, first clone this repository and navigate to the project directory:

```bash
git clone https://github.com/DIDSR/GenNuclei.git
cd GenNuclei
```

Create a virtual environment and install dependencies from the provided `requirements.txt`:

```bash
python3 -m venv gennuclei_env
source gennuclei_env/bin/activate
pip install -r requirements.txt
```

**Tested Environment:**
- Linux (Ubuntu 22.04 LTS recommended)
- Python 3.10+

### Dependencies

Some key dependencies include:

```sh
numpy==2.1.2
opencv-python==4.11.0.86
scikit-image==0.25.2
scikit-learn==1.6.1
matplotlib==3.10.1
pyfeats==1.0.1
mahotas==1.4.18
torch==2.5.1
torchvision==0.20.1
```

(See `requirements.txt` for the full list.)

---

## Getting Started Examples

Jupyter notebook and scripts provided to quickly familiarize you with the capabilities and usage of GenNuclei:

1. [Generate Nuclei Images](https://github.com/DIDSR/GenNuclei/blob/main/01_GenerateImage.ipynb)

---

## Contact and Contributions

For any inquiries, suggestions, or collaborative opportunities, please contact Seyed Kahaki either via this GitHub repo or via email (seyed.kahaki@fda.hhs.gov).

---

## Disclaimer
### About the Catalog of Regulatory Science Tools
The enclosed tool is part of the [Catalog of Regulatory Science Tools](https://cdrh-rst.fda.gov/), which provides a peer-reviewed resource for stakeholders to use where standards and qualified Medical Device Development Tools (MDDTs) do not yet exist. These tools do not replace FDA-recognized standards or MDDTs. This catalog collates a variety of regulatory science tools that the FDA’s Center for Devices and Radiological Health’s (CDRH) Office of Science and Engineering Labs (OSEL) developed. These tools use the most innovative science to support medical device development and patient access to safe and effective medical devices. If you are considering using a tool from this catalog in your marketing submissions, note that these tools have not been qualified as [Medical Device Development Tools](https://www.fda.gov/medical-devices/medical-device-development-tools-mddt) and the FDA has not evaluated the suitability of these tools within any specific context of use. You may [request feedback or meetings for medical device submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/requests-feedback-and-meetings-medical-device-submissions-q-submission-program) as part of the Q-Submission Program.
For more information about the Catalog of Regulatory Science Tools, email [RST_CDRH@fda.hhs.gov](mailto:RST_CDRH@fda.hhs.gov).

## Tool Reference
•	RST Reference Number: RSTXXXX.01

•	Date of Publication: XX/XX/XXXX

•	Recommended Citation: 

```
U.S. Food and Drug Administration. (2024). GenNuclei: A Generative AI tool for for Generating Nuclei Images (RSTXXXX.01). https://cdrh-rst.fda.gov/TBD
```
