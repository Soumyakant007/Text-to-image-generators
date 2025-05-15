from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda")

prompt = input("Enter your prompt: ")
n_prompt = input("Enter your negative prompt (optional): ")

if not n_prompt.strip():
    n_prompt = "blurry, low quality"

image = pipe(
    prompt=prompt,
    negative_prompt=n_prompt,
    num_inference_steps=50,
    guidance_scale=7.5,
    height=512,
    width=512
).images[0]

image.save("output.png")
