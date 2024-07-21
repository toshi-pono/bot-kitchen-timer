import asyncio
from dataclasses import dataclass
from aiotraq_message import TraqMessage


@dataclass
class TimerConfig:
    mm: int
    ss: int


def perse_command(command: str) -> TimerConfig | None:
    commands = command.strip().split(" ")
    if len(commands) >= 1 and commands[0] == "@BOT_KTimer":
        commands = commands[1:]

    # set mm:ss
    if len(commands) == 2 and commands[0] == "set":
        timer = commands[1]
        if ":" not in timer:
            return None
        mm, ss = timer.split(":")
        if not mm.isdigit() or not ss.isdigit():
            return None

        return TimerConfig(int(mm), int(ss))

    return None


async def component(am: TraqMessage, payload: str) -> None:
    message = payload

    config = perse_command(message)
    if config is None:
        am.write("""Invalid command
                 Usage:
                 @BOT_KTimer set mm:ss""")
        return

    mm = config.mm
    ss = config.ss
    first_count = 10
    delta = 1

    while ss > 0 or mm > 0:
        am.clear()
        am.write(f"$\\huge{mm:02}:{ss:02}$:loading:")

        # 最初は1秒ごとにカウント
        if first_count <= 0:
            delta = 10
        first_count -= 1

        # 最後の10秒は1秒ごとにカウント
        if mm == 0 and ss <= 10:
            delta = 1
        elif mm == 0 and ss < 20:
            delta = ss - 10

        await asyncio.sleep(delta)
        ss -= delta
        if ss < 0:
            ss = 60 + ss
            mm -= 1

    am.clear()
    am.write("$\\huge 時間です$")
