import asyncio

from viam.components.base import Base
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


SECRET = '' # make sure to place the secret value inside of the single quotes
REMOTE_ADDRESS = '' # likewise for the remote address


"""
The connect function establishes a network connection between Codespace host and the robot.
"""
async def connect():
  creds = Credentials(type='robot-location-secret', payload=SECRET)
  opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds))
  return await RobotClient.at_address(REMOTE_ADDRESS, opts)

            
"""
The move_in_square function contains the code that moves the robot, executing a sequence
of spin and move_straight commands that drives the robot in a square.
"""
async def move_in_square(base):
  for _ in range(4):
    # moves the rover forward 500mm at 500mm/s
    await base.move_straight(velocity=500, distance=500)
    print("move straight")
    # spins the rover 90 degrees at 100 degrees per second
    await base.spin(velocity=100, angle=90)
    print("spin 90 degrees")


"""
The main function is the one called upon script execution. It sets up and calls the
two other functions.
"""
async def main():
  robot = await connect()
  base = Base.from_robot(robot, 'viam_base')
  await move_in_square(base)

  # Don't forget to close the robot when you're done!
  await robot.close()


if __name__ == '__main__':
  asyncio.run(main())
