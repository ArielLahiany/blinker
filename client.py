"""
Manages the connections to a TwinCAT backend server.
"""

# Python modules
from logging import Logger

# PyAds modules
from pyads import Connection, PORT_TC3PLC1


def connect(logger: Logger, address: str = None, port: int = None):
    """
    A base function for a PLC connection over the ADS protocol.
    :param logger: The base logger of the module.
    :param address: Internet Protocol (IP) address.
    :param port: Internet Protocol (IP) port.
    :return: a PLC object for manipulation.
    """

    # Defines defaults for the connection.
    if (address and port) is None:
        address = "127.0.0.1.1.1"
        port = PORT_TC3PLC1

    # Creates a Connection object.
    try:
        plc = Connection(address, port)
    except ValueError:
        logger.error(
            msg="It is not a valid IP address.",
        )
    except FileNotFoundError:
        logger.error(
            msg="FileNotFoundError: Could not find module 'TcAdsDll.dll'."
        )
    else:
        try:
            plc.open()
        except plc is None:
            logger.error(
                "Backend server connection failed."
             )
        else:
            logger.info(
                msg="Backend server connection succeeded."
            )
            return plc
