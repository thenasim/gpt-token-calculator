import tiktoken

# Encoding types
enc_gpt4 = tiktoken.encoding_for_model("gpt-4")
enc_gpt3_5_turbo = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Input text, token and encode
input_prompt = input("Enter your input:\n")
encoded = enc_gpt4.encode(input_prompt)
total_token = len(encoded)
print(f"Total tokens: {total_token}")
total_token = input(f"Enter number of tokens: {total_token}? ")
total_token = int(total_token)

# Pricing
## Gpt3
gpt3 = 0.002
## Gpt4
gpt4_8_prompt = 0.03
gpt4_8_completion = 0.06
gpt4_32_prompt = 0.06
gpt4_32_completion = 0.12

per_token = 1000

print(f"Gpt 3 price: {(total_token * gpt3) / per_token}")
print(f"Gpt 4 8k context prompt: {(total_token * gpt4_8_prompt) /  per_token}")
print(f"Gpt 4 8k context completion: {(total_token * gpt4_8_completion) / per_token}")
print(f"Gpt 4 32k context prompt: {(total_token * gpt4_32_prompt) / per_token}")
print(f"Gpt 4 32k context completion: {(total_token * gpt4_32_completion) / per_token}")
