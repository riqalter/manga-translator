# Manga Translator

## Table of Contents

- [Introduction](#introduction)
- [Approach](#approach)
  - [Data Collection](#data-collection)
  - [yolov12s](#yolov12s)
  - [Manga-ocr](#manga-ocr)
  - [Deep-translator](#deep-translator)
- [Server](#server)

## Introduction

I love reading manga, and I can't wait for the next chapter of my favorite manga to be released. However, the newest chapters are usually in Japanese, and they are translated to English after some time. I want to read the newest chapters as soon as possible, so I decided to build a manga translator that can translate Japanese manga to English.

## Approach

I want to translate the text in the manga images from Japanese to English. I will first need to know where these speech bubbles are on the image. For this I will use `yolov12s` to detect the speech bubbles. Once I have the speech bubbles, I will use `manga-ocr` to extract the text from the speech bubbles. Finally, I will use `deep-translator` to translate the text from Japanese to English.

![Manga Translator](./assets/MangaTranslator.png)

### Data Collection

This [dataset](https://universe.roboflow.com/speechbubbledetection-y9yz3/bubble-detection-gbjon/dataset/2#) contains over 8500 images of manga pages together with their annotations from Roboflow. I will use this dataset to train `yolov12s` to detect the speech bubbles in the manga images. To use this dataset with yolov12s, I will need to convert the annotations to the YOLO format, which is a text file containing the class label and the bounding box coordinates of the object in the image.

This dataset is over 1.7GB in size, so I will need to download it to my local machine. The rest of the code should be run after the dataset has been downloaded and extracted in this directory.

The dataset contains mostly English manga, but that is fine since I am only interested in the speech bubbles.

### Yolov12s

`Yolov12s` is a state-of-the-art, real-time object detection system. I will use `Yolov12s` to detect the speech bubbles in the manga images.

**Note:** On this research prototype, the output shown is using the `Yolov11s`, final implementation will use `Yolov12s`.


### Manga-ocr

Optical character recognition for Japanese text, with the main focus being Japanese manga. This Python package is built and trained specifically for extracting text from manga images. This makes it perfect for extracting text from the speech bubbles in the manga images.

### Deep-translator

`Deep-translator` is a Python package that uses the Google Translate API to translate text from one language to another. I will use `deep-translator` to translate the text extracted from the manga images from Japanese to English.

## Server

I created a simple server and client using FastAPI. The server will receive the manga image from the client, detect the speech bubbles, extract the text from the speech bubbles, and translate the text from Japanese to English. The server will then send the translated text back to the client.

To run the server, you will need to install the required packages. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

You can then start the server by running the following command:

```bash
python app.py
```

The server will start running on `http://localhost:8000`. You can then send a POST request to `http://localhost:8000/predict` with the manga image as the request body.

```json
POST /predict
{
  "image": "base64_encoded_image"
}
```

### Todo changes on translator

- [x] add non-deeplearning translator (google translate)
- [ ] add deepl translator
- [x] add openai api compatibility base url

*reference: https://github.com/zyddnys/manga-image-translator/tree/main/manga_translator/translators

### Todo Upcoming image re-write from Pillow to LaMa

- [ ] add LaMa image re-write

### Finetune manga-ocr dataset
- [ ] fintune manga-ocr with academic only licensed dataset