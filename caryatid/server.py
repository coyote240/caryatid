import os
import signal
import asyncio
import functools


def exit_server(signame):
    print('Exiting on signal {}'.format(signame))
    loop.stop()


loop = asyncio.get_event_loop()

for signame in ('SIGINT', 'SIGTERM'):
    loop.add_signal_handler(getattr(signal, signame),
                            functools.partial(exit_server, signame))


def main():
    print('Server running at pid: {}'.format(os.getpid()))
    try:
        loop.run_forever()
    finally:
        loop.close()
