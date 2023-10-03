# OADS - OpenAI Autogen Development Studio

Generate games and programs using OpenAI agents. Built on top of [Microsoft Autogen](https://github.com/microsoft/autogen).

> ⚠️ **Work In Progress**  
> The current code works but:
> - A lot of thing need to be optimized in order to drastically reduce tokens usage:
    caching, steps-by-step process, conversation splitting, better prompts.
> - The code needs some cleaning up.
> - Microsoft Autogen is still in early stage and contains a few bugs.
> - A lot of hard-coded stuff could be customizable via config files.
> - I will only focus on a few programming languages at first.

## Why this project?

There are some amazing projects doing similar things but I hope to find a way to solve ambitious programs generation.

## Getting Started

### Pre-requisites

You either need an OpenAI API key or an Azure OpenAI API key.

**Do not rely on `GPT-3.5`**, whether `turbo` or standard, for more than just "sample" programs.
If you're aiming for more complex applications, `GPT-4` is a must, preferably even `GPT-4-32k`.

Using the OpenAI API might quickly exhaust your token limit.
For more extensive projects, Azure OpenAI API is recommended.

**Be mindful of costs** if you have ambitious goals! Always monitor tokens usage and what your agents are doing.
While AI can be a powerful tool, it isn't necessarily cheaper than hiring real developers — yet 🙄.

### Anaconda

#### 1/3 Installation

```sh
conda create -n autogen python=3.10
conda activate autogen
pip install poetry
poetry install
cp env.sample.jsonc env.jsonc
```

#### 2/3 Configuration

Edit your `env.json` to add your API keys and customize your installation.

#### 3/3 Run

Just:

```sh
make run
```

OADS will automatically generate the program source code in `./project` directory.

You can clean it via:

```sh
make clean
```
