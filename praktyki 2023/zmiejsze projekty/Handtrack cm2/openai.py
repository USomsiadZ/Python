import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)


#get random forest model    


