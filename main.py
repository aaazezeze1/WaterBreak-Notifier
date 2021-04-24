import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'Water Break',
            message = 'Drink Water!',
            app_icon = r'ur_icon_path.ico',
            timeout = 15,
        )
        time.sleep(1500)
        
        notification.notify(
            title = 'Take a Break',
            message = 'Take a break from what your doing right now',
            app_icon = r'ur_icon_path.ico',
            timeout = 15,
        )
        time.sleep(1500)
