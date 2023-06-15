import aiohttp
import asyncio
from typing import List, Tuple
import time
import psutil


def multy_async_func_test(func):
    async def wrapper(*args, **kwargs):
        process = psutil.Process()

        start_cpu_usage = process.cpu_percent()

        memory_info = process.memory_info()
        start_memory = memory_info.rss

        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 100
        print(f"Время выполнения функции {func.__name__} за 100к запросов: {execution_time} секунд")

        memory_info = process.memory_info()
        end_memory = memory_info.rss
        memory_usage = (end_memory - start_memory) / 1024 / 1024
        print(f"Затраты памяти: {memory_usage} МБ")

        end_cpu_usage = process.cpu_percent()
        cpu_usage = end_cpu_usage - start_cpu_usage
        print(f"Затраты процессора: {cpu_usage}%")
        return result
    return wrapper

async def fetch_status(session: aiohttp.ClientSession, url: str) -> Tuple[str, int]:
    async with session.head(url) as response:
        return url, response.status

@multy_async_func_test
async def fetch_all_status(urls: List[str]) -> List[Tuple[str, int]]:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_status(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results
    
async def main():

    urls: List[str] = []

    for i in range(1000):
        urls.append("http://google.com")

    results: List[Tuple[str, int]] = await fetch_all_status(urls)

    #for url, status in results:
    #print(f"URL: {url}, Status: {status}")

    # Время: 418.35484504699707 сек
    # Затраты памяти: 6.2578125 МБ
    # Затраты процессора: 8.2%

asyncio.run(main())