import logging
import time
import os

from configuration.set_up import set_up
from download_manager.download_manager import DownloadManager


def main():
    """
    reads the configuration file
    connects to services
    run the DownloadRunner with the configuration requested
    :return: 
    """
    # configure logging
    if not os.path.exists("../log"):
        os.makedirs("../log")

    FORMAT = '%(asctime)-15s %(levelname)s %(name)-s:%(lineno)d %(message)s'
    logging.basicConfig(filename=time.strftime(os.path.join("../log", "runner_%Y%m%d_%H_%M_%S.log")),
                        filemode="w",
                        level=logging.DEBUG,
                        format=FORMAT)

    # 'fundamental': FundamentalService(config.get('services', 'fundamental_data'))

    # scope = Scope(stocks=args.stocks, exchanges=args.exchanges)

    injector = set_up()

    # run program

    download_manager = injector.get(DownloadManager)
    # runner_manager = KafkaDownloadRunnerFactory.create(services, args, config)
    download_manager.run()


if __name__ == '__main__':
    print('Runner starting...')
    main()
