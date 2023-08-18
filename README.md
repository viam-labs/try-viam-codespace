# viam-python
Try out the [Python Viam SDK](https://python.viam.dev/) and use code to control a [robot in our lab](https://app.viam.com/try)!

## Get Started

1. Access this repo in a web browser at: https://github.com/viam-labs/try-viam-codespace .
1. Open a new [GitHub Codespace](https://github.com/features/codespaces) using this repo as a template by clicking the green **Use this template** button, and selecting **Open in a codespace**.
1. In a separate browser window, head to [Try Viam](https://app.viam.com/try), start a new session by clicking **Try Now**. If you haven’t already, you will need to [create a Viam account](https://docs.viam.com/manage/#create-account-and-log-in). Wait for configuration to complete, then click **Try My Rover** when ready.
1. In the **Control** tab, find the `viam_base` control panel, and enable the `cam` and `overhead-cam:overheadcam` cameras. You should see live feeds from its forward-facing webcam, as well as an external overhead camera.
1. Next, switch to the **Code sample** tab, and enable the **Include secret** toggle.
1. Copy the location secret, (the `payload`) shown in the **Code sample** tab and paste it between the single quotes for `SECRET_FROM_VIAM_APP` in `drive.py`.
1. Similarly, copy the robot address within `RobotClient.at_address()` shown in the **Code sample** tab and paste it between the single quotes for `ADDRESS_FROM_VIAM_APP` in `drive.py`. Only copy the hostname, ending with `viam.cloud`.
1. Return to the Terminal in your GitHub editor window, and run the Python code:

   ```sh
   python drive.py
   ```

You should see the robot move in the controls tab of the Try Viam app!
