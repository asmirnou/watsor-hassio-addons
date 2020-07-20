# Watsor

[Watsor](https://github.com/asmirnou/watsor) detects objects in video stream using deep learning-based approach. Intended primarily for surveillance it works in sheer real-time analysing the most recent frame to deliver fastest reaction against a detected threat.

## Configuration

Having installed Watsor add-on, you need to prepare configuration file, describing the cameras you've got and few other options such as types of detections and zones. Refer to the following [guide](https://github.com/asmirnou/watsor#configuration).

YAML configuration file is supposed to be in Home Assistant config folder. The default path to the file `/config/watsor/config.yaml` can be changed at _Configuration_ tab of the add-on. Using another add-on File Editor create the folder `watsor` and put there prepared YAML file `config.yaml`.

Additional files such as mask images can be uploaded to the same folder. A path to the mask image can be relative to the location of config file. Any sensitive information in the config file can be loaded from the Home Assistant `secrets.yaml` file.

## Running

Start the add-on. Wait for couple of seconds and take a look at the log to make sure it's running and you see `Starting Watsor on local-watsor with PID X` message.

Click on _OPEN WEB UI_ to navigate to a simple home page, where you'll find the links to the cameras video streams, snapshots of object detected classes and metrics.
