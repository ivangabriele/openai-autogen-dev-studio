# OADS - OpenAI Autogen Development Studio

Generate games and programs using OpenAI agents. Built on top of [Microsoft Autogen](https://github.com/microsoft/autogen).

> ⚠️ **Work In Progress**  
> The current code works but:
> - It needs some cleaning up.
> - Enhancements can be made with better prompt engineering and the addition of more agents.
> - Microsoft Autogen is still in its early stages contain a few bugs.

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
#### 2/3 Mandatory Autogen Fixes

First edit your local installed `autogen` to apply [this tiny PR fix](https://github.com/microsoft/autogen/pull/47)

Then, in the same file (`agentchat/conversable_agent.py`), edit `generate_oai_reply()` method like that:

```diff
    def generate_oai_reply(
        self,
        messages: Optional[List[Dict]] = None,
        sender: Optional[Agent] = None,
        config: Optional[Any] = None,
    ) -> Tuple[bool, Union[str, Dict, None]]:
        """Generate a reply using autogen.oai."""
        llm_config = self.llm_config if config is None else config
        if llm_config is False:
            return False, None
        if messages is None:
            messages = self._oai_messages[sender]
+       else:
+           for message in messages:
+               message.setdefault('content', "")

```

#### 3/3 Configuration

Edit your `env.json` to add your API keys and customize your installation.

#### Run

Just:

```sh
make run
```

OADS will automatically generate the program source code in `./project` directory.

You can clean it via:

```sh
make clean
```
