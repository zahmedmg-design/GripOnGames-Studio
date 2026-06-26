from obsws_python import ReqClient


class OBSController:
    def __init__(self, host="localhost", port=4455, password="HThqP9Ey8G2sCgmz"):
        self.host = host
        self.port = port
        self.password = password
        self.client = None

    def connect(self):
        try:
            self.client = ReqClient(
                host=self.host,
                port=self.port,
                password=self.password
            )
            version = self.client.get_version()
            return True, f"Connected to OBS {version.obs_version}"
        except Exception as e:
            return False, str(e)

    def start_stream(self):
        try:
            if self.client is None:
                return False, "OBS is not connected."
            self.client.start_stream()
            return True, "Stream started."
        except Exception as e:
            return False, f"Could not start stream: {e}"

    def stop_stream(self):
        try:
            if self.client is None:
                return False, "OBS is not connected."
            self.client.stop_stream()
            return True, "Stream stopped."
        except Exception as e:
            return False, f"Could not stop stream: {e}"

    def start_recording(self):
        try:
            if self.client is None:
                return False, "OBS is not connected."
            self.client.start_record()
            return True, "Recording started."
        except Exception as e:
            return False, f"Could not start recording: {e}"

    def stop_recording(self):
        try:
            if self.client is None:
                return False, "OBS is not connected."
            self.client.stop_record()
            return True, "Recording stopped."
        except Exception as e:
            return False, f"Could not stop recording: {e}"