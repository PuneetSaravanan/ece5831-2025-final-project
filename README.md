# Animal Sound Recognition

A deep learning project for recognizing and classifying animal sounds using the ESC-50 dataset.

## Project Structure

```
animal-sound-recognition/
├── data/                      # Data directory
│   ├── raw/                   # Original, immutable ESC-50 data
│   ├── processed/             # Preprocessed audio files and features
│   ├── interim/               # Intermediate data transformations
│   └── external/              # External datasets or additional resources
│
├── src/                       # Source code
│   ├── data/                  # Data loading and preprocessing
│   ├── features/              # Feature extraction (MFCCs, spectrograms, etc.)
│   ├── models/                # Model architectures
│   ├── training/              # Training loops and pipelines
│   ├── evaluation/            # Model evaluation and metrics
│   ├── utils/                 # Utility functions
│   └── visualization/         # Visualization tools
│
├── notebooks/                 # Jupyter notebooks
│   ├── exploratory/           # EDA and data exploration
│   └── experiments/           # Model experiments and prototyping
│
├── models/                    # Trained models
│   ├── saved_models/          # Final trained models
│   └── checkpoints/           # Training checkpoints
│
├── configs/                   # Configuration files
│   ├── config.yaml            # Main configuration
│   └── model_config.yaml      # Model-specific configurations
│
├── scripts/                   # Standalone scripts
│   ├── download_data.sh       # Download ESC-50 dataset
│   ├── preprocess.py          # Data preprocessing script
│   └── train.py               # Training script
│
├── tests/                     # Unit tests
│
├── logs/                      # Training logs and TensorBoard files
│
├── outputs/                   # Generated outputs (predictions, reports)
│
├── docs/                      # Documentation
│
├── requirements.txt           # Python dependencies
├── setup.py                   # Package installation script
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download ESC-50 dataset: `bash scripts/download_data.sh`
4. Preprocess data: `python scripts/preprocess.py`

## Usage

Train a model:
```bash
python scripts/train.py --config configs/config.yaml
```

## Dataset

This project uses the ESC-50 dataset from Kaggle, which contains 2000 environmental audio recordings suitable for benchmarking methods of environmental sound classification.

## License

MIT
