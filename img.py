import rasterio as rio
import numpy as np
import joblib
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from rasterio.errors import RasterioIOError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Open the Sentinel-2 image
        with rio.open('test.tif') as sentinel_image:
            logging.info("Sentinel-2 image opened successfully.")

            # Load the saved model
            try:
                classifier = joblib.load('maize_classifier.pkl')
                logging.info("Model loaded successfully.")
            except Exception as e:
                logging.error(f"Error loading model: {e}")
                return

            # Read the image data (assuming 12 bands)
            img = sentinel_image.read()[:12, :, :] 
            height, width, num_bands = img.shape[1], img.shape[2], img.shape[0]

            # Create an empty array with the same dimensions and data type
            img2 = np.empty((height, width,num_bands), dtype=sentinel_image.meta['dtype'])

            # Loop through the raster's bands to fill the empty array
            for band in range(num_bands):
                img2[:, :,band] = sentinel_image.read(band + 1)

            # Convert to 2D array (rows x columns, bands)
            img2d=img2[:,:,:12].reshape((img2.shape[0]*img2.shape[1],img2.shape[2]))

            # Predict labels using the classifier
            try:
                predicted_labels = classifier.predict(img2d)
                logging.info("Prediction completed successfully.")
            except Exception as e:
                logging.error(f"Error during prediction: {e}")
                return

            # Reshape predicted labels to match the original image dimensions
            img_cl = predicted_labels.reshape(img2[:,:,0].shape)

            # Convert to uint8 for saving as a raster
            img_cl = img_cl.astype(np.uint8)

            # Save the predicted labels as a new GeoTIFF
            try:
                with rio.open('Maize_mask.tif', 'w',
                              driver='GTiff',
                              height=height,
                              width=width,
                              count=1, 
                              dtype=img_cl.dtype,
                              crs=sentinel_image.crs,
                              transform=sentinel_image.transform) as dst:
                    dst.write(img_cl, 1)
                logging.info("Maize mask saved successfully as 'Maize_mask.tif'.")
            except RasterioIOError as e:
                logging.error(f"Error saving output raster: {e}")
                return

            # Visualization
            try:
                # Define a custom colormap
                cmap = mc.LinearSegmentedColormap.from_list("", ["green", "yellow"])

                # Plot the resulting array
                plt.figure(figsize=[15, 15])
                plt.imshow(img_cl, cmap=cmap)
                plt.axis('off') 
                plt.savefig("elhas_clustered.jpg", bbox_inches='tight') 
                plt.show()  
                logging.info("Visualization saved as 'maize_clustered.jpg'.")
            except Exception as e:
                logging.error(f"Error during visualization: {e}")

    except RasterioIOError as e:
        logging.error(f"Error opening Sentinel-2 image: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()