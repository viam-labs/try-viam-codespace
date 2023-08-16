import asyncio

from viam.components.base import Base
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


SECRET_FROM_VIAM_APP = '' # todo: replace with secret in 'Security' tab on the Viam app
ADDRESS_FROM_VIAM_APP = '' # todo: replace with remote address in 'Control' tab on the Viam app

async def connect():
  creds = Credentials(
    type='robot-location-secret',
    payload=SECRET_FROM_VIAM_APP)
  opts = RobotClient.Options(refresh_interval=0,
                    dial_options=DialOptions(credentials=creds))
  return await RobotClient.at_address(ADDRESS_FROM_VIAM_APP,
                                      opts)


async def moveInSquare(base):
  for _ in range(4):
    # moves the rover forward 500mm at 500mm/s
    await base.move_straight(velocity=500, distance=500)
    print("move straight")
    # spins the rover 90 degrees at 100 degrees per second
    await base.spin(velocity=100, angle=90)
    print("spin 90 degrees")


async def main():
  robot = await connect()
  base = Base.from_robot(robot, 'viam_base')
  await moveInSquare(base)

  # Don't forget to close the robot when you're done!
  await robot.close()


if __name__ == '__main__':
  asyncio.run(main())
