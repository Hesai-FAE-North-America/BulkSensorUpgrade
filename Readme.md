Initial repo for new python3 script to perform sw/fw upgrades on 6 sensors at once. 
Required Steps:
1. Must be able to change IP addresses on Sensor ( Sensors ship with same address and need to be customized to work in parallel)
2. Verify address change
3. Start fw/sw upgrade on 6 sensors and have this run in parallel ( threads?)
4. Confirm Upgrade finished successfully. 
5. Pull sensor configuration information and store in a unique file name
6. Change back IP address to default. 
