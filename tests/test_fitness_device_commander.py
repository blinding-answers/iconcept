from .fakes.channel import Channel
from iconcept.fitness_device_commander import FitnessDeviceCommander
from iconcept.enums.fitness_device_mode import FitnessDeviceMode


def test_init_command():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.init()

    commands = [
        "550C01FF",
        "55BB01FF",
        "552401FF",
        "552501FF",
        "552601FF",
        "552701FF",
        "550201FF",
        "550301FF",
        "550401FF",
        "550601FF",
        "551F01FF",
        "55A001FF",
        "55B001FF",
        "55B201FF",
        "55B301FF",
        "55B401FF",
        "55B501FF",
        "55B601FF",
        "55B701FF",
        "55B801FF",
        "55B901FF",
        "55BA01FF",
        "550B01FF",
        "551801FF",
        "551901FF",
        "551A01FF",
        "551B01FF",
    ]
    assert ''.join(commands) == channel.last_command


def test_reset_command():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.reset()
    assert "550A0102" == channel.last_command


def test_start_command():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.start()
    assert "550A0101" == channel.last_command


def test_pause_command():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.pause()
    assert "550A0100" == channel.last_command


def test_stop_command():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.stop()
    assert "550A0103" == channel.last_command


def test_enable_start_key():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.enable_start_key()
    assert "55080101" == channel.last_command


def test_set_speed():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.set_speed(15.32)
    assert "5521020F20" == channel.last_command
    commander.set_speed(0)
    assert "5521020000" == channel.last_command


def test_set_incline():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.set_incline(5)
    assert "55110105" == channel.last_command
    commander.set_incline(10)
    assert "5511010A" == channel.last_command
    commander.set_incline(15)
    assert "5511010F" == channel.last_command


def test_set_action_mode():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.set_action_mode(FitnessDeviceMode.DEFAULT)
    assert "55150100" == channel.last_command
    commander.set_action_mode(FitnessDeviceMode.HRC)
    assert "55150101" == channel.last_command
    commander.set_action_mode(FitnessDeviceMode.WATT)
    assert "55150102" == channel.last_command


def test_query_manufacturer():
    channel = Channel()
    commander = FitnessDeviceCommander(channel=channel)
    commander.query_manufacturer()
    assert "55B401FF" == channel.last_command
