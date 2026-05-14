import pyautogui
import time
import keyboard


class Cookieclicker():
    def __init__(self):
        self.GREEN_COLOR = (102, 255, 102)
        self.buldings_regions = [(1688, 360, 28, 10),
                                 (1689, 424, 23, 10),
                                 (1689, 488, 40, 10)]
        pyautogui.PAUSE = 0.3

    def check_for_buildings(self, region):
        img = pyautogui.screenshot(region=region)
        width, height = img.size

        for x in range(width):
            for y in range(height):
                if img.getpixel((x, y)) == self.GREEN_COLOR:
                    return region[0] + x, region[1] + y
        return None

    def start_browser(self, url="https://cookieclicker.com"):
        pyautogui.hotkey("win", "d")
        browser = pyautogui.locateCenterOnScreen("browser.png", confidence=0.9)
        if browser is not None:
            print("Browser image found successfully.")
            pyautogui.doubleClick(browser)
            time.sleep(1)
            pyautogui.click(445, 60)
            pyautogui.write(url, interval=0.01)
            pyautogui.press("enter")
            return True
        else:
            print("Image not found")
            return False

    def setup_game(self):
        time.sleep(2)
        cookie = pyautogui.locateCenterOnScreen("webcookie.png", confidence=0.9)
        if cookie is not None:
            print("Cookie image found successfully.")
            pyautogui.click(cookie)
        else:
            print("Cookie img not found")

        time.sleep(2)
        try:
            language = pyautogui.locateCenterOnScreen("english.png", confidence=0.9)

            if language is not None:
                print("Language image found successfully.")
                pyautogui.click(language)
        except: pass

    def start_game(self):
        time.sleep(2)
        try:
            while True:
                if keyboard.is_pressed('q'):
                    print("Program stopped by User")
                    break

                pyautogui.click(290, 500, clicks=1000, interval=0.02)

                for reg in self.buldings_regions:
                    position = self.check_for_buildings(reg)
                    if position:
                        print(f"Upgrade detected, Clicking...")
                        pyautogui.click(position)

                time.sleep(1)

        except KeyboardInterrupt:
            print("program stopped")


if __name__ == "__main__":
    bot = Cookieclicker()
    if bot.start_browser():
        bot.setup_game()
        bot.start_game()