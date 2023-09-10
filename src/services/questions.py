import aiohttp


async def get_topics():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="http://127.0.0.1:8000/topics") as response:
            result = await response.json()
    return result


async def get_questions():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="http://127.0.0.1:8000/questions") as response:
            result = await response.json()
    return result
