import logging
from pyats import aetest

# Get the logger instance for the current module
logger = logging.getLogger(__name__)

class SCPExample(aetest.Testcase):

    @aetest.setup
    def setup(self, testbed):
        # Connect to the device defined in the testbed YAML file
        self.device = testbed.devices['my_router']
        self.device.connect()

    @aetest.test
    def transfer_file_to_device(self):
        # Define SCP parameters
        username = 'myuser'
        server_ip = '10.1.1.100'
        remote_path = '/path/to/remote/file.txt'
        local_path = 'local_file.txt'
        device_destination = 'harddisk:file.txt' # Example for Cisco IOS XR

        # The SCP command as executed on the *device*
        scp_command = f'scp {username}@{server_ip}:{remote_path} {device_destination}'

        # Execute the command using the device connection
        logger.info(f"Executing SCP command: {scp_command}")
        try:
            output = self.device.execute(scp_command)
            logger.info("SCP successful. Output:")
            logger.info(output)
        except Exception as e:
            logger.error(f"SCP failed: {e}")
            self.failed("Failed to SCP file to the device")

    @aetest.cleanup
    def cleanup(self):
        self.device.disconnect()
