import asyncio
import heapq
import random
import time
import yfinance as yf


class Subscriber:
    def __init__(self, user_id, stock_symbol, threshold, priority, direction="up"):
        self.user_id = user_id
        self.stock_symbol = stock_symbol
        self.threshold = threshold  # 涨跌幅阈值
        self.priority = priority  # 优先级，数值越小优先级越高
        self.direction = direction  # 'up'表示涨幅，'down'表示跌幅，'both'表示两者

    def __lt__(self, other):
        return self.priority < other.priority


# 存储每个股票的上一周期价格
stock_prices = {}

notification_queue = []


async def get_stock_price(symbol):
    try:
        # stock = yf.Ticker(symbol)
        # data = stock.history(period="1d")
        # return data["Close"].iloc[-1]
        # 模擬價格
        return random.randint(100, 200)
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return stock_prices.get(symbol, 0)  # 返回上次的价格，避免系统崩溃


def should_notify(subscriber, change_percentage):
    if subscriber.direction == "up" and change_percentage >= subscriber.threshold:
        return True
    elif subscriber.direction == "down" and change_percentage <= -subscriber.threshold:
        return True
    elif subscriber.direction == "both" and abs(change_percentage) >= subscriber.threshold:
        return True
    else:
        return False


async def process_subscriber(subscriber):
    symbol = subscriber.stock_symbol
    current_price = await get_stock_price(symbol)

    # 获取 old_price，如果不存在，则初始化为 current_price
    old_price = stock_prices.get(symbol, current_price)

    # 计算涨跌幅
    if old_price == 0:
        change_percentage = 0
    else:
        change_percentage = ((current_price - old_price) / old_price) * 100

    # 判断是否需要通知
    if should_notify(subscriber, change_percentage):
        heapq.heappush(notification_queue, (subscriber.priority, subscriber, change_percentage, symbol))

    # 更新 old_price 为 current_price
    stock_prices[symbol] = current_price


async def check_and_notify(subscribers):
    tasks = [asyncio.create_task(process_subscriber(sub)) for sub in subscribers]
    await asyncio.gather(*tasks)


def process_notifications():
    while notification_queue:
        _, subscriber, change_percentage, symbol = heapq.heappop(notification_queue)
        send_notification(subscriber, change_percentage, symbol)


def send_notification(subscriber, change_percentage, symbol):
    if change_percentage >= 0:
        change_type = "涨幅"
    else:
        change_type = "跌幅"
    message = f"用户{subscriber.user_id}，您好！股票{symbol}的{change_type}已达到" f"{abs(change_percentage):.2f}%。"
    print(message)


def initialize_stock_prices(subscribers):
    for subscriber in subscribers:
        symbol = subscriber.stock_symbol
        if symbol not in stock_prices:
            stock_prices[symbol] = 0  # 初始化为0，实际会在第一次获取价格时更新


async def main():
    subscribers = [
        # Subscriber(user_id=2, stock_symbol="GOOG", threshold=3, priority=2, direction="down"),
        Subscriber(user_id=1, stock_symbol="AAPL", threshold=2, priority=1, direction="up"),
        Subscriber(user_id=2, stock_symbol="AAPL", threshold=2, priority=2, direction="up"),
        # Subscriber(user_id=3, stock_symbol="TSLA", threshold=5, priority=1, direction="both"),
    ]

    initialize_stock_prices(subscribers)

    step = 0
    while True and step < 100:
        await check_and_notify(subscribers)
        process_notifications()
        await asyncio.sleep(1)  # 每10秒检查一次


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("系统终止。")
