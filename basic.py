#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    # setup bt connection
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.debug("Bye")
