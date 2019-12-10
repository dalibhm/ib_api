from kafka_fundamental_download_runner import KafkaFundamentalDownloadRunner
from kafka_historical_download_runner import KafkaHistoricalDownloadRunner


class KafkaDownloadRunnerBuilder:
    @staticmethod
    def create(services, args, config):
        if args.historical:
            download_runner = KafkaHistoricalDownloadRunner(services=services,
                                                            start_date=args.start_date, end_date=args.end_date,
                                                            stock_number=int(args.stock_number), config=config)
        elif args.fundamental:
            download_runner = KafkaFundamentalDownloadRunner(services=services, stock_number=int(args.stock_number),
                                                             config=config)
        return download_runner
