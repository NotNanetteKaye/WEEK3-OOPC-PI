class AlarmClock: 
    def __init__(self):
        self.current_time = ''
        self. alarm_status = 1  # 1 means alarm is on
        self.alarm_alert = ''
        pass

    def change_current_time(self):
        #  I want the AlarmClock class to have a 
        #  method to set (or change) the current time and print to the console the current time.
        pass

    def toggle_alarm(self):
        user_input = input('Updating alarm status! Press 1 for on or 2 for off: ')
        if user_input == '1' or user_input == '2':
            if user_input == '1':
                print('Alarm status is on')
            elif user_input == '2':
                self.alarm_status += 1
                print('Alarm status is off')
        else:
            print('invalid option. try again')
            self.toggle_alarm()     
        pass

    def set_current_alarm_time(self):
        # I want the AlarmClock class 
        # to have a method to set the current alarm time 
        # and print to the console the current alarm time
        pass

# https://docs.google.com/document/d/1qe-YBxgL7rM4k-Pmpp3jyHY3XIDS9Hs0/edit