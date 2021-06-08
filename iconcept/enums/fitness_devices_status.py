class FitnessDeviceStatus:
    OFFLINE = 0
    STANDBY = 1
    RUNNING = 2
    PAUSED = 3

    @classmethod
    def get_status_description(cls, status: int) -> str:
        if status == cls.OFFLINE:
            return "Offline"
        if status == cls.STANDBY:
            return "Standby"
        if status == cls.RUNNING:
            return "Running"
        if status == cls.PAUSED:
            return "Paused"
