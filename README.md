# OADS - OpenAI Autogen Development Studio

Generate games and programs using OpenAI agents. Built on top of [Microsoft Autogen](https://github.com/microsoft/autogen).

> ⚠️ **Work In Progress**  
> The current code works but:
> - **THERE ARE, AND THERE WILL BE, BREAKING CHANGES:**
>   - Always check that your hidden `.env.jsonc` file match the last `env.sample.jsonc` structure.
>   - Always update your dependencies via `poetry install`.
> - A lot of thing need to be optimized in order to drastically reduce tokens usage:
    caching, steps-by-step process, conversation splitting, better prompts.
> - The code needs some cleaning up.
> - Microsoft Autogen is still in early stage and contains a few bugs.
> - A lot of hard-coded stuff could be customizable via config files.
> - I will only focus on a few programming languages at first.

---

- [Why this project?](#why-this-project)
- [Getting Started](#getting-started)
  - [Pre-requisites](#pre-requisites)
  - [Anaconda](#anaconda)
    - [1/3 Installation](#13-installation)
    - [2/3 Configuration](#23-configuration)
    - [3/3 Run](#33-run)
- [Open Source LLMs](#open-source-llms)
  - [1/2 Run Text generation web UI](#12-run-text-generation-web-ui)
  - [2/2 Setup OADS](#22-setup-oads)

---

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

## Open Source LLMs

**IMPORTANT: Functions will NOT work.**

### 1/2 Run Text generation web UI

From what I tested, Autogen seems to work with any Open Source LLM
supported by [Text generation web UI](https://github.com/oobabooga/text-generation-webui#text-generation-web-ui).

You just have to enable `openai` extension in "Session" tab of the web UI:

![Text generation web UI screenshot](/docs/images/tgwui-screenshot.png)

Be sure to have your `5001` port open or binded if it's a remote server
since this is where the OpenAI-like API will be exposed.

I personally deploy my current models on [RunPod](https://www.runpod.io) (not affiliated)
and use `thebloke/cuda11.8.0-ubuntu22.04-oneclick:latest` image
even though I think it seems a bit outdated regarding llama.cpp & co.

### 2/2 Setup OADS

```jsonc
  "models": [
    // Custom deployment of (for example) `Open-Orca/Mistral-7B-OpenOrca`
    // using "Text generation web UI" with `OpenAI` extension enabled:
    // https://github.com/oobabooga/text-generation-webui/tree/main/extensions/openai#an-openedai-api-openai-like
    // This can be any inference endpoint compatible following OpenAI API specs,
    // regardless of the model you use behind it.
    {
      "model": "Open-Orca/LlongOrca-13B-16k",
      "api_base": "http://localhost:5001", // Or your remote server URL
      "api_key": "sk-111111111111111111111111111111111111111111111111",
      "api_type": "open_ai"
    }
  ],
```
