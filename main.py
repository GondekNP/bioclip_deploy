import torch
from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Load model
model = ...
model.load_state_dict(torch.load("model.pth"))
model.eval()

# Define image transformations

transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def fetch_image(url: str) -> Image.Image:

    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


def classify_image(image: Image.Image) -> dict:

    image = transform(image)
    image = image.unsqueeze(0)

    with torch.no_grad():
        output = model(image)

    # Assuming some post-processing
    return {"classifications": output.argmax(dim=1).item()}


@app.post("/classify")
def classify(url: str):

    image = fetch_image(url)
    classifications = classify_image(image)

    return classifications


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
