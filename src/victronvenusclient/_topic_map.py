"""
Maps all the MQTT topics to either attributes or metrics.
"""

from victronvenusclient._unwrappers import unwrap_float, unwrap_int, unwrap_int_default_0, unwrap_string
from victronvenusclient.constants import DeviceType, MessageType, MetricNature, MetricType
from victronvenusclient.data_classes import TopicDescriptor

topic_map = {
    # generic device attributes
    "N/+/+/+/ProductName": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="model",
        unit_of_measurement=None,
        metric_type=None,
        metric_nature=None,
        precision=None,
        unwrapper=unwrap_string,
    ),
    "N/+/+/+/Serial": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="serial_number",
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=None,
        precision=None,
        unwrapper=unwrap_string,
    ),
    # inverter hides its serial number away in a different topic
    "N/+/vebus/+/Devices/0/SerialNumber": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="serial_number",
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=None,
        precision=None,
        unwrapper=unwrap_string,
    ),
    "N/+/+/+/Manufacturer": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="manufacturer",
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=None,
        precision=None,
        unwrapper=unwrap_string,
    ),
    "N/+/+/+/ProductId": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="victron_productid",
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=None,
        precision=0,
        unwrapper=unwrap_int,
    ),
    "N/+/+/+/FirmwareVersion": TopicDescriptor(
        message_type=MessageType.ATTRIBUTE,
        short_id="firmware_version",
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=None,
        precision=None,
        unwrapper=unwrap_string,
    ),
    # grid
    "N/+/system/+/Ac/Grid/NumberOfPhases": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="system_grid_phases",  # system attribute
        unit_of_measurement=None,
        metric_type=MetricType.NONE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=0,
        unwrapper=unwrap_int_default_0,
    ),
    # individual grid phases
    "N/+/grid/+/Ac/+/Voltage": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_voltage_{phase}",
        unit_of_measurement="V",
        metric_type=MetricType.VOLTAGE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/+/Current": TopicDescriptor(
        message_type="sensor",
        short_id="grid_current_{phase}",
        unit_of_measurement="A",
        metric_type=MetricType.CURRENT,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/+/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_power_{phase}",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    # total grid
    "N/+/grid/+/Ac/Voltage": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_voltage",
        unit_of_measurement="V",
        metric_type=MetricType.VOLTAGE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/Current": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_current",
        unit_of_measurement="A",
        metric_type=MetricType.CURRENT,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_power",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/Energy/Forward": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_energy_forward",
        unit_of_measurement="kWh",
        metric_type=MetricType.ENERGY,
        metric_nature=MetricNature.CUMULATIVE,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/grid/+/Ac/Energy/Reverse": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="grid_energy_reverse",
        unit_of_measurement="kWh",
        metric_type=MetricType.ENERGY,
        metric_nature=MetricNature.CUMULATIVE,
        device_type=DeviceType.GRID,
        precision=1,
        unwrapper=unwrap_float,
    ),
    #  cspell:ignore solarcharger MPPT
    # solar / MPPT  """ cspell:ignore  """
    "N/+/solarcharger/+/Dc/0/Voltage": TopicDescriptor(  # """ cspell:ignore  """
        message_type=MessageType.METRIC,
        short_id="solar_voltage",
        unit_of_measurement="V",
        metric_type=MetricType.VOLTAGE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SOLAR_CHARGER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/solarcharger/+/Dc/0/Current": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="solar_current",
        unit_of_measurement="A",
        metric_type=MetricType.CURRENT,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SOLAR_CHARGER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/solarcharger/+/Yield/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="solar_power",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SOLAR_CHARGER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/solarcharger/+/Yield/User": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="solar_yield",
        unit_of_measurement="kWh",
        metric_type=MetricType.ENERGY,
        metric_nature=MetricNature.CUMULATIVE,
        device_type=DeviceType.SOLAR_CHARGER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/solarcharger/+/History/Daily/0/MaxPower": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="solar_max_power",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SOLAR_CHARGER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    # batteries
    "N/+/battery/+/Dc/0/Voltage": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_voltage",
        unit_of_measurement="V",
        metric_type=MetricType.VOLTAGE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/Dc/0/Current": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_current",
        unit_of_measurement="A",
        metric_type=MetricType.CURRENT,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/Dc/0/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_power",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/Dc/0/Temperature": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_temperature",
        unit_of_measurement="°C",
        metric_type=MetricType.TEMPERATURE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/History/DischargedEnergy": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_discharged_energy",
        unit_of_measurement="kWh",
        metric_type=MetricType.ENERGY,
        metric_nature=MetricNature.CUMULATIVE,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/History/ChargedEnergy": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_charged_energy",
        unit_of_measurement="kWh",
        metric_type=MetricType.ENERGY,
        metric_nature=MetricNature.CUMULATIVE,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/Capacity": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_capacity",
        unit_of_measurement="Ah",
        metric_type=MetricType.ELECTRIC_STORAGE_CAPACITY,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/InstalledCapacity": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_installed_capacity",
        unit_of_measurement="Ah",
        metric_type=MetricType.ELECTRIC_STORAGE_CAPACITY,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/battery/+/Soc": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="battery_soc",
        unit_of_measurement="%",
        metric_type=MetricType.PERCENTAGE,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.BATTERY,
        precision=1,
        unwrapper=unwrap_float,
    ),
    # inverter
    "N/+/vebus/+/Ac/ActiveIn/+/P": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_input_power_{phase}",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/vebus/+/Ac/ActiveIn/+/F": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_input_frequency_{phase}",
        unit_of_measurement="Hz",
        metric_type=MetricType.FREQUENCY,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/vebus/+/Ac/ActiveIn/+/S": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_input_apparent_power_{phase}",
        unit_of_measurement="VA",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/vebus/+/Ac/Out/+/P": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_output_power_{phase}",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/vebus/+/Ac/Out/+/F": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_output_frequency_{phase}",
        unit_of_measurement="Hz",
        metric_type=MetricType.FREQUENCY,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/vebus/+/Ac/Out/+/S": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="inverter_output_apparent_power_{phase}",
        unit_of_measurement="VA",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.INVERTER,
        precision=1,
        unwrapper=unwrap_float,
    ),
    # integrated system. Note that this might not be currently accurate for all systems
    #  as there are different physical configurations
    # and don't have access to any other for testing or feedback.
    "N/+/system/+/Ac/ConsumptionOnOutput/+/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="system_critical_loads_{phase}",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SYSTEM,
        precision=1,
        unwrapper=unwrap_float,
    ),
    "N/+/system/+/Ac/ConsumptionOnInput/+/Power": TopicDescriptor(
        message_type=MessageType.METRIC,
        short_id="system_ac_loads_{phase}",
        unit_of_measurement="W",
        metric_type=MetricType.POWER,
        metric_nature=MetricNature.INSTANTANEOUS,
        device_type=DeviceType.SYSTEM,
        precision=1,
        unwrapper=unwrap_float,
    ),
}
