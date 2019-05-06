from tensor2tensor.models import transformer
from tensor2tensor.utils import registry

@registry.register_hparams
def myhparams():
  """HParams for transformer base model for single GPU."""
  hparams = transformer.transformer_base()
  hparams.batch_size = 1024
  hparams.learning_rate_schedule = "constant*linear_warmup*rsqrt_decay"
  hparams.learning_rate_constant = 0.1
  hparams.learning_rate_warmup_steps = 16000
  hparams.num_heads = 8
  hparams.num_hidden_layers = 6
  hparams.hidden_size = 512
  hparams.attention_dropout = 0.0
  hparams.relu_dropout = 0.0
  return hparams
  
@registry.register_ranged_hparams
def myhparamsrange(rhp):
  rhp.set_float("learning_rate", 0.01, 0.2, scale=rhp.LOG_SCALE)
  rhp.set_discrete("filter_size", [1024, 2048])
  rhp.set_int("num_hidden_layers", 3, 5)
  rhp.set_discrete("hidden_size", [128, 256, 512])
  rhp.set_float("attention_dropout", 0.4, 0.7)
  rhp.set_float("relu_dropout", 0.4, 0.7)