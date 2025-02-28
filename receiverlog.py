import logging
import json
import os
import re
from datetime import datetime

Receiver_logfilepath='Receiver_Process_logfile.log'

# Set up logging configuration
logging.basicConfig(
    filename=Receiver_logfilepath,  # Specify the path to your log file
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class Receiver_Process:
    # print('In Receiver_Process')
    
    logger = logging.getLogger("Receiver_Process")
    
    file_path = "sensor_data.json"
    
    Var = [{'DeviceID': '89203lh6hh10', 'type': 'apf', 'STATE': '1', 'fanSpeed': 'Hi', 'req_type': 'status', 'validity': '55', 'power_consumed': '0.91', 'min_power': '0.02', 'prvn': '1', 'hotspot': 0, 'timstamp': 954553},
           {'CO2': '1018', 'DeviceID': '174f63ddf608', 'Fan_Speed': 'Off', 'Hotspot': '0', 'hum': '38', 'pm10': '7', 'pm25': '21', 'temp': '81', 'type': 'Sensor_C', 'voc': '197', 'timstamp': 191655717},
           {'DeviceID': '80FA811C0610', 'type': 'apf', 'STATE': '2', 'fanSpeed': 'Hi', 'req_type': 'status', 'validity': '55', 'power_consumed': '0.91', 'min_power': '0.02', 'prvn': '1', 'hotspot': 0, 'timstamp': 489419},
           {'DeviceID': '5812BE1FB608', 'type': 'apf', 'STATE': '0', 'fanSpeed': 'Off', 'req_type': 'status', 'validity': '4080', 'power_consumed': '0.00', 'min_power': '0.00', 'prvn': '0', 'hotspot': 0, 'timstamp': 176},
           {'CO2': '1018', 'DeviceID': '1042BD1FB608', 'Fan_Speed': 'Off', 'Hotspot': '0', 'hum': '38', 'pm10': '7', 'pm25': '21', 'temp': '81', 'type': 'Sensor_C', 'voc': '197', 'timstamp': 8593301},
           {'DeviceID': '10FA811C0610', 'type': 'apf', 'STATE': '3', 'fanSpeed': 'Hi', 'req_type': 'status', 'validity': '56', 'power_consumed': '0.92', 'min_power': '0.02', 'prvn': '1', 'hotspot': 0, 'timstamp': 593303},
           ]
    
    for data in Var:
        # print(f"Data -  {data}")
        logger.info(f"Data - {data}")
    
          
    #Function to read the log file and filter Sensor_C type data
    # def get_sensor_c_data_from_log(logfile):
    #     sensor_c_data = []
    #     with open(logfile, 'r') as file:
    #         for line in file:
    #             if 'Sensor_C' in line:
    #                 sensor_c_data.append(line.strip())
    #     return sensor_c_data
    
    # def get_sensor_c_data_from_log(logfile):
    #     sensor_c_data = []
    #     with open(logfile, 'r') as file:
    #         for line in file:
    #             if 'Sensor_C' in line:
    #                 # Extract the JSON part from the log line
    #                 match = re.search(r'\{.*\}', line)
    #                 if match:
    #                     sensor_c_data.append(json.loads(match.group()))
    #     return sensor_c_data
    
    def get_sensor_c_data_from_log(logfile):
        sensor_c_data = []
        timestamp  = []
        with open(logfile, 'r') as file:
            for line in file:
                if 'Sensor_C' in line:
                    print(f"Line : {line}")
                    
                    
                    # Extract the timestamp
                    DateandTime = line.split(' - ')[0]
                    #print(f"Timestamp: {DateandTime}")
                    
                    # Convert the timestamp to datetime object
                    datetime_obj = datetime.strptime(DateandTime, "%Y-%m-%d %H:%M:%S,%f")
                    
                    # Get the timestamp in seconds
                    timestamp.append(datetime_obj.timestamp())
                    # timestamp = datetime_obj.timestamp()
                    print(f"Timestamp in seconds: {timestamp}")
                    
                    # Extract the JSON part from the log line
                    match = re.search(r'\{.*\}', line)
                    
                    if match:
                        try:
                            # Ensure the extracted string is a valid JSON string
                            json_str = match.group()
                            
                            # Replace single quotes with double quotes
                            json_str = json_str.replace("'", '"')
                            
                            # Parse the JSON string
                            sensor_c_data.append(json.loads(json_str))
                            
                            # for datasec in sensor_c_data:
                            #     print(f"datasec : {datasec}")
                            #     if 'timstamp' in datasec:
                            #         datasec['timstamp'] = int(timestamp*1000)
                            
                            for datasec in range(len(sensor_c_data)):
                                print(f"index : {datasec} {sensor_c_data[datasec]}")
                                if 'timstamp' in sensor_c_data[datasec]:
                                    sensor_c_data[datasec]['timstamp'] = int(timestamp[datasec]*1000)      
                                
                        except Exception as e:
                            # Log the error and the problematic line
                            logging.error(f"Failed to decode JSON from line: {line}")
                            logging.error(f"Error: {e}")
        return sensor_c_data

    # Get Sensor_C data from log file
    sensor_d_data = get_sensor_c_data_from_log(Receiver_logfilepath)
    for entry in sensor_d_data:
        print(f'entry : {entry}') 
        
        
    def store_sensor_c_data(data,path):
        with open(path,'w') as fff:
            json.dump(data,fff,indent=4)
            
                    
    store_sensor_c_data(sensor_d_data,file_path)
