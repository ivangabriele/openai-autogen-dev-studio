# OpenAI Autogen Game Studio

Generate games leveraging OpenAI agents, taking advantage of Microsoft Autogen OpenAI Agent.

> ⚠️ **This is a work in progress!**<br>
> The current code is a giant mess, and more agents are on their way to greatly improve results,
> even though it's already working.

## Getting Started

### Pre-requisites

You either need an OpenAI API or an Azure OpenAI API key.

**Don't count on `GPT-3.5`**, `turbo` or not, to achieve anything meaningful. `GPT-4` is a must, ideally `GPT-4-32k`.

### Anaconda

```sh
conda create -n autogen python=3.10
conda activate autogen
pip install poetry
poetry install
cp oai_config_list.sample.json oai_config_list.json
```

You MUST copy (locally) [this tiny fix](https://github.com/microsoft/autogen/pull/47) to get the code to work.

Edit the end of `main.py` to customize your first instruction.

Then you can run it via:

```sh
make run
```
