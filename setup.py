from setuptools import setup, find_packages

setup(
    name="flux-inpainting-controlnet-alimama",
    version="0.1.0",
    description="Alimama's Flux ControlNet and Transformer implementation for image generation",
    author="Nikola Gligorovski",
    author_email="gligorovskinikola@gmail.com",
    # packages=["."],  # Use "." since package is in root directory
    # package_dir={"": "."},  # Map root package to current directory
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "diffusers==0.30.2",
        "transformers>=4.46.2",
        "numpy>=2.1.3",
        "sentencepiece",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)