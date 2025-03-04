The project undertakes fine-tuning OpenAI's GPT-2 (124M) to generate coherent World War I text by training it on 15 Wikipedia articles and The Great War by Peter Hart, available on Internet Archive.

For this project, we use Hugging Face’s Transformers API, PyPDF2, Python's requests module, and BeautifulSoup4.

Example generated text:
"World War I was a dreadful experience for the Austrians. The Russians had to get over them and win their war on 31 July..."

Key Learnings:
From this project, we learn that training a language model—even for a specialized domain like World War I history—requires vast amounts of data. Additionally, efficient pre-processing pipelines are crucial; carelessness in this step can significantly impact model coherence.

Furthermore, our experiments suggest that GPT-2 (124M) exhibits signs of underfitting, struggling to learn efficiently as indicated by plateaus in the training loop. This highlights that while large-scale language models with billions of parameters can be fine-tuned effectively for domain-specific tasks, smaller models like GPT-2’s base version may struggle to achieve coherence in historical narration.
