Smart Poultry Farm IoT Project Documentation
1. Introduction
The Smart Poultry Farm IoT Project aims to automate climate control in poultry farms to ensure a healthy and optimal environment for the birds. Using a combination of temperature, humidity, and ammonia sensors, the system automatically adjusts the farm's conditions. The Django server enables farmers to monitor and control these parameters remotely.

2. Problem Statement
Maintaining a healthy climate inside poultry farms is critical for bird health and productivity. Variations in temperature, humidity, and ammonia levels can lead to disease and poor growth. This system addresses these challenges by providing real-time control and monitoring of environmental conditions, ensuring that optimal thresholds are maintained without constant manual intervention.

3. System Overview
The system comprises hardware and software components that work together to monitor and control the environment of a poultry farm. Farmers interact with the system through a web interface where they can monitor live data and set thresholds.

Main Features:
Temperature control through fans and heaters.
Humidity control through humidifiers and exhaust fans.
Ammonia level monitoring and control through exhaust fans.
4. System Architecture
4.1 Hardware Components:
ESP32 Controller: The central unit that reads sensor data and controls devices.
DHT22 Sensor: Measures temperature and humidity.
MQ3 Gas Sensor: Monitors ammonia levels in the air.
60W Bulb (Heater): Provides heat when the temperature is too low.
5V DC Cooling and Exhaust Fans: Used for cooling and air circulation.
2-Channel 5V Relays: Switches for controlling fans, heater, and humidifier.
4.2 Software Components:
Django Framework: Backend server to handle requests, data storage, and user authentication.
Arduino IDE: Used to program the ESP32 controller.
MQTT (HiveMQ): Protocol for communication between the ESP32 and the Django server.
HiveMQ: MQTT broker for device-server communication.
5. Key Functionalities
5.1 Temperature Control:
Users can set temperature thresholds on the web interface.
If the temperature exceeds the higher threshold, the cooling fan turns on.
If the temperature drops below the lower threshold, the heater (bulb) is activated.
5.2 Humidity Control:
Users can set humidity thresholds.
If the humidity exceeds the upper threshold, the exhaust fan turns on.
If the humidity drops below the lower threshold, the humidifier is activated.
5.3 Ammonia Control:
Ammonia levels are monitored using the MQ3 sensor.
If ammonia levels exceed the threshold, the exhaust fan is turned on for ventilation.
6. Data Flow and Communication
6.1 Data Publishing (ESP32):
The ESP32 controller collects temperature, humidity, and ammonia data from the sensors and publishes the data to an MQTT topic in JSON format.

##
<tab><tab>code/text here
doc["deviceId"] = "ESP32";
doc["siteId"] = "My Demo Lab";
doc["humidity"] = humidity;
doc["temperature"] = temperature;
doc["mq3Value"] = mq3Value;

serializeJson(doc, mqtt_message, sizeof(mqtt_message));
publishMessage("esp32_data", mqtt_message, true);
6.2 Data Processing (Django):
A Python script running on the Django server subscribes to the MQTT topic and stores the sensor data in a database.

python
Copy code
class SensorData(models.Model):
    device = models.ForeignKey(DeviceData, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    gas_sensor = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
6.3 Threshold Setting:
Farmers can set the desired thresholds for temperature, humidity, and ammonia levels via a web form. These values are published to MQTT and processed by the ESP32.


payload = json.dumps({
    'deviceId': threshold_data.device.tag,
    'temperature_max': threshold_data.highest_temperature_level,
    'temperature_min': threshold_data.lowest_temperature_level,
    'humidity_max': threshold_data.highest_humidity_level,
    'humidity_min': threshold_data.lowest_humidity_level,
    'ammonia_max': threshold_data.highest_ammonia_level,
})
client.publish(MQTT_THRESHOLD_TOPIC, payload)
7. User Interaction
7.1 Web Interface:
Users interact with the system through a Django-powered web interface. They can:

Log in using Django's built-in authentication.
View live sensor data (temperature, humidity, and ammonia) on the dashboard.
Set custom thresholds for climate control.
Visualize historical data via graphs for each sensor.
8. Data Visualization
The system offers two modes of data visualization:

Live Meters: Display the current temperature, humidity, and ammonia levels.
Historical Graphs: Show the trends over time for temperature, humidity, and ammonia levels.
9. Installation and Setup
Users do not need to install or configure any hardware or software. The setup is handled by the development team. However, for development purposes, the following tools are used:

VSCode: For editing code.
Arduino IDE: For programming the ESP32.
Django: For backend development.
MQTT (HiveMQ): For device-server communication.
10. Challenges and Considerations
Connectivity Issues:
If the device loses its connection to Wi-Fi, it cannot communicate with the server, and the real-time data may be delayed.
Security:
Users must protect their credentials to ensure the security of their accounts and data.
11. Use Cases
Scenario 1: Poultry Farms
Farmers can monitor and control the climate of their poultry farm remotely, ensuring optimal growth conditions for their flock.

Scenario 2: Indoor Plant Farming
The system can be adapted for indoor plant farming, maintaining humidity and temperature to ensure healthy plant growth.

Scenario 3: Mushroom Farming
Mushroom farms, which require precise environmental conditions, can benefit from automated climate control.

12. Conclusion
The Smart Poultry Farm IoT system enhances the farming experience by providing remote monitoring and control over key environmental factors. This ensures a healthier and more productive environment for poultry or other livestock.
