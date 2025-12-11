from setuptools import setup, find_packages

setup(
    name="animal-sound-recognition",
    version="0.1.0",
    description="Animal sound recognition using ESC-50 dataset",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "torch>=2.0.0",
        "torchaudio>=2.0.0",
        "librosa>=0.10.0",
        "scikit-learn>=1.3.0",
        "pyyaml>=6.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "flake8>=6.0.0",
            "jupyter>=1.0.0",
        ],
    },
)
