# Developer Guide

This guide provides instructions for setting up a development environment, adding new commands, and running the bot locally.

## Development Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CycloneAddons/espotive-bot.git
    cd espotive-bot
    ```

2.  **Install Poetry:**
    ```bash
    pip install poetry
    ```

3.  **Install dependencies:**
    ```bash
    poetry install
    ```

4.  **Create a `config.py` file:**
    -   Copy the `src/example.config.py` file to `src/config.py`.
    -   Fill in the required values, such as your Discord bot token and other API keys.

## Adding a New Command

1.  **Create a new cog:**
    -   Cogs are located in the `src/cogs` directory. You can create a new Python file in an existing subdirectory or create a new one.
    -   Your cog class should inherit from `core.Cog`.

2.  **Add your command:**
    -   Use the `@commands.command()` decorator to define a new command.
    -   The command method should be asynchronous and take `ctx` (a `core.Context` object) as its first argument.

3.  **Load the cog:**
    -   Add the path to your new cog to the `EXTENSIONS` list in `src/config.py`. For example, if your cog is in `src/cogs/utility/my_cog.py`, you would add `cogs.utility.my_cog` to the list.

## Running the Bot Locally

1.  **Start the bot:**
    ```bash
    poetry run python start.py
    ```

2.  **Stopping the bot:**
    -   You can stop the bot by pressing `Ctrl+C` in the terminal.
