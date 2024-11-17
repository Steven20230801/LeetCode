import asyncio


async def fetch_data(x: str):
    print(f"Fetching data for {x}")
    await asyncio.sleep(2)  # Simulate a network request
    print(f"Data fetched for {x}")
    return {"data": x}


async def main():
    print("Main function started")
    data = await fetch_data("data1")
    data2 = await fetch_data("data2")
    print(f"Received data: {data}")
    print(f"Received data2: {data2}")


# Run the main function
asyncio.run(main())
