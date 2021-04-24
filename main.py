import time
from plyer import notification

# Notifications
if __name__ == '__main__':
    while True:
    # def notifsWater():
        notification.notify(
            title = 'Water Break',
            message = 'Drink Water!',
            app_icon = r'C:\Users\Amazing\Documents\PyCharm\Mono\src\water.ico',
            timeout = 15,
        )
        time.sleep(1500)

    # def notifsBreak():
        notification.notify(
            title = 'Take a Break',
            message = 'Take a break from what your doing right now',
            app_icon = r'C:\Users\Amazing\Documents\PyCharm\Mono\src\break.ico',
            timeout = 15,
        )
        time.sleep(1500)
