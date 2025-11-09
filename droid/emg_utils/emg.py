import abc
from typing import Any, Dict, List, Tuple


class EMG(abc.ABC):

    def __init__(self):
        """Initialize the EMG device with the given configuration.

        Args:
            config: Configuration dictionary containing device settings.
        """
        self.sampling_rate = 200
        self.channels = 8
        self.position = "lower"
        self.connected = False
        self.window_length = 100

    @property
    @abc.abstractmethod
    def is_connected(self) -> bool:
        """Check if the EMG device is currently connected.

        Returns:
            bool: True if the EMG device is connected, False otherwise.
        """
        pass

    @abc.abstractmethod
    def connect(self) -> None:
        """Establish connection to the EMG device.

        This method should handle any necessary setup or initialization
        required to start capturing EMG data.
        """
        pass

    @abc.abstractmethod
    def read(self) -> Tuple[int, ...]:
        """Capture and return a single EMG data frame at a single time point

        Returns:
            Tuple[int, ...]: Captured EMG data as a tuple of ints.
        """
        pass

    @abc.abstractmethod
    def disconnect(self) -> None:
        """Disconnect the EMG device.

        This method should handle any necessary cleanup or shutdown procedures
        when the EMG device is no longer needed.
        """
        pass