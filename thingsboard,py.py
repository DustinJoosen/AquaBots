import logging
import time
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
from grove.grove_servo import GroveServo

# Configuration of logger, in this case it will send messages to console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger(__name__)

thingsboard_server = 'localhost:8080'
access_token = '4k1q85v7h544t6d6ki17'


def main():

    # Grove - Servo connected to PWM port
    servo = GroveServo(12)
    servo_angle = 90

    # Callback for server RPC requests (Used for control servo and led blink)
    def on_server_side_rpc_request(client, request_id, request_body):
        log.info('received rpc: {}, {}'.format(request_id, request_body))
        if request_body['method'] == 'getLedState':
            client.send_rpc_reply(request_id, light_state)
        elif request_body['method'] == 'setLedState':
            light_state = request_body['params']
            button.led.light(light_state)
        elif request_body['method'] == 'setServoAngle':
            servo_angle = float(request_body['params'])
            servo.setAngle(servo_angle)
        elif request_body['method'] == 'getServoAngle':
            client.send_rpc_reply(request_id, servo_angle)

    # Connecting to ThingsBoard
    client = TBDeviceMqttClient(thingsboard_server, access_token)
    client.set_server_side_rpc_request_handler(on_server_side_rpc_request)
    client.connect()


if __name__ == '__main__':
    main()
