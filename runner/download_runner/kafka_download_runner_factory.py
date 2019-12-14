from download_runner.impl.kafka_fundamental_download_runner import KafkaFundamentalDownloadRunner
from download_runner.impl.kafka_historical_download_runner import KafkaHistoricalDownloadRunner


class KafkaDownloadRunnerFactory:
    @staticmethod
    def create(services, args, config):
        if args.historical:
            download_runner = KafkaHistoricalDownloadRunner(services=services,
                                                            start_date=args.start_date, end_date=args.end_date,
                                                            config=config)
        elif args.fundamental:
            download_runner = KafkaFundamentalDownloadRunner(services=services,
                                                             config=config)
        return download_runner
