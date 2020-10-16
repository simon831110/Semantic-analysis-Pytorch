在這部分中我們訓練了"基於字母的CNN"來分類評論，分類為(正面、負面)。
模型以及實際執行源於<a href="https://github.com/ahmedbesbes/character-based-cnn">這裡</a>

模型架構則出於這則<a href="https://arxiv.org/pdf/1509.01626.pdf">論文</a>

##需求

- PyTorch >=0.4.1
- Tensorflow >=2.0.0 (optional, useful for model monitoring)
- TensorboardX >=1.8 (optional, useful for model monitoring) 

##訓練

爬蟲下載完的資料放置於 `src/scraping/trustpilot/comments_trustpilot_v2.csv`

```shell
cd src/training/

python train.py --data_path ../src/scraping/trustpilot/comments_trustpilot_v2.csv \
                --validation_split 0.1 \
                --label_column rating \
                --text_column comment \
                --group_labels binarize \ 
                --extra_characters "éàèùâêîôûçëïü" \
                --max_length 500 \
                --dropout_input 0 \
                --model_name trustpilot \
                --balance 1
```
