def generate_random_string(length=10):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def wait_for_element(page, selector, timeout=30000):
    from playwright.async_api import TimeoutError
    try:
        return page.wait_for_selector(selector, timeout=timeout)
    except TimeoutError:
        print(f"Element with selector '{selector}' not found within {timeout}ms.")
        return None

def log_message(message):
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")