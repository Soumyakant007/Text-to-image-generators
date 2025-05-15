# Text-to-image-generator

This project generates high-quality images based on text prompts using the **Stable Diffusion v1.5** model from Hugging Face's `diffusers` library.

## Features

- Generate realistic or artistic images from a text description.
- Optional **negative prompt** to refine output by avoiding unwanted features.
- GPU-accelerated generation using **PyTorch** and **CUDA**.
- Saves the final image as `output.png`.

## Technologies Used

- **Python** – Scripting and logic
- **Hugging Face Diffusers** – Stable Diffusion pipeline
- **PyTorch** – Deep learning framework
- **Stable Diffusion v1.5** – Pretrained generative model

## How It Works

1. Load the Stable Diffusion pipeline with FP16 precision.
2. Move the model to GPU (if available).
3. Ask the user to enter:
   - A **prompt** (what they want to see)
   - A **negative prompt** (optional, what they don’t want)
4. If the negative prompt is empty, defaults to `"blurry, low quality"`.
5. Generate and save the image as `output.png`.
