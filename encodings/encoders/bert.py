import torch
from keras_preprocessing.sequence import pad_sequences
from transformers import BertTokenizerFast, BertModel

# configure device
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("There are %d GPU(s) available." % torch.cuda.device_count())
    print("We will use the GPU:", torch.cuda.get_device_name(0))
else:
    print("No GPU available, using the CPU instead.")
    device = torch.device("cpu")


class BERT:
    def __init__(self, name="bert-base-uncased", max_len=512):
        self.name = name
        self.max_len = max_len

        # load BertTokenizer
        self.tokenizer = BertTokenizerFast.from_pretrained(name, do_lower_case=True)

        # load BertModel
        self.model = BertModel.from_pretrained(name, add_pooling_layer=True)
        self.model.eval()
        self.model.to(device)

    def encode(self, sent):
        # prepare inputs
        input_ids = self.tokenizer.encode(sent, add_special_tokens=True)
        input_ids = pad_sequences(
            [input_ids],
            maxlen=self.max_len,
            dtype="long",
            value=0,
            truncating="post",
            padding="post",
        )[0]
        att_mask = (input_ids > 0).astype(int)  # attention mask

        # load inputs to device
        input_ids = torch.tensor(input_ids).unsqueeze(0).to(device)
        att_mask = torch.tensor(att_mask).unsqueeze(0).to(device)

        # output
        outputs = self.model(
            input_ids, token_type_ids=None, attention_mask=att_mask
        ).pooler_output.to("cpu")

        outputs = outputs.detach().numpy()

        return outputs.tolist()
