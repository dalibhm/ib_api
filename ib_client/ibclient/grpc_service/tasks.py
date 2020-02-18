import asyncio


async def request_fundamental_data(request):
    try:
        self.logger.notice('Starting fundamental request: {} {}'.format(request.contract.symbol,
                                                                        request.reportType))
        # self.request_manager.add_request(request, RequestType.Fundamental)
        task = self.request_manager.add_request(request, RequestType.Fundamental)
        status = await asyncio.run(task)
        self.logger.notice('Processed fundamental request: {} {}'.format(request.contract.symbol,
                                                                         request.reportType))
    except asyncio.TimeoutError:
        self.logger.notice('Timeout historical request: {} {}'.format(request.contract.symbol,
                                                                      request.reportType))
        status = False
    except Exception as e:
        self.logger.exception('Request: {} {}'.format(request.contract.symbol,
                                                      request.reportType))
        status = False

    return request_data_pb2.Status(message=status)
