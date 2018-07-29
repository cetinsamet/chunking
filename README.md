# chunking
Simple chunk tagger implementation for the English language  
A chunking model is trained with a corpus containing almost 9,000 English sentences.  
  
## Model  
Model (mini model) in the repo is trained using mini data which contains only almost 100 English sentences.  
Therefore, it does not perform well enough.  
  
I encourage you to train a new model on your own using the corpus in data/ directory.  
My training lasted almost 14 minutes on a device with 3,1 GHz Intel Core i7 processor.  
  
## Usage  
$**python3**  chunk.py  input-sentence  
  
### Example  
$**cd**  src  
$**python3** chunk.py  "This is the strangest life I've ever known."  
**->** Chunker is loaded.  
**->** [('This', 'B-NP'), ('is', 'B-VP'), ('the', 'B-NP'), ('strangest', 'I-NP'), ('life', 'I-NP'), ('I', 'B-NP'), ("'ve", 'B-VP'), ('ever', 'I-VP'), ('known', 'I-VP'), ('.', 'O')]  
  
*P.S. Above example is tested with a model trained on corpus in data/ directory(with almost 9,000 English sentences).*   
  
> This is the strangest life I've ever known.
> Jim MORRISON
