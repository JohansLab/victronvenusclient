# SPDX-FileCopyrightText: 2024-present Johan du Plessis https://github.com/johanslab
#
# SPDX-License-Identifier: MIT

"""Tests that devices and metrics can be enumerated."""

import pytest
import victronvenusclient  # pylint: disable=import-error


@pytest.mark.asyncio
async def test_devices_and_metrics(config_host, config_port, config_username, config_password, config_use_ssl):
    hub = victronvenusclient.Hub(config_host, config_port, config_username, config_password, config_use_ssl)
    await hub.connect()
    await hub.initialize_devices_and_metrics()

    assert len(hub.devices) > 0

    for device in hub.devices:
        assert len(device.metrics) > 0
        assert device.device_type is not None
        assert device.device_type != victronvenusclient.DeviceType.ANY

        for metric in device.metrics:
            assert len(metric.short_id) > 0

    await hub.disconnect()
