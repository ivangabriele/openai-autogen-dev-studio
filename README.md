# OADS - OpenAI Autogen Development Studio

Generate games and programs using OpenAI agents. Built on top of [Microsoft Autogen](https://github.com/microsoft/autogen).

> ⚠️ **Work In Progress**  
> The current code works (yeah!) but:
> - It needs some cleaning up.
> - Enhancements can be made with better prompt engineering and the addition of more agents.
> - Microsoft Autogen is still in its early stages contain a few bugs.

## Getting Started

### Pre-requisites

You either need an OpenAI API key or an Azure OpenAI API key.

**Do not rely on `GPT-3.5`**, whether `turbo` or standard, for more than just "sample" programs.
If you're aiming for more complex applications, GPT-4 is a must, preferably GPT-4-32k.

Using the OpenAI API might quickly exhaust your token limit.
For more extensive projects, Azure OpenAI API is recommended.

Be mindful of costs if you have ambitious goals! Always monitor what your agents are doing.
While AI can be a powerful tool, it isn't necessarily cheaper than hiring real developers — yet 🙄.


### Anaconda

```sh
conda create -n autogen python=3.10
conda activate autogen
pip install poetry
poetry install
cp env.sample.jsonc env.jsonc
```

1. You MUST copy (locally) [this tiny PR fix](https://github.com/microsoft/autogen/pull/47) to get the code to work.
   This won't be necessary once the PR is merged.
2. Edit both `env.json` and `constants.py` with your OpenAI API or Azure OpenAI API configuration.
3. Edit the end of `main.py` to customize your first instruction.

Then you can run it via:

```sh
make run
```

OADS will automatically generate the program source code in `./project` directory.

You can clean it via:

```sh
make clean
```
