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

## Project Overview  

This project performs:  
- Face detection using OpenCV Haar cascades  
- Feature extraction (Hue and Saturation values)  
- Clustering using K-Means  
- Visualization of face clusters  
- Logging results using WandB  

## Contributions  

This is originially supposed to be my submission for machine-learning class at my university but feel free to fork the repository and contribute by submitting pull requests. 

