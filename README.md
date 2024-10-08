# Language Complexity
This repository contains the experiments for validating compressibility-based language complexity metrics over indigenous South American languages. We use
parallel data from the Bible and divide our analysis in two subsets: languages for wich we have at least 90% of Bible verses (d90) and the set of common verses for all languages (dall).

Here you will find the metrics implementations, the complexity values obtained computing the metrics, and the notebooks to perform metric validation from complexity values.

We are not making available the source text in indigenous languages, because the dataset is proprietary and we do not have permission to share.
However, you can use the code to reproduce our experiments for your own dataset and to reproduce our analysis over the complexities metrics data we computed over the original texts.


## Code organization 
- [notebooks](./notebooks/) contains the necessary notebooks for processing the dataset and analyzing the metric values obtained
- [src](./src) contains the source code.
    - [src/experiments.py](./src/experiments.py) computes the experiments over the given dataset
- [requirements.txt](./requirements.txt) requirements necessary to run the [notebooks](./notebooks/) and the programs in [src](./src)
- [shell.nix](./shell.nix) nix-shell setup (alternative for requirements.txt)
- [results](./results/) The metric values obtained from our experiments with the original data that you can use to reproduce our analysis using [./notebooks/Propositions.ipynb](./notebooks/Propositions.ipynb).

## How to run the experiments and reproduce our analysis
1. Install requirements
2. Put your data in a ./dataset directory
3. Run the notebook: [Create_Dataset.ipynb](./notebooks/Create_Dataset.ipynb) (fix path to your dataset)
4. Run the experiments program:
```Bash
    python src/experiments.py filename encoding percent runs seed output
```
5. Copy and adapt (or change)  [./notebooks/Propositions.ipynb](./notebooks/Propositions.ipynb) to use the results from the previous step


