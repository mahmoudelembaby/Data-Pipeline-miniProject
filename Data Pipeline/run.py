import logging, json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions, StandardOptions, GoogleCloudOptions

subscription = "projects/PROJECT/subscriptions/SUBSCRIPTION"
project_id = "PROJECT"

def run(argv=None):
    """Build and run the pipeline."""
    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True
    p = beam.Pipeline(options=options)

    # Big query configs
    table_spec = "PROJECT:DATASET.TABLE"
    table_schema = "deviceId:STRING,temperature:FLOAT,longitude:FLOAT,latitude:FLOAT,time:TIMESTAMP"

    # Read from PubSub into a PCollection.
    messages = (
            p | 'Read From PubSub' >> beam.io.ReadFromPubSub(subscription=subscription).with_output_types(bytes)
            | 'Decoding' >> beam.Map(lambda x: x.decode('utf-8'))
            | 'Extract elements' >> beam.ParDo(Split().with_output_types('unicode'))
            | 'Write into Bigtable' >> beam.io.WriteToBigQuery(
                    table_spec,
                    schema=table_schema,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
        )
    )

    result = p.run()
    result.wait_until_finish()