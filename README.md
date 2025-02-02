# Maize Classification Using Sentinel-2 Imagery
This project demonstrates how to classify maize crops using Sentinel-2 satellite imagery and a pre-trained machine learning model. The workflow includes data preprocessing, model prediction, and visualization of the results. The output is a GeoTIFF file containing the classified maize mask and a visual representation saved as a JPG image. You can tweak the visualization code to suit your preferences. 

# Table of Contents
1. Project Overview
2. Features
3. Requirements
4. Installation
5. Usage
6. Output
7. Contributing
8. License
9. Acknowledgement


## Project Overview
This project aims to classify maize crops in agricultural fields using Sentinel-2 satellite imagery. The workflow includes:

* Loading and preprocessing Sentinel-2 imagery.

* Using a pre-trained machine learning model (maize_classifier.pkl) to predict maize presence.

* Saving the classified output as a GeoTIFF file.

* Visualizing the results using a custom colormap and saving the visualization as a JPG image.

## Features
* Sentinel-2 Imagery Processing: Reads and processes multi-band Sentinel-2 imagery.

* Machine Learning Integration: Uses a pre-trained classifier to predict maize presence.

* GeoTIFF Output: Saves the classified output as a GeoTIFF file for further analysis.

* Visualization: Generates a visual representation of the classified output using a green-to-yellow colormap.

* Error Handling: Robust error handling and logging for smooth execution.

## requirements

To run this project, you need the following Python libraries and tools:

* Python 3.8+

*  Rasterio: For reading and writing geospatial raster data.

* NumPy: For numerical operations.

* Joblib: For loading the pre-trained machine learning model.

* Matplotlib: For visualization.

* Scikit-learn: For machine learning (if retraining the model).

You can install the required libraries using the following command:

`pip install rasterio numpy joblib matplotlib scikit-learn`

## Clone this repository to your local machine

1. Clone this repo


`git clone https://github.com/korykorir/maizeclassfication.git`

2. Install the required dependencies

`pip install -r requirements.txt`

3. Download Sentinel-2 imageary around Uasin-Gishu County only[test.tif] and use the pretrainde random forest classifier [maize_classifier.pkl]


## Usage
Ensure the Sentinel-2 imagery and pretrained model are in the same directory

Run the script `python img.py`

The script will: 
- Load the Sentinel-2 imagery you downloaded
- Predict maize presence using the pretrained model
- Save the classified output as [Maize_mask.tif]


## Output 
The script generates the following outputs
1. [maize_mask.tif] - Which is a GeoTIFF file containing the classifies maize mask
2. [maize_clustered.jpg] - A jPG image visualizing the classified output using a green to yellow colormap

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bugfix.

3. Commit your changes.

4. Submit a pull request.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the MIT License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Acknowledgments

* Sentinel-2 Imagery: Provided by the European Space Agency (ESA).
* Google Earth Engine : Dowloading of the Images

## Contact

For questions or feedback, please contact
* stephenkorykorir@gmail.com
* Github: korykorir
