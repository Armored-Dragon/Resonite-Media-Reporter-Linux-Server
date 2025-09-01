import asyncio
import websockets
from playerctl import PlayerctlClass
playerctl = PlayerctlClass()

async def get_music_from_music_player():
    return playerctl.get_music_metadata()

async def echo(websocket):
    try:
        async for message in websocket:
            if (message == "GetCurrentlyPlayingMedia"):
                try:
                    await websocket.send(await get_music_from_music_player())
                finally:
                    return
    finally:
        return False

async def main():
    if not playerctl.check():
        print("playerctl is not installed.")
        exit(0)

    async with websockets.serve(echo, "localhost", 8081):
        await asyncio.Future()

asyncio.run(main())
