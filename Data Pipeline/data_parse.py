class Split(beam.DoFn):

    def process(self, element):
        element = json.loads(element)
        return [{
            'deviceId': element["deviceId"],
            'temperature': element["temperature"],
            'longitude': element["location"][0],
            'latitude': element["location"][1],
            'time': element["time"]
        }]