import re
import pandas as pd

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.data_generators import text_encoder
from tensor2tensor.utils import registry

@registry.register_problem
class MyProblem(text_problems.Text2TextProblem):
  """Predict next line of poetry from the last line. From Gutenberg texts."""

  @property
  def vocab_size(self):
    return 16000

  #@property
  #def vocab_type(self):
  #  return text_problems.VocabType.CHARACTER

  #@property
  #def oov_token(self):
  #  """Out of vocabulary token. Only for VocabType.TOKEN."""
  #  return None
  
  @property
  def is_generate_per_split(self):
    # generate_data will shard the data into TRAIN and EVAL for us.
    return False

  @property
  def dataset_splits(self):
    """Splits of data to produce and number of output shards for each."""
    # 10% evaluation data
    return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 9,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]

  def generate_samples(self, data_dir, tmp_dir, dataset_split):
    with open("../dataset/input.txt","r",encoding="utf-8")as f_in, open("../dataset/output.txt","r",encoding="utf-8")as f_out:
      for in_text, out_text in zip(f_in.readlines(),f_out.readlines()):
        if not in_text or not out_text:
            continue
        yield {
            'inputs': in_text,
            'targets': out_text
        }
        
  #def generate_encoded_samples(self, data_dir, tmp_dir, dataset_split):
  #  generator = self.generate_samples(data_dir, tmp_dir, dataset_split)
  #  encoder = text_encoder.TokenTextEncoder(data_dir + "/vocab.my_problem.tokens", replace_oov="<unk>")
  #  target_encoder = encoder
    # call local encoding generator
  #  return text_problems.text2text_generate_encoded(generator, encoder, target_encoder, has_inputs=self.has_inputs)