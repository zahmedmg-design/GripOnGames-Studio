from obsws_python import ReqClient


class OBSController:

    def __init__(
        self,
        host="localhost",
        port=4455,
        password="HThqP9Ey8G2sCgmz",
    ):

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