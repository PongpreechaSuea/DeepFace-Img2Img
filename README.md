# DeepFaceHuman-Img2Img

DeepFace-Img2Img is a specialized project dedicated to face swapping within images. It operates by taking a source image and a target image, and seamlessly swapping the faces between the two. This service utilizes advanced deep learning techniques to ensure high-quality and realistic results. The primary focus of the project is to provide an easy and efficient way to swap faces in photos, making it ideal for entertainment, personal projects, or research purposes. With a user-friendly interface and powerful backend, DeepFace-Img2Img simplifies the process of face swapping, delivering impressive outcomes with minimal effort.

Access the Colab Notebook for examples and further learning [Colab Notebook](https://colab.research.google.com/drive/1cJGRSdM8j7WJ3WrXcQ2ESiTxGHW0SG5I?usp=sharing)


## Features

- Face swapping from uploaded images
- Adjustable full generation option
- Web interface for easy interaction
- API endpoints for programmatic access

## Requirements

- Python 3.8+
- FastAPI
- Pillow
- torch
- opencv-python
- onnxruntime

## Installation

1. Clone repository:
    ```bash
    git clone https://github.com/PongpreechaSuea/DeepFace-Img2Img.git
    cd DeepFace-Img2Img
    ```

2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    pip install insightface==0.7.3
    ```

4. Download Model:
    ```bash
    cd model
    python download_models.py
    cd ..

    cd src\CodeFormer\CodeFormer\weights
    python download_weights.py
    ```


## Configuration

Customize the `src/config.py` file as needed:

```python
SOURCE_PATH = "./temp_source.jpg"
TARGET_PATH = "./temp_target.jpg"
MODEL_PATH = "./model/inswapper_128.onnx"
# Add other configuration variables as needed
```

## Usage
### Starting the Server
Start the FastAPI server:
```bash
python app.py
```
The server will run on http://0.0.0.0:8000 by default.

## API Endpoints
### Swap Faces in Images

- Endpoint: /swap-face/
- Method: POST
- Description: Upload source and target images to swap faces
- Request: multipart/form-data

    - source: Source image for face swapping
    - target: Target image for face swapping
    - full_generate: Boolean for full generation option


- Response: JPEG image with swapped face

## Web Interface
Access the web interface at http://0.0.0.0:8000/ to use the face swapping tool through a user-friendly interface.

## Example Usage
```python
import requests

url = "http://0.0.0.0:8000/swap-face/"
files = {
    'source': open('path_to_source_image.jpg', 'rb'),
    'target': open('path_to_target_image.jpg', 'rb')
}
data = {'full_generate': 'true'}

response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    with open('result.jpg', 'wb') as f:
        f.write(response.content)
    print("Face swapped image saved as result.jpg")
else:
    print("Error:", response.status_code, response.text)
```


## Docker Support
This project includes Docker support for easy deployment.

## Building and Running with Docker
Build the Docker image:

```bash
docker build -t deepface-img2img .
```

Run the container:
```bash
docker run -p 8000:8000 deepface-img2img
```

## Using Docker Compose
Alternatively, you can use Docker Compose:
```bash
docker-compose up --build
```

This will build the image and start the container, mapping port 8000 on your host to port 8000 in the container.

## Example Output

<p align="center">
  <img src="./images/example_output.jpg" alt="Example Output" width="750"/>
</p>
