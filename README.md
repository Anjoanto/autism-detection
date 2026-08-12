# Autism Detection

Educational project that explores autism-related screening using **video gesture analysis**, **OpenCV**, **MediaPipe**, and a **deep learning** image classifier.

> **Disclaimer:** This is a student / research prototype. It is **not** a medical device and must **not** be used for clinical diagnosis. Always consult qualified healthcare professionals.

## Overview

The system captures a short webcam video of hand motion, extracts hand landmarks, plots the gesture trail as an image, and classifies that graph with a CNN as **Autistic** or **Non-autistic**.

```
Webcam video
    → Hand tracking (OpenCV + MediaPipe)
    → Landmark coordinates (CSV)
    → Gesture graph image
    → Keras CNN (keras_model.h5)
    → Prediction shown in PHP UI
```

## Project structure

```
autism-detection/
├── backend/                 # Python pipeline + Flask API
│   ├── api.py               # Flask server (`/track`)
│   ├── handTrack.py         # Webcam capture + hand landmark tracking
│   ├── convertcsv.py        # Landmark averaging / cleanup
│   ├── graph.py             # Plot landmarks → aut.png
│   ├── train.py             # Run trained model on graph image
│   ├── createModel.py       # CNN training script
│   ├── keras_model.h5       # Trained model weights
│   └── labels.txt           # Class labels
├── frontend/                # PHP UI
│   ├── index.php            # Start form (name / gender)
│   ├── result.php           # Shows prediction result
│   └── button.css           # Styles
└── dataset/                 # Sample gesture graph images
    ├── autistic-graph/
    └── non-autistic-graph/
```

## How it works

1. **Capture** — `handTrack.py` opens the webcam for ~10 seconds, tracks a selected ROI with OpenCV, and detects hand landmarks with MediaPipe.
2. **Process** — Landmark `(x, y)` points are written to `test.csv`, then averaged into `free.csv` by `convertcsv.py`.
3. **Visualize** — `graph.py` plots the landmark path and saves `aut.png`.
4. **Classify** — `train.py` loads `keras_model.h5` and predicts:
   - `0` → Autistic  
   - `1` → Non-autistic  
5. **Present** — The PHP frontend calls the Flask `/track` endpoint and shows the score on `result.php`.

## Tech stack

| Layer | Tools |
| --- | --- |
| Computer vision | OpenCV, MediaPipe |
| ML / DL | Keras / TensorFlow, CNN (Conv2D + Dense) |
| Backend API | Flask |
| Frontend | PHP, HTML, CSS |
| Data | Gesture graph PNGs under `dataset/` |

## Getting started

### Prerequisites

- Python 3.8+ (recommended)
- PHP + a local server (e.g. XAMPP / built-in PHP server)
- Webcam access

### Backend setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install flask opencv-python mediapipe pandas numpy matplotlib keras tensorflow
python api.py
```

Flask should start at `http://127.0.0.1:5000`.

### Frontend setup

Serve the `frontend/` folder (example with PHP’s built-in server):

```bash
cd frontend
php -S localhost:8080
```

Open `http://localhost:8080/index.php`, enter a name, and click **Get's Started**. The page calls `http://127.0.0.1:5000/track` and redirects to the result page.

> Note: Some paths in the original PHP (e.g. image URL on `result.php`) assume a local XAMPP layout. Adjust those URLs for your environment if assets do not load.

## Training the model (optional)

`createModel.py` builds a small binary CNN and trains it on image folders:

```bash
cd backend
python createModel.py
```

Update `train_data_dir` / `validation_data_dir` in that script to point at your prepared image directories before training. The script saves weights to `keras_model.h5`.

Sample labeled graphs for reference live under:

- `dataset/autistic-graph/`
- `dataset/non-autistic-graph/`

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Basic index template |
| `GET` | `/track` | Runs the tracking → graph → prediction pipeline and returns JSON |

## Labels

From `backend/labels.txt`:

```
0 Autistic
1 Non-autistic
```

## Limitations

- Relies on a short webcam session and hand visibility.
- Model quality depends heavily on dataset size and labeling quality.
- Output is a prototype score, not a clinical assessment.
- Some scripts use `exec(open(...))` chaining and Windows-oriented paths from the original setup; clean those up for production use.

## Author

**Anjo Anto** · [GitHub](https://github.com/Anjoanto)
