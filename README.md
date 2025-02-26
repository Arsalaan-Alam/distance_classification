# Distance Classification  

This repository implements a distance-based classification system using machine learning and image processing techniques. It includes face detection, clustering, and visualization of results.  

## Setup  

Follow these steps to set up the project:  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/Arsalaan-Alam/distance_classification/
   cd distance_classification
   ```  
2. **Create and activate a virtual environment:**  
   ```sh
   python -m venv venv  
   source venv/bin/activate  # On macOS/Linux  
   venv\Scripts\activate  # On Windows  
   ```  
3. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt  
   ```  
4. **Login to Weights & Biases (WandB):**  
   ```sh
   wandb login  
   ```  
   Enter your WandB API key when prompted.  

5. **Run the Jupyter Notebook:**  
   ```sh
   jupyter notebook  
   ```  
   Open `lab.ipynb` in Jupyter and run the notebook to process and visualize results.  

## Plots  

Below are the generated plots from the classification and clustering process:  

![Plot 1](https://cdn.discordapp.com/attachments/837925621099266089/1344359476882313256/image.png?ex=67c09fd4&is=67bf4e54&hm=df964e2e9453d451a2bb7616a37c15ba80c4dcd1515b0b6c859e5a7137096d2d&)  

![Plot 2](https://cdn.discordapp.com/attachments/837925621099266089/1344359526928744478/image.png?ex=67c09fe0&is=67bf4e60&hm=8edbb8af0a8d4deb7d2e3a839ac0c865153a87b50f9dce29d0db3bfc29cd74ff&)  

![Plot 3](https://cdn.discordapp.com/attachments/837925621099266089/1344359577336021075/image.png?ex=67c09fec&is=67bf4e6c&hm=164acacf700ec38954a285f1e4463a50ba938c991e0b0fee07231cde0c5fabdf&)  

![Plot 4](https://cdn.discordapp.com/attachments/837925621099266089/1344359633824907337/image.png?ex=67c09ff9&is=67bf4e79&hm=8902ed989d548e6b8245f137235904ce7d5967a6ee23b6d1dda787f497b04599&)  

## WandB logging

Below are the photos of metrics being logged on WandB:

![Log 1](https://cdn.discordapp.com/attachments/837925621099266089/1344365372828287046/image.png?ex=67c0a551&is=67bf53d1&hm=994fa525d721fad421f6e6b685e8b61ba2b118ec8e05f4f57b93329321406d85&)  

![Log 2](https://media.discordapp.net/attachments/837925621099266089/1344365440478089227/image.png?ex=67c0a562&is=67bf53e2&hm=bdd554c4b1f554881f2f50a8b76ca0f9134640e2d2adca8c158fde435ec1858b&=&format=webp&quality=lossless&width=1210&height=557)  

## Report

#### 1. What are the common distance metrics used in distance-based classification algorithms?  
Common distance metrics include Euclidean, Manhattan, Chebyshev, and Minkowski distances. Mahalanobis accounts for correlations, Cosine measures vector orientation, and Hamming detects differences in binary data. Each metric is used based on the data type and classification needs.  

#### 2. What are some real-world applications of distance-based classification algorithms?  
Applications include face recognition, spam filtering, customer behavior analysis, fraud detection, speech processing, medical diagnostics, self-driving cars, recommendation systems, document classification, and credit scoring. These algorithms use distance metrics to identify patterns and classify data efficiently.  

#### 3. Explain various distance metrics.  
Euclidean measures straight-line distance, Manhattan calculates grid-based paths, Chebyshev finds maximum coordinate differences, and Minkowski generalizes metrics. Mahalanobis considers data correlations, Cosine evaluates vector angles in text analysis, and Hamming counts binary differences for error detection. Each serves specific classification tasks based on dataset characteristics.  

#### 4. What is the role of cross-validation in model performance?  
Cross-validation evaluates model performance by splitting data into subsets, preventing overfitting and aiding model selection. Methods include k-fold cross-validation, leave-one-out cross-validation (LOOCV), and stratified k-fold cross-validation, ensuring class balance and reliable performance estimation.  

#### 5. Explain variance and bias in terms of KNN.  
Bias increases with high k, causing underfitting, while variance rises with low k, leading to overfitting. The bias-variance tradeoff is crucial—small k results in high variance, large k in high bias. Choosing the right k balances both, ensuring better model generalization and performance.


## Project Overview  

This project performs:  
- Face detection using OpenCV Haar cascades  
- Feature extraction (Hue and Saturation values)  
- Clustering using K-Means  
- Visualization of face clusters  
- Logging results using WandB  

## Contributions  

This was originially supposed to be my submission for machine-learning class at my university but feel free to fork the repository and contribute by submitting pull requests. 

