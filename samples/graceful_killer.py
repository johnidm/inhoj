import time
from inhoj.classes import GracefulDeath
from inhoj.contexts import gracefuldeath


if __name__ == '__main__':
    pass

    #
    #
    
    @gracefuldeath("Killing...")
    def run():
        print('running...')

    while True:
        run()

    # while True:
    #   with gracefuldeath():
    #       print('processing...')

    # killer = GracefulDeath()
    # killer = GracefulDeath('Killing...')
    # while True:
    #     time.sleep(1)
    #     print("doing something in a loop ...")
    #     if killer.kill_now:
    #         break # or sys.exit(0)

    # print("End of the program. I was killed gracefully :)")
