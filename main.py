import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time

def load_image(image_path):
    img = Image.open(image_path)
    img_data = np.array(img, dtype=np.float64) / 255  # normalizing the image 
    return img, img_data

#color quantization here
def k_means_quantize(image_path, k_list):
    img, img_data = load_image(image_path)
    h, w, d = img_data.shape
    pixels = img_data.reshape((h * w, d))  # reshape from 3d to 2d

    execution_times = {}

    for k in k_list:
        start_time = time.time()  # Start timing

        #randomly choose from points list i.e. image
        centroids = pixels[np.random.choice(h * w, k, replace=False), :]
        
        for iteration in range(10):  # 10 iters
            # compute euclidean distance and assign to nearest cluster
            dists = np.linalg.norm(pixels[:, None] - centroids, axis=2)
            labels = np.argmin(dists, axis=1)

            # new centroid mean calculation
            new_centroids = np.array([pixels[labels == i].mean(axis=0) for i in range(k)])
            
            # if no change, end process -> convergence
            if np.all(centroids == new_centroids):
                break
            
            centroids = new_centroids

        # replaces each pixels color in the original image with the color of its assigned centroid
        # rescaled back to 0-255 range for display
        quantized_image_data = centroids[labels].reshape((h, w, d))
        quantized_img = Image.fromarray((quantized_image_data * 255).astype(np.uint8))

        end_time = time.time()  # End timing
        execution_times[k] = end_time - start_time  # Calculate elapsed time

        # display original, quantized image, and the centroids
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))
        ax1.imshow(img)
        ax1.set_title('Original Image')
        ax1.axis('off')
        
        ax2.imshow(quantized_img)
        ax2.set_title(f'Quantized Image with K={k}')
        ax2.axis('off')
        
        # Display the color palette
        ax3.imshow([centroids], aspect='auto')
        ax3.set_title(f'Palette of K={k} colors')
        ax3.axis('off')
        
        plt.show()

    for k, exec_time in execution_times.items():
        print(f"Execution time for K={k}: {exec_time:.4f} seconds")

image_path = 'face.jpg'  
k_values = [2, 3, 5, 10, 15, 20]
k_means_quantize(image_path, k_values)