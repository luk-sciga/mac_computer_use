import asyncio
from pathlib import Path

from dotenv import load_dotenv

from loop import SYSTEM_PROMPT
from streamlit_file import main, st_session_state

load_dotenv()


async def run():
    p = "actions_1.txt"
    path = Path(p)
    with path.open("r") as f:
        contents = f.read()

    print(contents)
    st_session_state["messages"] = [
        {
            "role": "assistant",
            "content": SYSTEM_PROMPT,
        },
        {
            "content": contents,
            "role": "user"
        }]

    await main()


if __name__ == "__main__":
    asyncio.run(run())
