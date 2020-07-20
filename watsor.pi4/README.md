# Watsor

[Watsor](https://github.com/asmirnou/watsor) detects objects in video stream using deep learning-based approach. Intended primarily for surveillance it works in sheer real-time analysing the most recent frame to deliver fastest reaction against a detected threat.

## Getting started

This add-on is for Raspberry Pi 4 with 64-bit OS.

Bear in mind that object detection as such requires much computation. To get decent performance on a device such as Raspberry Pi you need [the Coral USB accelerator](https://coral.ai/products/accelerator/). Without the accelerator Raspberry Pi 3 can process only 1 FPS, Raspberry Pi 4 - 5 FPS. The accelerator boost the performance up to 7 for Raspberry Pi 3 and 30 FPS for Raspberry Pi 4.

### Configuration

Having installed Watsor add-on, you need to prepare configuration file, describing the cameras you've got and few other options such as types of detections and zones. Refer to the following [guide](https://github.com/asmirnou/watsor#configuration).

YAML configuration file is supposed to be in Home Assistant config folder. The default path to the file `/config/watsor/config.yaml` can be changed at _Configuration_ tab of the add-on. Using another add-on File Editor create the folder `watsor` and put there prepared YAML file `config.yaml`.

Additional files such as mask images can be uploaded to the same folder. A path to the mask image can be relative to the location of config file. Any sensitive information in the config file can be loaded from the Home Assistant `secrets.yaml` file.

### Running

Disable protection mode if you use USB accelerator. The add-on as such doesn't require full access, but without it the USB device may not be activated at the very first time. 

Start the add-on. Wait for couple of seconds and take a look at the log to make sure it's running and you see `Starting Watsor on local-watsor with PID X` message.

Click on _OPEN WEB UI_ to navigate to a simple home page, where you'll find the links to the cameras video streams, snapshots of object detected classes and metrics.

### Troubleshooting

Depending on whether protection mode is enabled or not, the following messages appear at the start (both can be ignored):

- The add-on conainer starts the daemon to detect dynamically plugged devices and this requries the protection mode enabled.

    ```
    Unable to start udev, container must be run in privileged mode to start udev!
    ```

    The add-on most probably will fail to detect USB accelerator for the first time and has to be started again. 

- The supervisor of Home Assistant passes the virtual device that can not be mounted inside the container.

    ```
    mount: /tmp/tmpmount/console: special device /dev/console does not exist.
    umount: /dev: target is busy.
    ```

    Ignore the message as it doesn't affect the application.
