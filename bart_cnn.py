from transformers import BartTokenizer, BartForConditionalGeneration
# Load the tokenizer and model once
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def summarize_text(text):
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(inputs, max_length=150, min_length=20, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# resp = summarize_text("[Sales Rep - Sandeep]: Hello, Brian! Thank you for taking the time to speak with us today. My name is Sandeep, and I'm a sales representative from TechSolutions. I see we have quite the team here, which is fantastic. Before we dive into the details, could you briefly introduce yourself and tell us a bit more about your company?")
# print(resp)