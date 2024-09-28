#Importing the libraries
import torch
from diffusers import FluxPipeline as fp

# defining the image generater model
model_id = "black-forest-labs/Flux.1-schnell"

# defining pipeline
pipe = fp.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload() # saving VRAM by clocking CPU

# Defining the prompt and generating image
prompt = "A girl dancing with openpose points in a disco hall"
seed = 42
image = pipe(
    prompt,
    output_type = "pil",
    num_inference_steps=4,
    generator=torch.Generator("cpu").manual_seed(seed)
).images[0]

# saving the image
image.save("flux_image.png")
